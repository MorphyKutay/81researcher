#!/usr/bin/python3
from pathlib import Path
import re
import glob
import os
from tabulate import tabulate

x = input("taranacak klasorun tam yolu : ")

ff = "echo 'SQLİ ola bilir buraya dikkat edin' "
ll = "echo 'bir password unutulmuş ola bilir buraya dikkat edin' "
kk = "echo 'bir key unutulmuş ola bilir buraya dikkat eidn ' " 
vv = "echo 'Insertion of Sensitive Information into Log File '"
cry = "echo 'Identifying Insecure and/or Deprecated Cryptographic Algorithms' " 
ex = "echo 'External Storage Zafiyeti ola bilir' "
#os.chdir(x)
#for file in glob.glob("*.java"):
 #   print(file)

import os
  
# Folder Path
path = x
  
# Change the directory
os.chdir(path)
  
# Read text File
  
  
def read_text_file(file_path):
    with open(file_path, 'r') as f:
        #print(f.read())
        print("-"*30)
        os.system("grep -Hi password "+file_path+ " && "+ll)
        os.system("grep -Hi SQLiteDatabase "+file_path+" && "+ff)    
        os.system("grep -Hi key "+file_path+" && "+kk)    
        os.system("grep -Hi Access_Key "+file_path+" && "+kk)    
        os.system("grep -Hi Access_Token "+file_path+" && "+kk)        
        os.system("grep -Hi sql "+file_path+" && "+ff)        
        os.system("grep -Hi db.rawQuery "+file_path+" && "+ff)        
        os.system("grep -Hi Cursor "+file_path+" && "+ff)        
        os.system("grep -Hi localUserSecretStore "+file_path+" && "+vv)        
        os.system("grep -Hi myCompositeKey "+file_path+" && "+vv)        
        os.system("grep -Hi MD5 "+file_path+" && "+cry)
        os.system("grep -Hi MD4 "+file_path+" && "+cry)
        os.system("grep -Hi SHA1 "+file_path+" && "+cry)
        os.system("grep -Hi Environment.getExternalFilesDir "+file_path+" && "+cry)


# iterate through all file
for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".java"):
        file_path = f"{path}/{file}"
  
        # call read text file function
        read_text_file(file_path)

print("-"*30)
#os.system("grep -i pass "+file_path)
