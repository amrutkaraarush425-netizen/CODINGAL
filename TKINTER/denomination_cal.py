from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Denomination Counter")
root.configure(bg='light blue')
root.geometry("640x400")

upload = Image.open("C:\Users\Aarush\OneDrive\Pictures\01.jpg")
upload = upload.resize((300,300))
Image = ImageTk.PhotoImage("upload")

label = Label(root, image=image, bg="light blue")
label.place(x=180, y=20)

label1= Label(
    root,
    text="Hey User! Welcome to Domination Counter Application."
    bg='light blue'
)
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
   MsgBox = messagebox.showinfo(
       "Alert"
       "Do You Want to Calculate Denomination Count?"
   )
   if MsgBox == "ok":
      topwin()

      button1 = Button(
          root,
          text="Lets get started!"
          command=msg,
          bg="brown",
          fg="white"
      )
      button1.place(x=260, y=360)

def topwin():
top = TopLevel()
top.title("Denomination Calculator")
top.configure(bg="light grey")



