

import time, os, re, urllib
import msvcrt
import sys      
import serial   
from datetime import datetime


PORT="COM3"   
TARGET="D:\.spyder-py3\DeepSARA-master\sample.text"

sendvalue=0
prevsendvalue=0

def kbfunc():
    
    if x:
        ret = ord(msvcrt.getch())
    else:
        ret = 0
    return ret

# Program specific function

def txtfilequery(FILE,QUERY):
    # Search a text file for the query and return the value
    txtfile=open(FILE,"r")
    text=txtfile.read()
    txtfile.close()
    index = text.find(QUERY)
    querylength= len(QUERY)
    querytarget= text[index+querylength:]

    return querytarget    

# Program specific function

def textmcu(sendvalue):
    
    
    ser.write(sendvalue)
    time.sleep(2)
    
# Start communication with Arduino
print ("Starting serial port communications")
ser = serial.Serial(PORT, 2400)
time.sleep(3)


sendvalue=0
prevsendvalue=0
while 1==1:
    sendvalue=int(txtfilequery(TARGET,""))
    print (" Sent value is ") % sendvalue
    if sendvalue!=prevsendvalue:
        commandarduino(sendvalue)
    prevsendvalue=sendvalue
    sleepiter=0
    while sleepiter<1:
        time.sleep(1)
        X=kbfunc()  
        if X==122:
            sys.exit()
        sleepiter=sleepiter+1
    