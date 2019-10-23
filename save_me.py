import socket
import curses
import serial
import struct
import time
import cv2
import numpy as np

import os
import datetime
import RPi.GPIO as gpio

import io
import pickle
import zlib

from twilio.rest import Client

account_sid = 'ACec8b09987b86f06aebdcd9fe660a5b69' 
auth_token = '2734e7a3f7dbf66ea4cebd651eaf6214' 

myPhone = '+8801521313223' 
TwilioNumber = '+12512548095' 



gpio.setmode(gpio.BOARD)
gpio.setwarnings(0)
gpio.setup(7,gpio.IN, pull_up_down=gpio.PUD_DOWN)
cnt = 0 


print("Client Created")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.43.158', 8486))

print("Client Bound")

connection = client_socket.makefile('wb')

rp=client_socket.recv(1024)
location=rp.decode('utf-8')

#print("")


while 1:    
    if gpio.input(7)==gpio.HIGH:
       #
       #fswebcam -p YUYV -d /dev/video0 -r 640x480 $DIR/$filename
        print("button pushed")

        time.sleep(2)
        name='fswebcam -p YUYV -d /dev/video0 -r 640x480 /home/pi/Desktop/save_me/cap'+str(cnt)+'.jpg'
        os.system(name)
        
        time.sleep(2)
        
        
        msg= "I'm in danger. Rescue me. My location : "+str(location)
        directory='/home/pi/Desktop/save_me/cap'+str(cnt)+'.jpg'

        client = Client(account_sid, auth_token)
        client.messages.create(
            to=myPhone,
            from_=TwilioNumber,
            body=msg)
        time.sleep(2)
        cnt=cnt+1
        cam = cv2.VideoCapture(0)

        cam.set(3, 320);
        cam.set(4, 240);

        img_counter = 0

        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

        while gpio.input(7)==gpio.HIGH:
            ret, frame = cam.read()
            result, frame = cv2.imencode('.jpg', frame, encode_param)
        #    data = zlib.compress(pickle.dumps(frame, 0))
            data = pickle.dumps(frame, 0)
            size = len(data)

            
            print("{}: {}".format(img_counter, size))
            client_socket.sendall(struct.pack(">L", size) + data)
            img_counter += 1



        cam.release()

        

        

        
    
        
