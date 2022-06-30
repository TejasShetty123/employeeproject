from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os

class Admin_Menu:
    def __init__(self,root):
        self.root=root
        root.geometry("1550x800")
        root.title("Employee Management System")

        img=Image.open(r"./images/OIP.jpg")
        img=img.resize((1550,800),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(img)

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="white")
        frame.place(x=280,y=120,width=750,height=500)

        str=Label(frame, text="Admin Menu", font=("times new roman", 20, "bold"),fg="white", bg="black")
        str.place(x=280,y=20)

        

        self.Photo_Manageemp=PhotoImage(file=r"images/fees.png")
        self.Photo_Manageemp=self.Photo_Manageemp.subsample(5,5)

        self.Manageemp_btn=Button(frame,text="ManageEmp",bd=0,cursor="hand2",font=("times new roman",15,"bold"),compound=TOP,image=self.Photo_Manageemp,command=lambda:self.AdminFunction(root))
        self.Manageemp_btn.place(x=120,y=100,width=200,height=120)

        self.Photo_Manageleave=PhotoImage(file=r"images/attendance.png")
        self.Photo_Manageleave=self.Photo_Manageleave.subsample(5,5)

        self.Manageleave_btn=Button(frame,text="ManageLeave",bd=0,cursor="hand2",font=("times new roman",15,"bold"),compound=TOP,image=self.Photo_Manageleave)
        self.Manageleave_btn.place(x=420,y=100,width=200,height=120)

        self.Photo_Exit=PhotoImage(file=r"images/exit.png")
        self.PhotoExit=self.Photo_Exit.subsample(5,5)

        self.Exit_btn=Button(frame,text="Exit",bd=0,cursor="hand2",font=("times new roman",15,"bold"),compound=TOP,image=self.PhotoExit,command=lambda:self.ExitFunction(root))
        self.Exit_btn.place(x=280,y=300,width=150,height=120)

         


    def ExitFunction(self,root):
        root.withdraw()
        os.system("py .\Homepage.py")
        root.deiconify()

    def AdminFunction(self,root):
        root.withdraw()
        os.system("py .\AdminDesign.py")
        root.deiconify()

       





root=Tk()
menu=Admin_Menu(root)
root.mainloop()

  
