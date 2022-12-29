from tkinter import *
import shutil
from PIL import ImageTk,Image
import sqlite3
from tkinter import filedialog
import tkinter.messagebox as tmsg
from subprocess import call


def register():
    call(["python", "registerGUI.py"])
def VideoSurveillance():
    call(["python", "surveillance.py"])
def detectCriminal():
    call(["python", "detect.py"])


root = Tk()
root.geometry('1350x720')
root.minsize(1350,720)
root.state("zoomed")
root.title("CFIS- Criminal Face Identification System")
root.configure(bg="#7AC5CD")


Fullname=StringVar()
father=StringVar()
var = IntVar()
c=StringVar()
d=StringVar()
var1= IntVar()
file1=""
image=Image.open("home.png")
photo=ImageTk.PhotoImage(image)
photo_label=Label(image=photo,width=1550,height=220,bg='white').place(x=0,y=0)
photo_label

label_0 = Label(root, text="CRIMINAL FACE IDENTIFICATION SYSTEM",width=38,font=("Times New Roman", 40),anchor=CENTER,bg="#FF4500",fg="white")
label_0.place(x=200,y=300)

Button(root, text='REGISTER CRIMINAL',width=35,height=3,bg='blue',fg='white',font=("bold", 15),command=register).place(x=600,y=400)
Button(root, text='PHOTO MATCH',width=35,height=3,bg='blue',fg='white',font=("bold", 15),command=detectCriminal).place(x=600,y=500)
Button(root, text='VIDEO SURVEILLANCE',width=35,height=3,bg='red',fg='white',font=("bold", 15),command=VideoSurveillance).place(x=600,y=600)
