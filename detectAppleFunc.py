# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 21:25:27 2020
######################################################################
# Development Of an Embedded  Vision Based Fruit Sorting Machine #####
@author: CLARY NORMAN (2017141960)                               ####
"""                                                             #####
####################################################################
import numpy as np
import cv2 

def detectApple(I):    
    # load or hard code your parameters here
    mu = np.array([167.978,76.6507,65.574])
    sigma = np.array([[1068.4,1003.08,640.939],[1003.08,1468.42,999.001],[640.939,999.001,784.846]])
    threshold = 2.13807e-8
    D = 3
    ########################################################################################################################
    # find the ball color pixel using your model
    ########################################################################################################################
    #output = cv2.resize(I, (400,400))
    im_rgb1 = cv2.cvtColor(I, cv2.COLOR_BGR2RGB)
    im_rgb = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
    #cv2.imshow('Origial Apple fruit',output)

    R = im_rgb1[:,:,0]
    G = im_rgb1[:,:,1]
    B = im_rgb1[:,:,2]

    S1 = np.zeros([50,50])

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
                     S1[m,n] = True
      # Calculating the pixel of the Orange fruit            
    pixels = cv2.countNonZero(S1) 
    image_area = im_rgb1.shape[0] * im_rgb1.shape[1]
    area_ratio = (pixels / image_area) * 100  
    # apply morphological method to fill the holes
    kernel = np.ones((5,5),np.uint8)
    dilation = cv2.dilate(S1,kernel,iterations = 1)
    closing1 = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel) 
   # covert binary image to its original image without the background
    mask = np.atleast_3d(closing1)
    red = np.uint8(mask)*I
    return red,area_ratio,closing1,I
    