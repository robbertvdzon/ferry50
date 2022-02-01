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

### Clone the project from github
```
git clone https://github.com/robbertvdzon/ferry50.git
```

### Make sure to start the robot and video player at boot time 
cp ~/ferry50/autostart /home/pi/.config/lxsession/LXDE-pi/

### Install bwbasic (for programming sample)
```
sudo apt install bwbasic
```

### Record video
```
sudo apt install kazam
```

