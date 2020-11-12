# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 14:36:45 2020
######################################################################
# Development Of an Embedded  Vision Based Fruit Sorting Machine #####
@author: CLARY NORMAN (2017141960)                               ####
"""                                                             #####
####################################################################
# Code for training the model
from mpl_toolkits import mplot3d 
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import numpy

# calculating the mean and standard deviation 
df = pd.read_csv (r'C:\Users\CLARY NORMAN\Documents\2020\2nd semester\Capstone 2\Fruit sorting\samples\apple\Apple_data_training')
#reading dataset 
r = df.iloc[:,0]
g = df.iloc[:,1]
b = df.iloc[:,2]

# Creating figure 
fig = plt.figure(figsize = (10, 7)) 
ax = plt.axes(projection ="3d") 
# Creating plot 
ax.scatter3D(r, g,b,color ="red"); 
plt.title("pixel color distribution") 
plt.xlabel("Red")
plt.ylabel("Green");
#plt.zlabel("Blue");
plt.show()
#choose model type and estimate the parameters (mu and Sigma) from the sample data.
D = 3
X = np.double(df)
mu = numpy.mean(X,axis = 0)
s = df.shape
sigma = np.cov(df,rowvar = 0)
p = np.zeros(s[0])

for n in range(0,s[0]):      
    B = X[n,:]
    SIGMA_inv = np.linalg.inv(sigma)
    denominator = np.sqrt((2 * np.pi)**D * np.linalg.det(sigma))
    exponent = -(1/2) * ((B - mu).T @ SIGMA_inv @ (B - mu ))
    p[n] = float((1. / denominator) * np.exp(exponent) ) 
   
    print (p[n])
    