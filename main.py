import os
import sys

def banner():
    print('''
    
 █████╗  ██╗                                                                    
██╔══██╗███║                                                                    
╚█████╔╝╚██║                                                                    
██╔══██╗ ██║                                                                    
╚█████╔╝ ██║                                                                    
 ╚════╝  ╚═╝                                                                    
                                                                                
██████╗ ███████╗███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗███████╗██████╗ 
██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗
██████╔╝█████╗  ███████╗█████╗  ███████║██████╔╝██║     ███████║█████╗  ██████╔╝
██╔══██╗██╔══╝  ╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║██╔══╝  ██╔══██╗
██║  ██║███████╗███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║███████╗██║  ██║
╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                
    
    ''')


banner()
x = input("apk decompiler edlsin mi [y/n/d]  : ")

if x == "y":
    os.system("clear")
    os.system("python3 decompiler/main.py")

if x == "n":
    print("çıkılıyor...")
    sys.exit()
elif x == "d":
    komut = input("AndroidManifest.xml dosyasındaki hardcoded değerleri taramak istiyor musunuz [y/n] :  ")
    if komut == "y":
        os.system("python3 androidxml.py")
    elif komut == "n":
        os.system("python3 scan.py")
