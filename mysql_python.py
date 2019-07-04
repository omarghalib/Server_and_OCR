# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 03:21:29 2019

@author: ogs19
"""
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from datetime import datetime
import MySQLdb
import time
from Main_act import *
import socket 
def insertPythonVaribleInTable(name,national_number,address,image_url):
    name.encode()
#    national_number.encode()
    address.encode()
    image_url.encode()
    conn= MySQLdb.connect(host = 'localhost' ,user ='root' ,passwd='' ,db='db_images', port = 3308)
    conn.set_character_set('utf8')
    cursor=conn.cursor()
    sql_insert_query = """ INSERT INTO `ids`
                         (`timestamp`, `name`, `national_number`, `address`, `image_url`) VALUES (%s,%s,%s,%s,%s)"""
    datetime = time.strftime("%Y/%m/%d %H:%M:%S")
    insert_tuple = (datetime,name,national_number,address,image_url)
    cursor.execute(sql_insert_query, insert_tuple)
    result=cursor.fetchall()
    conn.close()
    print ("Record inserted successfully into python_users table")
    
def check_for_records() :
    hostname = socket.gethostname()    
    IPAddr = socket.gethostbyname(hostname)    
    print("Your Computer Name is:" + hostname) 
    print(IPAddr)
    conn= MySQLdb.connect(host = 'localhost' ,user ='root' ,passwd='' ,db='db_images', port = 3308)
    conn.set_character_set('utf8')
    cursor=conn.cursor()
    try:
        mySQLconnection = mysql.connector.connect(host = 'localhost' ,user ='root' ,passwd='' ,db='db_images', port = 3308)
        sql_select_Query = "select url from images"
        cursor = mySQLconnection .cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        print("Total number of rows is - ", cursor.rowcount)
        for img_url in records:
            print(img_url[0])
            print(type(img_url[0]))
            url_path = img_url[0]
            replaced = 'http://' + IPAddr + '/Image_Storage/uploads/'
            url_path = url_path.replace(replaced, 'C:\\wamp64\\www\\Images_Storage\\Uploads\\' )
            print(url_path)
            done = Turn_to_rec(url_path)
            if done :
                #delete this record
                sql_select_Query = "Delete from images where url = %s"
                cursor.execute(sql_select_Query, img_url)
                mySQLconnection.commit()
        cursor.close()
    except Error as e :
        print ("Error while connecting to MySQL", e)
    finally:
        #closing database connection.
        if(mySQLconnection .is_connected()):
            conn.close()
            print("MySQL connection is closed")