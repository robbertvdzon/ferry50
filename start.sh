killall python
/usr/bin/python /home/pi/ferry50/zwaailicht.py&
/usr/bin/python /home/pi/ferry50/lampen.py&
/usr/bin/python /home/pi/ferry50/beweeg_armen.py&
/usr/bin/python /home/pi/ferry50/read_sensors.py&
/usr/bin/python /home/pi/ferry50/read_button.py&

/usr/bin/vlc --loop --fullscreen /home/pi/ferry3.avi