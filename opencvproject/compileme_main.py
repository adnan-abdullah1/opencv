from tkinter import *
import os
import abc 
import tkinter as messagebox

root=Tk()
root.title("Welcome to the project")
root.geometry("700x450")
root.configure(background="powder blue")
label=Label(root,text='Python!',fg='green',bg='powder blue',font=(100,100),height=0,width=30)
label.pack(side=TOP)
root1=Frame(root,bg='powder blue')

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

def exit1():
    exit()
   # root.destroy



btn1=Button(root1,text="Original image",fg="red",command=Ab, width=25,height=2)
btn1.grid(row=0,column=0,pady=10,padx=40)

btn2=Button(root1,text="Binary image",fg="red",command=Ac,width=25,height=2)
btn2.grid(row=1,column=0,pady=10,padx=40)

btn3=Button(root1,text="Extract RGB",fg="red",command=Ad,width=25,height=2)
btn3.grid(row=2,column=0,pady=10,padx=40)
btn4=Button(root1,text="Translation",fg="red",command=Ae,width=25,height=2)
btn4.grid(row=3,column=0,pady=10,padx=40)

btn5=Button(root1,text="gray_Scale",fg="red",command=Af,width=25,height=2)
btn5.grid(row=4,column=0,pady=10,padx=40)

btn6=Button(root1,text="Hsv",fg="red",command=Ag,width=25,height=2)
btn6.grid(row=5,column=0,pady=10,padx=40)
btn7=Button(root1,text="Airthmetic",fg="red",command=Af,width=25,height=2)

btn7.grid(row=0,column=1,pady=10,padx=40)
btn8=Button(root1,text="Blur",fg="red",command=Ag,width=25,height=2)
btn8.grid(row=1,column=1,pady=10,padx=40)
btn9=Button(root1,text="Smooth",fg="red",command=Ah,width=25,height=2)
btn9.grid(row=2,column=1,pady=10,padx=40)

btn10=Button(root1,text="Transpose",fg="red",command=Ai,width=25,height=2)
btn10.grid(row=3,column=1,pady=10,padx=40)


btn11=Button(root1,text="Pyramid",fg="red",command=Aj,width=25,height=2)
btn11.grid(row=4,column=1,pady=10,padx=40)

btn12=Button(root1,text="Crop",fg="red",command=Ak,width=25,height=2)
btn12.grid(row=5,column=1,pady=10,padx=100)

btn13=Button(root1,text="Exit",fg="black",bg="red",command=exit1,width=25,height=2)
btn13.grid(row=6,column=4,pady=10,padx=40)


root1.pack(side=BOTTOM)
root.mainloop()




