from tkinter import *
from PIL import ImageTk, Image
import os
from tkinter import filedialog
from tkinter import messagebox

root=Tk()
root.minsize(650,650)
root.maxsize(650,650)
root.configure (bg = "cyan")

#open_img = ImageTk.PhotoImage(Image.open("open_file.png"))
#save_img = ImageTk.PhotoImage(Image.open("save_file.png"))
#run_img = ImageTk.PhotoImage(Image.open("run.png"))

label_file_name = Label(root, text="File name")
label_file_name.place(relx=0.28,rely=0.03,anchor= CENTER)

input_file_name = Entry(root)
input_file_name.place(relx=0.46,rely=0.03,anchor= CENTER)

my_text = Text(root,height=35,width=80, bg="slate gray")
my_text.place(relx=0.5,rely=0.55,anchor= CENTER)

root.mainloop()