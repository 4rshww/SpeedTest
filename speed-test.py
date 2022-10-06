#pip install requirements.txt
#https://github.com/4rshww

from errno import WSAEHOSTUNREACH
from time import sleep
from unittest import result
import sys
from pydoc import cli
import speedtest
import os


#os module
os.system('cls')
os.system('title SpeedTest by Arshww')
os.system('color a')


st=speedtest.Speedtest()

option =int(input('''
░██████╗██████╗░███████╗███████╗██████╗░  ████████╗███████╗░██████╗████████╗
██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗  ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
╚█████╗░██████╔╝█████╗░░█████╗░░██║░░██║  ░░░██║░░░█████╗░░╚█████╗░░░░██║░░░
░╚═══██╗██╔═══╝░██╔══╝░░██╔══╝░░██║░░██║  ░░░██║░░░██╔══╝░░░╚═══██╗░░░██║░░░
██████╔╝██║░░░░░███████╗███████╗██████╔╝  ░░░██║░░░███████╗██████╔╝░░░██║░░░
╚═════╝░╚═╝░░░░░╚══════╝╚══════╝╚═════╝░  ░░░╚═╝░░░╚══════╝╚═════╝░░░░╚═╝░░░
    ᴡʜᴀᴛ sᴘᴇᴇᴅ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴛᴇsᴛ:
1) download speed
2) upload speed
your choice: '''))



if option == 1:
    for x in range(10):
        os.system('title getting download speed.')
        sleep(0.5)
        os.system('title getting download speed..')
        sleep(0.5)
        os.system('title getting download speed...')
        sleep(0.5)
    e = (st.download()/(1025*1025))
    print(f'{e} MB')
    os.system(f'title your download speed is {e} MB')
    input('press enter to exit: ')
    exit()

if option == 2:
        for x in range(10):
            os.system('title getting upload speed.')
            sleep(0.5)
            os.system('title getting upload speed..')
            sleep(0.5)
            os.system('title getting upload speed...')
            sleep(0.5)
        up1 = (st.upload()/(1025*1025))
        print(f'{up1} MB')
        os.system(f'title your upload speed is {up1} MB')
        input('press enter to exit: ')
        exit()


else:
    print("please enter the correct option")
