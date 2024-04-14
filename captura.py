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
from urasp import *
from db import *

''' URL DEL API DE WMM-CONTROL '''
API_URL = "http://control.mirrormarketing.com.co/api/mirrors/"
''' CONFIGURACION DEL ESPEJO '''
id_espejo = "15"
img_captura = ""

''' ADQUISICION DE DATOS TECNICOS '''
''' Network '''
ipaddress = IPAddress()
ipaddr = ipaddress.get_ipaddress()
macaddr = get_mac()
device = ':'.join(("%012X" % macaddr)[i:i+2] for i in range(0, 12, 2))


#NOMBRE WIFI
f = open ('/home/pi/Documents/DigitalSignage/wifi.txt','r')
wifissid = str(f.read())
f.close




''' Resources '''
cpu = get_cpuload() # in % percent
ramt = str(ram[0]) # in Kb Kilobytes
ramu = str(ram[1]) # in Kb Kilobytes
raml = str(ram[2]) # in Kb Kilobytes
tempcpu = str(get_cpu_temp()) # in ºC Celcius degrees
tempgpu = str(get_gpu_temp()) # in ºC Celcius degrees
uptime = get_uptime() # in HH:MM:SS of time

''' LEER ARCHIVO DE REGISTRO DE IMPACTOS '''
f = open ('/home/pi/Documents/DigitalSignage/db.txt','r')
impactos = "1" #str(f.read())
f.close


''' REALIZA CAMPTURA DE PANTALLA '''
encoded = base64.b64encode(open("/home/pi/estado1.png", "rb").read())
img_captura = encoded.decode('ascii')
# print(impactos)


#STATUS WMM2.SERVICE
os.system('sudo systemctl status wmm2.service > /home/pi/servicio.txt')
f = open ('/home/pi/servicio.txt','r')
statuswmm2 = str(f.read())
f.close

#STATUS WMM1.SERVICE
os.system('sudo systemctl status wmm1.service > /home/pi/servicio1.txt')
f = open ('/home/pi/servicio1.txt','r')
statuswmm1 = str(f.read())
f.close


''' ENVIA DATOS DE ESTADO DEL ESPEJO AL API DE WMM-CONTROL '''
END_API = API_URL + id_espejo
data = {
    'id': id_espejo,
    'thumbnail': img_captura,
    'ipaddress': ipaddr,
    'device': device,
    'wifiname': wifissid,
    'impcount': impactos,
    'stats_cpu': cpu,
    'stats_ramt': ramt,
    'stats_ramu': ramu,
    'stats_raml': raml,
    'stats_tempc': tempcpu,
    'stats_tempg': tempgpu,
    'stats_uptime': uptime,
    'log_service1': statuswmm1,
    'log_service2': statuswmm2
    }
r = requests.put(url = END_API, data = data)

print(r.text)
