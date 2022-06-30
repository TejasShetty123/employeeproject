from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os

class Employlee_Menu:
    def __init__(self,root):
        self.root=root
        root.geometry("1550x800")
        root.title("Employee Management System")

        img=Image.open("/images/OIP.jpg")
        img=img.resize((1550,800),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(img)

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="white")
        frame.place(x=280,y=120,width=750,height=500)

        str=Label(frame, text="Employee Menu", font=("times new roman", 20, "bold"),fg="white", bg="black")
        str.place(x=280,y=20)

      
        

        self.Photo_Update=PhotoImage(file=r"images/editicon.png")
        self.Photo_Update=self.Photo_Update.subsample(5,5)

        self.Update_btn=Button(frame,text="Update",bd=0, bg='white', image=self.Photo_Update,compound=TOP,command=lambda:self.EmployeeFunction(root))
        self.Update_btn.place(width= 150, height=120, x= 120, y=100)

        self.photo_View = PhotoImage(file=r"images/editicon.png")
        self.photo_View = self.photo_View.subsample(5, 5)

        self.View_btn = Button(frame, text='View', bd=0, bg='white', image=self.photo_View,
                               compound=TOP) 
        self.View_btn.place(width= 150, height=120, x= 420, y=100)



        self.photo_Leave = PhotoImage(file=r"images/attendance.png")
        self.photo_Leave = self.photo_Leave.subsample(5, 5)

        self.Leave_btn = Button(frame, text='Apply Leave', bd=0, bg='white', image=self.photo_Leave,
                               compound=TOP) 
        self.Leave_btn.place(width= 150, height=120, x= 120, y=300)




        self.photo_exit = PhotoImage(file=r"Images/exit.png")
        self.photo_exit = self.photo_exit.subsample(5, 5)

        self.Exit_btn = Button(frame, text='Exit', bd=0, bg='white', image=self.photo_exit,
                               compound=TOP,command=lambda:self.ExitFunction(root)) 
        self.Exit_btn.place(width= 150, height=120, x= 420, y=300)

    def ExitFunction(self,root):
        root.withdraw()
        os.system("py .\Homepage.py")
        root.deiconify()

    def EmployeeFunction(self,root):
        root.withdraw()
        os.system("py .\EmployeeDesign.py")
        root.deiconify()










root=Tk()
menu=Employlee_Menu(root)
root.mainloop()

  
