# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 13:45:40 2019

@author: ogs19
"""

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from datetime import datetime
import MySQLdb
import time
#from __future__ import print_function
def cloud_insertPythonVaribleInTable(name,national_number,address,image_url):
    try:
        name.encode()
    #    national_number.encode()
        address.encode()
        image_url.encode()
        cnx = mysql.connector.connect(host = 'hospital.c8piany8wokr.us-east-2.rds.amazonaws.com' ,user ='Hospital' ,passwd='sbme2019' ,db='Hospital')
        #cnx.set_character_set('utf8')
        cursor = cnx.cursor()
        sql_insert_query = (" INSERT INTO Admission"
                             "(timestamp, name, national_number, address, image_url)" " VALUES (%s,%s,%s,%s,%s)")
        
        datetime = time.strftime("%Y/%m/%d %H:%M:%S")
        insert_tuple = (datetime,name,national_number,address,image_url)
        cursor.execute(sql_insert_query, insert_tuple)
        #result=cursor.fetchall()
        #cnx.commit()
        #conn.close()
        lastR = cursor.lastrowid
        # Make sure data is committed to the database
        cnx.commit()
    
        cursor.close()
        cnx.close()
        print ("Record inserted successfully into python_users table")
        
    except:
        print("error inserting in cloud DB")