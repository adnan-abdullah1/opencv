from tkinter import *
from tkinter import messagebox

import os
import abc 


root=Tk()
root.title("Welcome to the project")
root.geometry("700x450")
root.configure(background="purple")
label=Label(root,text='Image Manipulation',fg='green',bg='purple',font=(100,100),height=0,width=30)
label.pack(side=TOP)
root1=Frame(root,bg='purple')

def Ab():
    os.system('python3 A1.py')
def Ac():
    os.system('python3 A2.py')
def Ad():
    os.system('python3 A3.py')
def Ae():
    os.system('python3 A4.py')
def Af():
    os.system('python3 A5.py')
def Ag():
    os.system('python3 A6.py')
def Ah():
    os.system('python3 A7.py')
def An():
    root11.destroy
    exit()
def Ai():
    os.system('python3 A12.py')

def Aj():
    os.system('python3 A8.py')
def Ak():
    os.system('python3 A9.py')
def Al():
    os.system('python3 A10.py')
def Am():
    os.system('python3 A11.py')
def Ao():
    os.system('python3 A13.py')
def Ap():
    os.system('python3 A14.py')
def Aq():
   os.system('python3 A15.py')  
   
def Ar():
   from PIL import Image
   import pytesseract
   import cv2
   img=cv2.imread("/root/Desktop/nielit/gitopencv/opencv/opencvproject/img/a1.jpg")
   cv2.imshow('output image',img)
   cv2.waitKey(0)
        
   cv2.destroyAllWindows()
       
   
        #location=input("enter location and image name ")
   im=Image.open("/root/Desktop/nielit/gitopencv/opencv/opencvproject/img/a1.jpg")
   text=pytesseract.image_to_string(im,lang='eng')
   print(text)
  
   messagebox.showinfo('text from image',text)
   cv2.waitKey(0)
        
   cv2.destroyAllWindows()
        

def exit1():
    exit()
   



btn1=Button(root1,text="Original image",fg="red2",command=Ab, width=25,height=2) #ok
btn1.grid(row=0,column=0,pady=10,padx=40)

btn2=Button(root1,text="Binary image",fg="red",command=Ac,width=25,height=2) #ok
btn2.grid(row=1,column=0,pady=10,padx=40)

btn3=Button(root1,text="Extract RGB",fg="red",command=Ad,width=25,height=2) #ok
btn3.grid(row=2,column=0,pady=10,padx=40)
btn4=Button(root1,text="Translation",fg="red",command=Ae,width=25,height=2) #ok
btn4.grid(row=3,column=0,pady=10,padx=40)

btn5=Button(root1,text="gray_Scale",fg="red",command=Af,width=25,height=2)  #ok
btn5.grid(row=4,column=0,pady=10,padx=40)

btn6=Button(root1,text="Hsv",fg="red",command=Ag,width=25,height=2)   #ok
btn6.grid(row=5,column=0,pady=10,padx=40)

btn9=Button(root1,text="Airthmetic",fg="red",command=Ah,width=25,height=2) #ok
btn9.grid(row=2,column=1,pady=10,padx=40)

btn10=Button(root1,text="Blur",fg="red",command=Ai,width=25,height=2) #ok
btn10.grid(row=3,column=1,pady=10,padx=40)


btn11=Button(root1,text="Smooth",fg="red",command=Aj,width=25,height=2) #ok
btn11.grid(row=4,column=1,pady=10,padx=40)

btn12=Button(root1,text="Transpose",fg="red",command=Ak,width=25,height=2) #ok
btn12.grid(row=5,column=1,pady=10,padx=100)

btn14=Button(root1,text="Pyramid",fg="red",command=Al,width=25,height=2) #ok
btn14.grid(row=5,column=1,pady=10,padx=100)


btn15=Button(root1,text="Crop",fg="red",command=Am,width=25,height=2) #ok
btn15.grid(row=5,column=1,pady=10,padx=100)

btn16=Button(root1,text="Negative",fg="red",command=Ao,width=25,height=2) #ok
btn16.grid(row=0,column=1,pady=10,padx=100)

btn17=Button(root1,text="Log",fg="red",command=Ap,width=25,height=2) #ok
btn17.grid(row=1,column=1,pady=10,padx=100)


btn13=Button(root1,text="Exit",fg="black",bg="red",command=exit1,width=25,height=2)
btn13.grid(row=6,column=4,pady=10,padx=40)


btn19=Button(root1,text="Ocr",fg="red",command=Ar,width=25,height=2)
btn19.grid(row=1,column=2,pady=10,padx=40)


btn18=Button(root1,text="Edge_Detect",fg="red",command= Aq  ,width=25,height=2)
btn18.grid(row=0,column=2,pady=10,padx=40)


root1.pack(side=BOTTOM)
root.mainloop()




