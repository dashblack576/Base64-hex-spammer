#! /usr/bin/local/python3/

import base64
import time 
import binascii
import os



target_str = input("Enter the thing that you want to be encoded\n>>>")
how_many = int(input("How many times do you want your string to be encoded? The more encodes you do the longer it will take to encode. This may take a while.\n>>>"))


def convert_to_64():
    global target_str
    target_str = target_str.encode()
    target_str = base64.b64encode(target_str)
    target_str = target_str.decode()

def convert_to_hex():
    global target_str
    target_str = target_str.encode()
    target_str = binascii.hexlify(target_str)
    target_str = target_str.decode()

def final():
    global target_str
    print(target_str)

wait = True
time_until_conv = 0
x = 0

while wait ==True:
    os.system('clear')
    print("loading")
    time.sleep(1)
    os.system('clear')
    print("loading.")
    time.sleep(1)
    os.system('clear')
    print("loading..")
    time.sleep(1)
    os.system('clear')
    print("loading...")
    time.sleep(1)
    os.system('clear')
    convert_to_64()
    convert_to_hex()
    time_until_conv += 1

    if time_until_conv ==how_many:
        final()
        wait = False
    else:
        wait = True


def base64_decode():
    global easy
    easy = easy.encode()
    easy = base64.b64decode(easy)
    easy = easy.decode()
 
 def hex_decode():
    global easy
    easy = easy.encode()
    easy = binascii.unhexlify(easy)
    easy = easy.decode()
 
def final():
    global easy
    print(easy)




wait2 = True

while wait 2 ==True 

decode? = input("Time to decode! If you don't want to just hit enter.")

if decode? =="":
    wait2 = False

else









































