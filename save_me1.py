import socket
import curses
import serial
import struct
import time

import numpy as np

import os
import datetime
import RPi.GPIO as gpio



import base64

gpio.setmode(gpio.BOARD)
gpio.setwarnings(0)
gpio.setup(7,gpio.IN, pull_up_down=gpio.PUD_DOWN)
cnt = 0 


host = '192.168.43.158'
port = 5576

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while 1:    
    if gpio.input(7)==gpio.HIGH:
        
        print("button pushed")
        
        time.sleep(2)
        name='fswebcam /home/pi/Desktop/save_me/cap'+str(cnt)+'.jpg'
        os.system(name)
        
        time.sleep(2)
        
        

        directory='/home/pi/Desktop/save_me/cap'+str(cnt)+'.jpg'

        
        with open(directory, "rb") as img_file:
            message = base64.b64encode(img_file.read())
        cnt=cnt+1
        print(len(message))
        s.send(str.encode(message))
        s.close()
        

        
    
        
