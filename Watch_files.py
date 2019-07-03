# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 17:41:47 2019

@author: ogs19
"""

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from subprocess import call
from Crop_Image import *
import requests
import sys
import os
import cgi
import MySQLdb
import cgitb
from OCR_Upload_Python import *
from OCR_3 import *
from cloud_mysql_python import *
from mysql_python import *
from Image_Processing import *
from Image_Processing_others import *
import cv2
import numpy as np
from matplotlib import pyplot as plt

cgitb.enable()
 
class Watcher:
    DIRECTORY_TO_WATCH = "C:\\wamp64\\www\\Images_Storage\\Uploads"
 
    def __init__(self):
        self.observer = Observer()
 
    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(100)
        except:
            self.observer.stop()
            print ("Error")
 
        self.observer.join()
 
 
class Handler(FileSystemEventHandler):
 
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None
 
        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print("File is created")
            print(event.src_path)
            image = event.src_path
            
            file_path_name = 'C:\\wamp64\\www\\Images_Storage\\Crop_Output\\cropped_Name.jpg'
            file_path_add = 'C:\\wamp64\\www\\Images_Storage\\Crop_Output\\cropped_Add.jpg'
            file_path_num = 'C:\\wamp64\\www\\Images_Storage\\Crop_Output\\cropped_N.jpg'
            Processed_num = "C:\\wamp64\\www\\Images_Storage\\Crop_Output\\P_num.png"
            Processed_name = "C:\\wamp64\\www\\Images_Storage\\Crop_Output\\P_name.png"
            Processed_name_2 = "C:\\wamp64\\www\\Images_Storage\\Crop_Output\\P_name_2.png"
            Processed_name_3 = "C:\\wamp64\\www\\Images_Storage\\Crop_Output\\P_name_3.png"
            crop(image, (0, 20, 549, 133), file_path_name)
            crop(image, (0, 133, 549, 250), file_path_add)
            crop(image, (0, 261, 549, 380), file_path_num)
            print("Done Cropping")
            process_image(file_path_num,'P_num.png')
            process_image_erosion(file_path_name,'P_name.png')
            process_image_dilation(file_path_name,'P_name_2.png')
            process_image(file_path_name,'P_name_3.png')
            
            n1,n2 = OCR_Req_name(Processed_name)
            name_1 = n1 + n2
            print("with erosion:" + name_1)
            
            n1,n2 = OCR_Req_name(file_path_name)
            name_2 = n1 + n2
            print("without I.P:" + name_2)
            
            n1,n2 = OCR_Req_name(Processed_name_3)
            name_3 = n1 + n2
            print("with blurring:" + name_3)
            
            
            print( "max:" + max([name_1, name_2, name_3], key=len))
            names = [name_1, name_2, name_3]
            max_name = max(names, key=len)
            if len(max_name) < 40:
                name = max_name
            else: 
                names.remove(max_name)
                if len(max(names, key=len)) < 40 :
                    name = max(names, key=len)
                else:
                    name = min(names, key=len)
            #num_OCR_str = " "
            num_OCR = OCR_Nums(Processed_num)
            #num_OCR_str = num_OCR
            print(type(num_OCR))
            #print(num_OCR_str)
            print(num_OCR)
            num_OCR = num_OCR.replace(" ", "")
            print(num_OCR)
            num_OCR_int = int(num_OCR)
            print(num_OCR_int)
            
            add1,add2 = OCR_Req_add(file_path_add)
            add = add1 + add2
            print(add)
            cloud_insertPythonVaribleInTable(name, num_OCR_int,add, image )
            #insertPythonVaribleInTable(name, num_OCR_int,add, image )
            

if __name__ == '__main__':
    w = Watcher()
    w.run()