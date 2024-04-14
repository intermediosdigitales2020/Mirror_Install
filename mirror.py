# -*- coding: utf-8 -*-

import os
import sys
import time
import serial
import subprocess
from subprocess import Popen
import RPi.GPIO as GPIO
import requests
import socket


# >> Configura pines GPIO para uso de sensores.
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN)


# >> Crea un objeto socket para el servidor y se conecta. 
s = socket.socket()
s.connect(("192.168.1.120", 9999))


# >> Configura ruta del proyecto, librerias y archivos de video.
files_path = ("/home/pi/Documents/DigitalSignage/")
dbus_file = ("dbuscontrolm.sh")
movie1 = (files_path + "estado1.mp4")
movie2 = (files_path + "estado2.mp4")


# >> Configura e inicializa la comunicacion serial con el Arduino y variable DISTANCIA.
arduino = serial.Serial('/dev/ttyACM0',baudrate=9600, timeout = 3.0)
arduino.setDTR(False)
time.sleep(1)
arduino.flushInput()
arduino.setDTR(True)
distancia = 0


# >> Inicializa estado del boton KILLALL.
killapp = True


# >> Declara el estado inicial del PRIMER_ARRANQUE, ESTADO_1, ESTADO_2.
first_run = 0
init_estado1 = 0
init_estado2 = 0


# >> DECLARA PLAYER que almacena estado abierto/cerrado del reproductor.
player = False
momento = 0
rpi_type = 1 # ++  MASTER: 0, SLAVE: 1
r = 0


# >> INCIA PROGRAMA PRINCIPAL.
while True:

    if momento <= 5:
        momento = momento + 1
        # time.sleep(2)
        # print(momento)


    # >> Lee estado del boton KILLALL
    killapp = GPIO.input(2)


    # >> Lee dato del arduino y almacena resultado en la variable DISTANCIA.
    try:
        val = arduino.readline()
        distancia = int(val)
        print(distancia)
    except:
        print('======== REBOOT ========')
        #os.system("reboot")

    # >> Inicia instancias de OMXPLAYER para el ESTADO_1 y ESTADO_2, asegurando una sola ejecucion.
    if first_run == 0:
        os.system('killall omxplayer.bin') # ++ Termina cualquier instancia de OMXPLAYER no relacionada con el programa.
        omxc1 = Popen(['omxplayer', '--win','0,0,1080,1790', '--no-osd', '--loop', '--layer', '1', '--dbus_name', 'org.mpris.MediaPlayer2.omxplayer', movie1])
        omxc2 = Popen(['omxplayer', '--win','0,0,1080,1790', '--no-osd', '--loop', '--layer', '5', '--dbus_name', 'org.mpris.MediaPlayer2.omxplayer2', movie2])
        first_run = 1 # ++ Actualiza estado del PRIMER_ARRANQUE para evitar crear instanciad adicionales de OMXPLAYER.
        player = True

    # >> Muestra el ESTADO_2 si la distancia es igual o menor a 25 y oculta si es igual o mayor a 26.
    if (first_run == 1 and distancia <= 25):
        subprocess.call([files_path + dbus_file + " unhidevideo"], shell = True)
        # print("MOSTRAR ESTADO 2")
    elif (first_run == 1 and distancia >= 26):
        subprocess.call([files_path + dbus_file + " hidevideo"], shell = True)
        # print("OCULTAR ESTADO 2")

    # r = requests.get("http://192.168.1.120:8080/timecode/")
    # if r.status_code == 200:
        # print (r.text)

    s.send('timecode')
    r = s.recv(65507)

    # >> Obtiene el timecode del MASTER y sincroniza el video.
    if (player and first_run == 1 and momento == 5 and rpi_type == 1):
        print (r)
        try:
            subprocess.call([files_path + dbus_file + " setposition " + r], shell = True)
            momento = 0
        except:
            omxc1 = Popen(['omxplayer', '--win','0,0,1080,1790', '--no-osd', '--loop', '--layer', '1', '--dbus_name', 'org.mpris.MediaPlayer2.omxplayer', movie1])
            pass


    # >> Cierra todas las instancias de OMXPLAYER, configura PLAYER en 0 y finaliza la ejecucion
    #       del programa al oprimir el boton KILLALL.
    if (killapp == False):
        os.system('killall omxplayer.bin')
        player = False
        sys.exit()


# >> Cierra conexion socket con servidor.
s.close()


# >>>>>>>>>> FIN DEL PROGRAMA <<<<<<<<<<