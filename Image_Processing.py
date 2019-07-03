# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 23:10:16 2019

@author: ogs19
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
def process_image(filename, name):
    img = cv2.imread(filename)
    
    blur = cv2.blur(img,(5,5))
    path = 'C:\\wamp64\\www\\Images_Storage\\Crop_Output\\' + name
    print(path)
    cv2.imwrite(path,blur)