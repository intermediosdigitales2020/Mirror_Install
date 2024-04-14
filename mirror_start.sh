#!/bin/bash

# killall omxplayer.bin

# estado1=0
# estado2=0

killall omxplayer.bin

# try {
/home/pi/Documents/DigitalSignage/mirror_s1.sh &
# } catch {
#     sudo reboot
# }

python /home/pi/Documents/DigitalSignage/mirror_s2.py

# estado1=1

# while read -r line < /dev/ttyACM0; do
#   # $line is the line read, do something with it
#     if [ $line -gt 30 ]
#     then
#         echo "ABRE ESTADO 1"
#         if [ $estado2 -eq 1 ]
#         then
#             ./dbuscontrolm.sh stop2
#             estado2=0
#         fi
#     else
#         # echo "ESTADO 2"
#         echo "ABRE ESTADO 2"
#         # estado1=1
#         ./mirror_s2.sh &
#         estado2=1
#     fi
# done
