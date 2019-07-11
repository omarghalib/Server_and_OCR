# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 01:18:53 2019

@author: ogs19
"""
from OCR_Upload_Python import *
from OCR_3 import *
from cloud_mysql_python import *
#from mysql_python import *
from Image_Processing import *
from Image_Processing_others import *
from Crop_Image import *

def Turn_to_rec(image) :
    file_path_name = 'C:\\wamp64\\www\\Images_Storage\\Crop_Output\\cropped_Name.jpg'
    file_path_add = 'C:\\wamp64\\www\\Images_Storage\\Crop_Output\\cropped_Add.jpg'
    file_path_num = 'C:\\wamp64\\www\\Images_Storage\\Crop_Output\\cropped_N.jpg'
    Processed_num = "C:\\wamp64\\www\\Images_Storage\\Crop_Output\\P_num.png"
    Processed_name = "C:\\wamp64\\www\\Images_Storage\\Crop_Output\\P_name.png"
    Processed_name_2 = "C:\\wamp64\\www\\Images_Storage\\Crop_Output\\P_name_2.png"
    Processed_name_3 = "C:\\wamp64\\www\\Images_Storage\\Crop_Output\\P_name_3.png"
    crop(image, (0, 0, 554, 133), file_path_name)
    crop(image, (0, 133, 554, 250), file_path_add)
    crop(image, (0, 261, 554, 380), file_path_num)
    print("Done Cropping")
    process_image(file_path_num,'P_num.png')
    process_image_erosion(file_path_name,'P_name.png')
    process_image_dilation(file_path_name,'P_name_2.png')
    process_image(file_path_name,'P_name_3.png')
    not_done = False
    if not not_done :
        not_done = True
        i = 1
        while not_done and i < 4 :
            not_done, n1,n2 = OCR_Req_name(Processed_name)
            name_1 = n1 + n2
            print("with erosion:" + name_1)
            i += 1
            
    if not not_done :
        not_done = True    
        i = 1
        while not_done and i < 4 :
            not_done, n1,n2 = OCR_Req_name(file_path_name)
            name_2 = n1 + n2
            print("without I.P:" + name_2)
            i += 1
                
    if not not_done :
        not_done = True    
        i = 1
        while not_done and i < 4 :
            not_done, n1,n2 = OCR_Req_name(Processed_name_3)
            name_3 = n1 + n2
            print("with blurring:" + name_3)
            i += 1
        
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

        num_OCR = OCR_Nums(Processed_num)
        print(type(num_OCR))
        print(num_OCR)
        num_OCR = num_OCR.replace(" ", "")
        print(num_OCR)
        num_OCR_int = int(num_OCR)
        print(num_OCR_int)
            
    if not not_done :
        not_done = True    
        i = 1
        while not_done and i < 4 :
            not_done, add1,add2 = OCR_Req_add(file_path_add)
            add = add1 + add2
            print(add)
            i += 1
            
    if not not_done :
        not_done = True    
        i = 1
        while not_done and i < 4 :    
            try:
                cloud_insertPythonVaribleInTable(name, num_OCR_int,add, image )
                #insertPythonVaribleInTable(name, num_OCR_int,add, image )
                not_done = False
            except:
                print("Error inserting the record" + i)
                i += 1
    if not_done :
        print("Not done! record saved for next iteration")
        return False        
    else:
        print("Done, record deleted from local DB")
        return True
    
