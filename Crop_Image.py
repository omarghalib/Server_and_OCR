# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 18:01:58 2019

@author: ogs19
"""

from PIL import Image

 
def crop(image_path, coords, saved_location):
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    width, height = image_obj.size
    #print(width)
    #print(height)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)
    #cropped_image.show()
    
 
#if __name__ == '__main__':
#    image = 'a08a6e8f-1d84-4ddc-99a1-312a4e140ed0.png'
#    crop(image, (161, 166, 300, 400), 'cropped.jpg')