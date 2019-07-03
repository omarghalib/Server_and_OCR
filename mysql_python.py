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
#conn= MySQLdb.connect(host = 'localhost' ,user ='root' ,passwd='' ,db='db_images')
#cursor=conn.cursor()
#cursor.execute("select * from images")
#result=cursor.fetchall()
#cursor.close()
#conn.close()

   # except mysql.connector.Error as error :
    #    connection.rollback()
     #   print("Failed to insert into MySQL table {}".format(error))
    #finally:
     #   #closing database connection.
      #  if(connection.is_connected()):
       #     cursor.close()
        #    connection.close()