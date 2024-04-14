import requests
import socket
import psutil
import os
import subprocess
from uuid import getnode as get_mac
import base64



def peticion():
    payload = {
        "id_espejo": "YXRVkKddBfALKEBatMAr",
        "screenshot": "data:image/png;base64,",
        "ip_publica": "1213325435",
        "ip_privada": "3454656757",
        "mac": "MchErtYY",
        "tipo": "Tipo",
        "impactos": "Impactos",
        "stats_cpu": "stats_cpu",
        "stats_ramt": "stats_ramt",
        "stats_ramu": "stats_ramu",
        "stats_raml": "stats_raml",
        "stats_tempc": "stats_tempc",
        "stats_tempg": "stats_tempg",
        "stats_uptime": "stats_uptime",
        "log_service1": "log_service1",
        "log_service2": "log_service2",
        "ssh": [{"url": "url", "port": "port"}],
        "informacion": [{"informacion": "Informacion adicional"}]
    }
    ip = requests.get('https://api.ipify.org').text
    nombre_equipo = socket.gethostname()
    direccion_equipo = socket.gethostbyname(nombre_equipo)
    mac = get_mac()
    mac = ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
    cmd = "/bin/cat /proc/uptime"
    (status, output) = subprocess.getstatusoutput(cmd)
    
    ''' REALIZA CAMPTURA DE PANTALLA '''
    encoded = base64.b64encode(open("/home/pi/estado1.png", "rb").read())
    img_captura = encoded.decode('ascii')
    # print(impactos)
    ''' LEER ARCHIVO DE REGISTRO DE IMPACTOS '''
    f = open ('/home/pi/Documents/DigitalSignage/db.txt','r')
    impactos = str(f.read())
    f.close

    opcion = {
         "id_espejo": "YXRVkKddBfALKEBatMAr",
         "screenshot": img_captura,
         'ip_privada' : direccion_equipo,
         'ip_publica' : format(ip),
         'mac' : mac,
         "tipo": "Tipo",
         "impactos": impactos,
         'stats_cpu' : psutil.cpu_percent(),
         'stats_ramt' : psutil.virtual_memory().total,
         'stats_ramu' : psutil.virtual_memory().used,
         'stats_raml' : psutil.virtual_memory().available,
         'stats_tempc' : subprocess.getstatusoutput('cat /sys/class/thermal/thermal_zone0/temp'),
         'stats_tempg' : subprocess.getstatusoutput('/opt/vc/bin/vcgencmd measure_temp'),
         'stats_uptime' : output.split()[0],
         "ssh": [{"url": "url", "port": "port"}],
         'log_service1' : subprocess.getstatusoutput('systemctl status wmm1.service'),
         'log_service2' : subprocess.getstatusoutput('systemctl status wmm2.service'),
         'informacion' : [{"informacion": subprocess.getstatusoutput('tvservice -s')}]

    }
    resp2 = requests.put('https://api-espejos-i.herokuapp.com/info/YXRVkKddBfALKEBatMAr', json=opcion)

    for key in opcion:
     print(key, ":", opcion[key])

peticion()