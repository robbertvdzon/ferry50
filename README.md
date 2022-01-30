# Ferry's programmerende abraham pop

## Configure Raspberry pi:
### Enable ssh and i2c 
```
sudo raspi-config
```

### Install Python
```
sudo pip3 install adafruit-circuitpython-pca9685
sudo pip3 install adafruit-circuitpython-servokit
```
### Copy apps and video's to the pi 
Copy the following files to ~:
- abraham.py
- abraham.mp4

### Start application at boot time
Create the following file '/home/pi/.config/lxsession/LXDE-pi/autostart'
echo '/usr/bin/python /home/pi/abraham.py' >> /home/pi/.config/lxsession/LXDE-pi/autostart



