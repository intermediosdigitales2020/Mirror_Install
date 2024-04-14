# -*- coding: utf-8 -*-

import os
import sys
import time
import serial
import dbus
import subprocess
from subprocess import Popen
import RPi.GPIO as GPIO


# >> Configura pines GPIO para uso de sensores.
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN)


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
input_state1= True
input_state2= True

last_state1= True
last_state2= True


# >> DECLARA PLAYER que almacena estado abierto/cerrado del reproductor.
player = False
momento = 0
rpi_type = 1 # ++  MASTER: 0, SLAVE: 1
r = 0
 
 



# >> INCIA PROGRAMA PRINCIPAL.
while True:
    try:
        try:
            val = arduino.readline()
            distancia = int(val)
            print(distancia)
        except:
            print('======== REBOOT ========')
            #os.system("reboot")


        # >> Muestra el ESTADO_2 si la distancia es igual o menor a 25 y oculta si es igual o mayor a 26.
        ##if (distancia <= 25 and init_estado2 == 0):

         def read_position_local(self):
        position_local = self.controller.Position()
        if position_local:
            self.position_local = float(position_local)/1000000
        else:
            return False
        print(position_local)

        ## COMANDO PARA ARRANCAR VIDEO DESDE LA POSICION  -l  --pos n Start position (hh:mm:ss)
        if(distancia <= 25):
            # os.system('omxplayer --dbus_name org.mpris.MediaPlayer2.omxplayer2 estado2.mp4')
            input_state1 = True #david
            input_state2 = False #david
            if (input_state1 != last_state1 and position_local = range(8)): 
                omxprocess = subprocess.Popen(['omxplayer','--loop','--layer','5', '--pos', '00:00:00', movie2],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
                #omxc1 = Popen(['omxplayer', '--no-osd', '--loop', '--layer', '5', '--dbus_name', 'org.mpris.MediaPlayer2.omxplayer2', movie2])
                init_estado2 = True
                print("MOSTRAR ESTADO 2")
            elif (input_state1 != last_state1 and position_local = range(8,15)): 
                omxprocess = subprocess.Popen(['omxplayer','--loop','--layer','5', '--pos', '00:00:08', movie2],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
                #omxc1 = Popen(['omxplayer', '--no-osd', '--loop', '--layer', '5', '--dbus_name', 'org.mpris.MediaPlayer2.omxplayer2', movie2])
                init_estado2 = True
                print("MOSTRAR ESTADO 2-1")
            elif (input_state1 != last_state1 and position_local = range(15,22)): 
                omxprocess = subprocess.Popen(['omxplayer','--loop','--layer','5', '--pos', '00:00:15', movie2],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
                #omxc1 = Popen(['omxplayer', '--no-osd', '--loop', '--layer', '5', '--dbus_name', 'org.mpris.MediaPlayer2.omxplayer2', movie2])
                init_estado2 = True
                print("MOSTRAR ESTADO 2-2")
            elif (input_state1 != last_state1 and position_local = range(22,29)): 
                omxprocess = subprocess.Popen(['omxplayer','--loop','--layer','5', '--pos', '00:00:22', movie2],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
                #omxc1 = Popen(['omxplayer', '--no-osd', '--loop', '--layer', '5', '--dbus_name', 'org.mpris.MediaPlayer2.omxplayer2', movie2])
                init_estado2 = True
                print("MOSTRAR ESTADO 2-2")
            else:
                print("error estado 1")
        

        ##if (distancia >= 35 and init_estado2 == 1):
        if (distancia >= 35):
            input_state1 = False  ##DAvid
            input_state2 = True   ##david      
            if (input_state2 != last_state2): #david
                init_estado2 = False
                print("OCULTAR ESTADO 2")
                time.sleep(3)
                omxprocess.stdin.write(b'q')
            pass
                #subprocess.call([files_path + dbus_file + " stop2"], shell = True)

        last_state1= input_state1
        last_state2= input_state2
        # >> Lee dato del arduino y almacena resultado en la variable DISTANCIA.
    except:
        print("error de video ... reinicio")
        input_state1= True
        input_state2= True

        last_state1= True
        last_state2= True

    
# >>>>>>>>>> FIN DEL PROGRAMA <<<<<<<<<<
print("error termina el programa")
