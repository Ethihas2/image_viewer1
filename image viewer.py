from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog
import os

root = Tk()
root.title("Image viewer")
root.geometry("500x600")
root.configure(background="deep sky blue")

img_label = Label(root,bg="CadetBlue1",font=("Candara Light",18,"bold"),highlightthickness=3,borderwidth=1,relief=SOLID)
img_label.place(relx=0.5,rely=0.4,anchor=CENTER)

img_path = ""

def open_img():
    global img_path
    
    img_path = filedialog.askopenfilename(title="Select an Image", filetype=(('image    files','*.jpg'),('all files','*.*')))
    print(img_path)
    img = ImageTk.PhotoImage(Image.open(img_path))
    img_label["image"]=img
    img_path.close()
    
def close_img():
    img_label["image"]=""
    
button_open = Button(root,text="Open Image",command=open_img,bg="CadetBlue1",font=("Comic Sans MS",10))
button_open.place(relx=0.4,rely=0.2,anchor=CENTER)

button_close = Button(root,text="Close Image",command=close_img,bg="CadetBlue1",font=("Comic Sans MS",10))
button_close.place(relx=0.6,rely=0.2,anchor=CENTER)
root.mainloop()