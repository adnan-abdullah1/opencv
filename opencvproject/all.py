import numpy as np 
import cv2
import split 
i=1
while i==1:
    print(" \033[1;34;40m ENTER 1 TO READ IMAGE\nENTER 2 TO GET IMAGE INFO \n ENTER 3 TO GET BINARY OF IMAGE \n ENTER 4 TO EXTRACT RGB\nENTER 5 TO DISPACE IMAGE\nENTER 6 TO GET GRAY SCALE\n ENTER 7 TO GET HSV OF IMAGE\nENTER 8 TO ROTATE IMAGE")
    print("\033[1;34;40m Enter 9 to get transpose of image\nEnter 10 to Resize \n Enter 11 to resixe image using pyramid\n Enter 12 to Crop image")
    f=int(input(" enter choice "))
   
    


    if f==1:
        split.read()
    if f==2:
        getinfo()
    if f==3:
        split.binimg()
    if f==4:
        split.rgb()
    if f==5:
        split.dip()
    if f==6:
        split.gray()
    if f==7:
        split.hsv()
    if f==8:
        split.rotate()
    if f==9:
        split.transpose()
    if f==10:
        split.resize()
    if f==11:
        split.pyramid()
    if f==12:
        split.crop()
    i=int(input(" enter 1 if contuniue "))