import httplib, time, os, sys, json


conexión = httplib.HTTPConnection(“localhost”, 8888)

# Solicitar el fichero dynamic.json (formato de datos json)
conexion.request(“GET”,”/dynamic.json”)

# Respuesta del servidor
respuesta = conexion.getresponse()

# A una respuesta correcta obtener los datos en sí mismos
if ( respuesta.status == 200 ):
datos = respuesta.read()
# Abrir una función que analice los datos, comunique
# y encienda la pantalla para mostrar luego los datos
pantalla = json.loads( datos )
lcd.init()
lcd.backlight(1)

# Por ejemplo, obtener temperatura:
rpi_temperatura = temperature
rpi_humidity = humidity

# Cerrar la conexión con el servidor web integrado del RPi-Monitor
conexion.close()
# y apagar pantalla lcd --- enviar a servidor

