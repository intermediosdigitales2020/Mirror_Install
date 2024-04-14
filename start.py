import os
import sys
import subprocess
from subprocess import Popen
import RPi.GPIO as GPIO


# >> Configura pines GPIO para uso de sensores.
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)


# >> Inicializa estado del boton KILLALL.
killapp = True
first_run = 0


while True:
    # >> Lee estado del boton KILLALL
    killapp = GPIO.input(4)

    if (first_run == 0):
        # >> Ejecuta los programas principales.
        process1 = subprocess.Popen(['python', 'mirror.py', '&'])
        process2 = subprocess.Popen(['python', 'news_ticker.py', '&'])
        first_run = 1

    # >> Cierra todas las instancias de OMXPLAYER y finaliza la ejecucion
    #       de los programas al oprimir el boton KILLALL.
    if (killapp == True):
        os.system('killall omxplayer.bin')
        os.system('pkill -f mirror.py')
        os.system('pkill -f news_ticker.py')
        sys.exit()
