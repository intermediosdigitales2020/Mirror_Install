#! /usr/bin/python
# encoding: utf-8


import socket
import base64
import requests
from uuid import getnode as get_mac
from ipaddress import IPAddress
import os
import sys
import subprocess
import time
import db
from db import *


impacto2 = os.system("sudo python /home/pi/Documents/DigitalSignage/db.py -a")
impactos = db.leer_todos()

f = open ('/home/pi/Documents/DigitalSignage/impactos.txt','w')
f.write(impactos)
f.close

cliente1 = db.leer(1)
f = open ('/home/pi/Documents/DigitalSignage/dato1.txt','w')
f.write(str(cliente1))
f.close

cliente2 = db.leer(2)
f = open ('/home/pi/Documents/DigitalSignage/dato2.txt','w')
f.write(str(cliente2))
f.close

cliente3 = db.leer(3)
f = open ('/home/pi/Documents/DigitalSignage/dato3.txt','w')
f.write(str(cliente3))
f.close

cliente4 = db.leer(4)
f = open ('/home/pi/Documents/DigitalSignage/dato4.txt','w')
f.write(str(cliente4))
f.close

cliente5 = db.leer(5)
f = open ('/home/pi/Documents/DigitalSignage/dato5.txt','w')
f.write(str(cliente5))
f.close

cliente6 = db.leer(6)
f = open ('/home/pi/Documents/DigitalSignage/dato6.txt','w')
f.write(str(cliente6))
f.close

cliente7 = db.leer(7)
f = open ('/home/pi/Documents/DigitalSignage/dato7.txt','w')
f.write(str(cliente7))
f.close

cliente8 = db.leer(8)
f = open ('/home/pi/Documents/DigitalSignage/dato8.txt','w')
f.write(str(cliente8))
f.close

cliente9 = db.leer(9)
f = open ('/home/pi/Documents/DigitalSignage/dato9.txt','w')
f.write(str(cliente9))
f.close

cliente10 = db.leer(10)
f = open ('/home/pi/Documents/DigitalSignage/dato10.txt','w')
f.write(str(cliente10))
f.close



print("BASE DE DATOS COPIADA")