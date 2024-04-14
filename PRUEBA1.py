# -*- coding: utf-8 -*-
import serial
import time
from time import sleep
import os, sys
import webbrowser
import subprocess
from subprocess import Popen
import RPi.GPIO as GPIO
import Tkinter as tk
from Tkinter import *
import os, time, threading, random
import feedparser
##import wget


GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

d = 1
s = 1
quit_video = True
#estado1 = True
#estado2 = False
input_state1= True
input_state2= True

last_state1= True
last_state2= True

player = False

#movie1= ()
#movie2= ()
#movie3= ()
#movie4= ()
#movie5= ()
#movie6= ()

estado1=["/home/pi/Documents/estado1.mp4","/home/pi/Documents/estado1-1.mp4","/home/pi/Documents/estado1-2.mp4"]
estado2=["/home/pi/Documents/estado2.mp4","/home/pi/Documents/estado2.mp4","/home/pi/Documents/estado2.mp4"]
posicion = 0
posicion1 = 0

arduino = serial.Serial("/dev/ttyACM0", baudrate=9600, timeout= 1.0)

arduino.setDTR(False)
time.sleep(1)
arduino.flushInput()
arduino.setDTR(True)




noticias=feedparser.parse('http://www.eltiempo.com/rss/colombia.xml')
noticias1=feedparser.parse('http://www.eltiempo.com/rss/bogota.xml')
noticias2=feedparser.parse( 'http://www.eltiempo.com/rss/mundo.xml')

root = tk.Tk()
root.config(bg="black")
root.title('SECCION DE NOTICIAS')
root.geometry("1080x100+0+1730")
deli = 50
time1 =''
svar= tk.StringVar()
labl = tk.Label(root, textvariable=svar, height=10, width=200, font=('Consolas', 40), bg='black', fg='white')
clock= Label(root, font=('Consolas', 40), bg="Black", fg="white")
clock.pack()
clock.place (x=0, y=23)

def reloj ():
    global time1
    time2 = time.strftime('%H:%M')
    if time2 != time1:
        time1 = time2
        clock.configure (text=time2)
    clock.after(500,reloj)

def shif():
    shif.msg = shif.msg[1:] + shif.msg[0]
    svar.set(shif.msg)
    root.after(deli, shif)
shif.msg=noticias['entries'][0]['title'] + noticias1['entries'][0]['title'] + noticias2['entries'][0]['title']
shif()
labl.pack()
reloj()

os.system('killall omxplayer.bin')
omxc= Popen(['omxplayer','--win','0,0,1080,1795','--loop',estado1[posicion]])

while (s == 1):
    try:
        val = arduino.readline()
        print(val)
        distancia = int(val)
    except:
        os.system("reboot")
    root.update()
        #print(distancia)        
    quit_video = GPIO.input(24)
    if(posicion == 3):
        posicion = 0
    posicion1 = posicion + 1
        ##se determina el estado que se encuentra el sistema
    if (distancia > 30):
        input_state1 = True
        input_state2 = False
        if (input_state1 != last_state1):
            os.system('killall omxplayer.bin')
            omxc= Popen(['omxplayer','--win','0,0,1080,1795','--loop',estado1[posicion]])
            print(estado1[posicion])
            print("ESTADO 1")
            posicion+=1
            time.sleep(1)
            pass
                
            
    elif (distancia <= 25):
        input_state1 = False
        input_state2 = True
            
        if (input_state2 != last_state2):
            if (posicion1 == 3):
                posicion1 = 0
            os.system('killall omxplayer.bin')
            omxc= Popen(['omxplayer','--win','0,0,1080,1795','--loop',estado2[posicion1]])
            print("ESTADO 2")
            posicion+=1
            time.sleep(1)
            pass
                
        
        ##si no lectura de sensor
    elif (player and input_state1 and input_state2):
        os.system('killall omxplayer.bin')
        player = False
        
        ##close sistem
    if (quit_video == False):
        os.system('killall omxplayer.bin')
        player = False
        break
        
            
    ##se determina el estado anterior
        
    last_state1= input_state1
    last_state2= input_state2
    ##print(posicion)
        