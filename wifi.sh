#!/bin/bash
nombre=$(/sbin/iwgetid wlan0 --raw)
echo $nombre > /home/pi/Documents/DigitalSignage/wifi.txt