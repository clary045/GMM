#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 08:37:40 2020

@author: pi
"""

from picamera import PiCamera
from picamera.array import PiRGBArray
import time 
import cv2
import pickle
import numpy as np
import matplotlib.pyplot as plt
import random 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.svm import SVC

camera = PiCamera()

for i in range (50):
        #camera.capture("/home/pi/Desktop/newfile/" + i + ".jpg")
        rawCapture = PiRGBArray(camera)
        time.sleep(0.5)
        #t.start()
        camera.capture(rawCapture,format = 'bgr')
        I = rawCapture.array
        show = cv2.cvtColor(I, cv2.COLOR_BGR2RGB)
        I = cv2.resize(I, (50,50))
        from detectOrangeFunc import detectOrange
        [y,x,r,z] = detectOrange(I)

        from detectAppleFunc import detectApple
        [y1,x1,t,z1] = detectApple(I)

        # Classify whether apple or Orange
        if x >x1:
            print("Orange")
            plt.imshow(show,cmap = 'gray')
            plt.show()

        elif x1 > x:
            print("Apple")
            plt.imshow(show,cmap = 'gray')
            plt.show()



 