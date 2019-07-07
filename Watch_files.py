# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 17:41:47 2019

@author: ogs19
"""

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from subprocess import call
import requests
import sys
import os
import cgi
import MySQLdb
import cgitb
import cv2
import numpy as np
from matplotlib import pyplot as plt
from Main_act import *
from mysql_python import *

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
                time.sleep(1)
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
            # Check records when a file is first created.
            print("File is created")
            print(event.src_path)
            check_for_records()

if __name__ == '__main__':
    w = Watcher()
    w.run()