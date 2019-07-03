# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 19:13:44 2019

@author: ogs19
"""
import cv2
import numpy as np

def process_image_erosion(filename, name):
    img = cv2.imread(filename)
    
    kernel = np.ones((3,3),np.uint8)
    #kernel_2 = np.ones((5,5),np.uint8)
    #dilation = cv2.dilate(img,kernel,iterations = 1)
    erosion = cv2.erode(img,kernel,iterations = 1)
    path = 'C:\\wamp64\\www\\Images_Storage\\Crop_Output\\' + name
    print(path)
    cv2.imwrite(path,erosion)
    
def process_image_dilation(filename, name):
    img = cv2.imread(filename)
    
    kernel = np.ones((2,2),np.uint8)
    #kernel_2 = np.ones((5,5),np.uint8)
    dilation = cv2.dilate(img,kernel,iterations = 1)
    #erosion = cv2.erode(img,kernel,iterations = 1)
    path = 'C:\\wamp64\\www\\Images_Storage\\Crop_Output\\' + name
    print(path)
    cv2.imwrite(path,dilation)