#!/usr/bin/python3

import os

#hardocde deger
giris = input("XML dosyanızın adı : ")

ff = "echo 'hardcoded deger bulundu  ' "
print("--"*30)
os.system("grep -i  api "+giris+" && " + ff)
print("--"*30)
os.system("grep -i  pass "+giris+" && " + ff)
print("--"*30)
os.system("grep -i  password "+giris+" && " + ff)
print("--"*30)
os.system("grep -i  key "+giris+" && " + ff)
print("--"*30)
os.system("grep -i  user "+giris+" && " + ff)
print("--"*30)
os.system("grep -i  login "+giris+" && " + ff)
print("--"*30)
os.system("grep -i  register "+giris+" && " + ff)
print("--"*30)
os.system("grep -i  admin "+giris+" && " + ff)
print("--"*30)
os.system("grep -i  hostname "+giris+" && " + ff)
