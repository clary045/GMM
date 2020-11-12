# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 23:29:39 2020
######################################################################
# Development Of an Embedded  Vision Based Fruit Sorting Machine #####
@author: CLARY NORMAN (2017141960)                               ####
"""                                                             #####
####################################################################
import numpy as np
import cv2 

def detectOrange(I):
   # load or hard code your parameters here
   mu = np.array([200.224,123.543,32.4314])
   #m1 = mu.reshape(1,3)
   sigma = np.array([[746.829,613.434,114.998],[613.434,724.818,380.201],[114.998,380.201,698.326]])
   threshold = 2.04108e-07
   D = 3
   ########################################################################################################################
   # find the ball color pixel using your model
   ########################################################################################################################
   #output1 = cv2.resize(I, (400,400))
   im_rgb1 = cv2.cvtColor(I, cv2.COLOR_BGR2RGB)
   im_rgb = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
#   cv2.imshow('Origial Orange fruit',output)


   R = im_rgb1[:,:,0]
   G = im_rgb1[:,:,1]
   B = im_rgb1[:,:,2]

   S = np.zeros([50,50])

   for m in range(50):
       for n in range (50):
           r = R[m,n]
           g = G[m,n]
           b = B[m,n]
           x = np.double([r,g ,b])
           SIGMA_inv = np.linalg.inv(sigma)
           denominator = np.sqrt((2 * np.pi)**D * np.linalg.det(sigma))
           exponent = -(1/2) * ((x - mu).T @ SIGMA_inv @ (x - mu ))
           p = float((1. / denominator) * np.exp(exponent) ) 
           if (p > threshold):
               S[m,n] = True

   # Calculating the pixel of the Orange fruit            
   pixels = cv2.countNonZero(S) 
   image_area = im_rgb1.shape[0] * im_rgb1.shape[1]
   area_ratio1 = (pixels / image_area) * 100 
   # apply morphological method to fill the holes
   kernel = np.ones((5,5),np.uint8)
   dilation = cv2.dilate(S,kernel,iterations = 1)
   closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel) 
   # covert binary image to its original image without the background
   mask = np.atleast_3d(closing)
   red1 = np.uint8(mask)*I
   return red1,area_ratio1,S,I
