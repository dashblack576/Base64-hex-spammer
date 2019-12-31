#! /usr/bin/local/python3/

import base64
import time 
import binascii
import os

target_str = input("Enter the thing that you want to be encoded\n>>>")
how_many = int(input("How many times do you want your string to be encoded?\n>>>"))


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

while not x==how_many: 
    convert_to_64()
    convert_to_hex()
    x += 1

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
    time_until_conv += 1

    if time_until_conv ==5:
        final()
        wait = False
    else:
        wait = True










































