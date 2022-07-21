__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

from functools import cache
import os
import zipfile
from pathlib import Path



#part1 
def clean_cache(): 
    path = '/Users/linah/Winc/files/cache'
    dir=os.path.exists(path)
    if not dir: #if path doesn't exist create folder cache
        os.mkdir(path)
    else: #if path does exist remove files in folder cache
        for files in os.listdir(path):
            new_path = path+"/"+files
            if os.path.isfile(new_path):
                print("Deleting file:", new_path)
                os.remove(new_path)
    return 'cache folder is created and empty'
            
#print(clean_cache())

#part2 #import zipfile module
def cache_zip(zip_file_path,dir_path):
    file = '/Users/linah/Winc/files/data.zip'
    zip_obj=zipfile.ZipFile(file,"r")#question: why first create zip_object if it is already a zip object?
    zip_obj.extractall('/Users/linah/Winc/files/cache') 
    return 'zip file is unpacked'

zip = '/Users/linah/Winc/files/data.zip'
dir = '/Users/linah/Winc/files/cache'
#print(cache_zip(zip,dir))

#part3 #obtain absolute path cache folder, irrespective of os 
#return list of all files in cache 
def cached_files():
    abs_path = os.path.abspath('/Users/linah/Winc/files/cache')
    list_cached_files = []
    for path in os.listdir(abs_path):
        add_path =os.path.join(abs_path,path)
        list_cached_files.append(add_path)
    return list_cached_files

#print(cached_files())
#question: outcome should be list of all file paths? instead of list of all file names? 

#part4 
def find_password(list):
    for textfile in list:
        file = open(textfile,'r')
        lines=file.readlines()
        for item in lines:
            item_into_list = item.split("\n")
            for detail in item_into_list: 
                if "password" in detail: 
                    return detail[detail.find(" ")+1:]
                    #alternative return detail[10:40]#question how to best only return password itself?                     

print(find_password(cached_files()))


     

