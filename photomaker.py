from time import sleep
from picamera import PiCamera
import os
import subprocess

dir = os.getcwd()

n = 1;
for file in os.listdir(dir):
    if file.endswith("duplicate.jpg"):
        n = n;
    elif file.endswith(".jpg"):
        n=n+1;

photoname = 'image%d.jpg'% n
duplicatename = 'image%dduplicate.jpg' %n

camera = PiCamera()
camera.resolution = (320, 240)
camera.start_preview()
# Camera warm-up time

sleep(2)
camera.capture(photoname,'jpeg')

shellcommand1 = 'cp %s %s' % (photoname, duplicatename) #creates a copy of the original image
shellcommand2 = 'jpegoptim -m50 -s %s' % photoname #gives the command for optimising the image and stripping the metadata

subprocess.Popen(shellcommand1, shell=True)
subprocess.Popen(shellcommand2, shell=True)
