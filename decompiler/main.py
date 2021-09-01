import argparse
import os
import shutil
import zipfile

def banner():
    print('''
    
▄▄▄▄  ▄▄▄ . ▄▄·       • ▌ ▄ ·.  ▄▄▄·▪  ▄▄▌  ▄▄▄ .▄▄▄  
██▪ ██ ▀▄.▀·▐█ ▌▪▪     ·██ ▐███▪▐█ ▄███ ██•  ▀▄.▀·▀▄ █·
▐█· ▐█▌▐▀▀▪▄██ ▄▄ ▄█▀▄ ▐█ ▌▐▌▐█· ██▀·▐█·██▪  ▐▀▀▪▄▐▀▀▄ 
██. ██ ▐█▄▄▌▐███▌▐█▌.▐▌██ ██▌▐█▌▐█▪·•▐█▌▐█▌▐▌▐█▄▄▌▐█•█▌
▀▀▀▀▀•  ▀▀▀ ·▀▀▀  ▀█▄▀▪▀▀  █▪▀▀▀.▀   ▀▀▀.▀▀▀  ▀▀▀ .▀  ▀
    
    
    ''')

banner()
command = input("işletim sisteminiz nedir [windows/linux] :")
if command == "linux":
    os.system("clear")
    banner()
    x = input("apk yolunu giriniz : ")
    #os.system("bash decompiler/modules/apktool/apktool d "+x)
    #os.system("bash decompiler/modules/dex2jar-2.0/d2j-dex2jar.sh "+x)
    os.system("bash decompiler/modules/jadx/bin/jadx -d decompiler/modules "+x)