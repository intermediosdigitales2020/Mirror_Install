#import firebase_admin
#from firebase_admin import credentials
#from firebase_admin import firestore
##

import json
import sys, getopt
import os
import sys

import time
import serial
import subprocess
from subprocess import Popen
import socket





# >> Configura ruta del proyecto, librerias y archivos de video.
files_path = ("/home/pi/Documents/estado2/")
dbus_file = ("dbuscontrolm.sh")
db=(" python /home/pi/Documents/DigitalSignage/")
movie1 = (files_path + "estado1.mp4")
movie2_1 = (files_path + "estado2.mp4")
movie2_2 = (files_path + "estado2-1.mp4")
movie2_3 = (files_path + "estado2-2.mp4")
movie2_4 = (files_path + "estado2-3.mp4")
movie2_5 = (files_path + "estado2-4.mp4")
movie2_6 = (files_path + "estado2-5.mp4")
movie2_7 = (files_path + "estado2-6.mp4")
movie2_8 = (files_path + "estado2-7.mp4")
movie2_9 = (files_path + "estado2-8.mp4")
movie2_10 = (files_path + "estado2-9.mp4")
movie2_11 = (files_path + "estado2-10.mp4")






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
impactos = 0
tiempo_final = 0
tiempo_pauta = 70
# >> DECLARA PLAYER que almacena estado abierto/cerrado del reproductor.
player = False
momento = 0
#rpi_type = 1 # ++  MASTER: 0, SLAVE: 1
#r = 0
# >> INCIA PROGRAMA PRINCIPAL.

#omxplayer_sync = subprocess.Popen(['omxplayer-sync','-muv', movie1],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
#
master = False
#texto de salida 
f = open ('/home/pi/Documents/DigitalSignage/verificacion.txt','w')
f.write('segundoestadook'+ time.strftime("%c") )
f.close()


while True:
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        client.bind(("", 1677))
    except:
        if(master == True):
            print('===REBOOT AUTOMATICO====')
            f = open ('/home/pi/Documents/DigitalSignage/verificacion.txt','w')
            f.write('error 1103' + time.strftime("%c") )
            f.close()
        elif(master == False):
            continue
    
    try:
        try:
            val = arduino.readline()
            distancia = int(val)
            print(distancia)
        except:
            print('======== REBOOT ========')
            f = open ('/home/pi/Documents/DigitalSignage/verificacion.txt','w')
            f.write('error 1102 Fecha y hora' + time.strftime("%c"))
            f.close()
        
        if( 10 < distancia <= 50):
            #c = open ('/home/pi/Documents/DigitalSignage/cliente1.txt','r')
            #i = cliente1.read()
            #c.close
            #c = open ('/home/pi/Documents/DigitalSignage/cliente1.txt','w')
            ##impactos = i + 1
            #print(impactos)
           # c.write(impactos)
           # c.close()
            input_state1 = True 
            input_state2 = False 
            if (input_state1 != last_state1):
                f = open ('/home/pi/Documents/DigitalSignage/estado2.txt','w')
                f.write('true')
                f.close()
                e = open ('/home/pi/Documents/DigitalSignage/estado2log.txt','a')
                e.write('true' + '' + time.strftime("%c") + '\n')
                e.close()
                data = client.recv(1024)
                datax = data.decode('utf-8')
                dataz = int(datax)
                print(dataz)
                #client.close()
                
                    
                if (dataz == 1):
                    eleccion = 3
                elif (dataz == 2):
                    eleccion = 4
                elif (dataz == 0):
                    eleccion = 1
                elif (dataz == 3):
                    eleccion = 5
                elif (dataz == 4):
                    eleccion = 2
                elif (dataz == 5):
                    eleccion = 6
                elif (dataz == 6):
                    eleccion = 7
                elif (dataz == 7):
                    eleccion = 8
                elif (dataz == 8):
                    eleccion = 9
                elif (dataz == 9):
                    eleccion = 10
                elif (dataz == 10):
                    eleccion = 11
                else:
                    eleccion = 1
                
                if (eleccion == 1) :
                    omxprocess = subprocess.Popen(['omxplayer','--loop','--layer','5','--win','0,0,1080,1800', movie2_1],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
                    time.sleep(4)
                    print("video1")
                    os.system(db + "db.py -s 1")
                elif (eleccion == 2):
                    print("video2")
                    omxprocess = subprocess.Popen(['omxplayer','--loop','--layer','5','--win','0,0,1080,1800', movie2_2],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
                    time.sleep(4)
                    print("video1")
                    os.system(db + "db.py -s 2")
                elif (eleccion == 3):
                    print("video3")
                    omxprocess = subprocess.Popen(['omxplayer','--loop','--layer','5','--win','0,0,1080,1800', movie2_3],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
                    time.sleep(4)
                    print("video1")
                    os.system(db + "db.py -s 3")
                elif (eleccion == 4):
                    print("video4")
                    omxprocess = subprocess.Popen(['omxplayer','--loop','--layer','5','--win','0,0,1080,1800', movie2_4],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
                    time.sleep(4)
                    print("video1")
                    os.system(db + "db.py -s 4")
                elif (eleccion == 5):
                    print("video5")
                    omxprocess = subprocess.Popen(['omxplayer','--loop','--layer','5','--win','0,0,1080,1800', movie2_5],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
                    time.sleep(4)
                    print("video1")
                    os.system(db + "db.py -s 5")
                elif (eleccion == 6):
                    print("video6")
                    omxprocess = subprocess.Popen(['omxplayer','--loop','--layer','5','--win','0,0,1080,1800', movie2_6],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
                    time.sleep(4)
                    print("video1")
                    os.system(db + "db.py -s 6")
                elif (eleccion == 7):
                    print("video7")
                    omxprocess = subprocess.Popen(['omxplayer','--loop','--layer','5','--win','0,0,1080,1800', movie2_7],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
                    time.sleep(4)
                    print("video1")
                    os.system(db + "db.py -s 7")
                elif (eleccion == 8):
                    print("video8")
                    omxprocess = subprocess.Popen(['omxplayer','--loop','--layer','5','--win','0,0,1080,1800', movie2_8],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
                    time.sleep(4)
                    print("video1")
                    os.system(db + "db.py -s 8")
                elif (eleccion == 9):
                    print("video9")
                    omxprocess = subprocess.Popen(['omxplayer','--loop','--layer','5','--win','0,0,1080,1800', movie2_9],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
                    os.system(db + "db.py -s 9")
                elif (eleccion == 10):
                    print("video10")
                    omxprocess = subprocess.Popen(['omxplayer','--loop','--layer','5','--win','0,0,1080,1800', movie2_10],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
                    os.system(db + "db.py -s 10")
                else:
                    print("video sin cliente")
                    omxprocess = subprocess.Popen(['omxplayer','--loop','--layer','5','--win','0,0,1080,1800', movie2_2],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
                    os.system(db + "db.py -s 10")
                
        
        if (distancia >= 80):
            input_state1 = False  
            input_state2 = True
            if (input_state2 != last_state2):
                f = open ('/home/pi/Documents/DigitalSignage/estado2.txt','w')
                f.write('false')
                f.close()  
                init_estado2 = False
                time.sleep(1)
                arduino.setDTR(False)
                time.sleep(1)
                arduino.flushInput()
                arduino.setDTR(True)
                time.sleep(1)
                omxprocess.terminate()
                omxprocess.stdin.write(b'q')
                omxprocess.stdin.flush()
                datax = ''
                           
                
        

        last_state1= input_state1
        last_state2= input_state2
        
        # >> Lee dato del arduino y almacena resultado en la variable DISTANCIA.
    except:
        print("error de video ... reinicio")
        input_state1= True
        input_state2= True
        last_state1= True
        last_state2= True
        f = open ('/home/pi/Documents/DigitalSignage/verificacion.txt','w')
        f.write('error 1101' + time.strftime("%c"))
        f.close()

    
# >>>>>>>>>> FIN DEL PROGRAMA <<<<<<<<<<
print("error termina el programa")
