# -*- coding: utf-8 -*-

import web
import json
import subprocess
from subprocess import Popen

urls = (
    '/timecode/', 'timecode',
)

application = web.application(urls, globals()).wsgifunc()

files_path = ("/home/pi/Documents/DigitalSignage/")
dbus_file = ("dbuscontrolm.sh")
current_time = ""

class timecode:
    codes = { 400 : '400 Bad Request',
              404 : '404 Not Found',
              405 : '405 Method Not Allowed',
              409 : '409 Conflict'
              }
    def __init__(self):
        web.header('Content-Type', 'application/json', unique=True)

    def GET(self, tcode=None):
        try:
            current_time = subprocess.check_output([files_path + dbus_file + " status"], shell = True)
            output = current_time
            output = output.rstrip('\n')
            return output
        except Exception as e:
            msg, code = e.args if len(e.args)==2 else (e.args, 404)
            raise web.HTTPError(self.codes[code], data="Error: " + str(msg) + "\n")

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()