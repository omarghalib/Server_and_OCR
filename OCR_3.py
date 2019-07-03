# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 17:56:33 2019

@author: ogs19
"""

from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
def OCR_Nums(filename):
    text = pytesseract.image_to_string(Image.open(filename), lang='ara_number')
    print("OCR_nums:")
    print(text)
    return(text)