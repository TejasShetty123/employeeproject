import string
from tkinter import *
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

        # ************variables**********************
       # self.var_fname=String
       
       
       # bg image
        my_bg=Image.open(r"C:\Users\Tejas shetty\Desktop\Project1(Employee management)\img\tree-g1fad11442_1280.jpg")
        resized=my_bg.resize((1550,800),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(resized)
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        # left image
        my_pic=Image.open(r"C:\Users\Tejas shetty\Desktop\Project1(Employee management)\img\Log in\Log in\vector.png")
        resized=my_pic.resize((550,550),Image.ANTIALIAS)
        self.left=ImageTk.PhotoImage(resized)
        bg_lbl=Label(self.root,image=self.left)
        bg_lbl.place(x=120,y=100,width=470,height=550)

        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="blue",bg="white")
        register_lbl.place(x=20,y=20)

        ##############Label and entry#############
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        lname.place(x=370,y=100)

        self.lname_entry=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.lname_entry.place(x=370,y=130,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white")
        email.place(x=50,y=170)

        self.email_entry=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.email_entry.place(x=50,y=200,width=250)

        contact_no=Label(frame,text="Contact_No",font=("times new roman",15,"bold"),bg="white")
        contact_no.place(x=370,y=170)

        self.contact_no_entry=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.contact_no_entry.place(x=370,y=200,width=250)

        security_quection=Label(frame,text="Select Security Quection",font=("times new roman",15,"bold"),bg="white")
        security_quection.place(x=50,y=240)

        self.cmb_security_quection=ttk.Combobox(frame,font=("times new roman",13,"bold"),state="readonly",justify="center")
        self.cmb_security_quection['values']=("Select","Your Birth Place","Your Best Friend Name","Your First Pet Name")
        self.cmb_security_quection.current(0)
        self.cmb_security_quection.place(x=50,y=270,width=250,height=30)
        
        security_answer=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
        security_answer.place(x=370,y=240)

        self.security_answer_entry=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.security_answer_entry.place(x=370,y=270,width=250)

        password=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        password.place(x=50,y=310)

        self.password_entry=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.password_entry.place(x=50,y=350,width=250)

        conf_password=Label(frame,text=" Conform Password",font=("times new roman",15,"bold"),bg="white")
        conf_password.place(x=370,y=310)

        self.conf_password_entry=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.conf_password_entry.place(x=370,y=350,width=250)

        self.var_checkbtn=IntVar()
        checkbtn=Checkbutton(frame,text=" I Agree the terms and condition",variable=self.var_checkbtn,font=("times new roman",15,"bold"),onvalue=1,offvalue=0,bg="white")
        checkbtn.place(x=50,y=400)

        imgreg=Image.open(r"C:\Users\Tejas shetty\Desktop\Project1(Employee management)\img\Log in\Log in\register.png")
        edit=imgreg.resize((200,50),Image.ANTIALIAS)
        self.regphoto=ImageTk.PhotoImage(edit)
        b1=Button(frame,image=self.regphoto,bd=0,cursor="hand2",font=("times new roman",15,"bold"),command=self.register_data)
        b1.place(x=40,y=460,width=200)

        imglog=Image.open(r"C:\Users\Tejas shetty\Desktop\Project1(Employee management)\img\Log in\Log in\register.png")
        edit1=imglog.resize((200,50),Image.ANTIALIAS)
        self.logphoto=ImageTk.PhotoImage(edit1)
        b1=Button(frame,image=self.logphoto,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=360,y=460,width=200)

    ################registration##############
    def register_data(self):
        if self.fname_entry.get()=="" or self.lname_entry.get()=="" or self.email_entry.get()=="" or  self.contact_no_entry.get()=="" or  self.cmb_security_quection.get()=="select" or   self.security_answer_entry.get()=="" or self.password_entry.get()=="" or self.conf_password_entry.get()=="":
            messagebox.showerror("Error","All Field Are Requried")
        elif self.password_entry.get()!=self.conf_password_entry.get():
             messagebox.showerror("Error","Incorrect Password")
        elif self.var_checkbtn.get()==0:
            messagebox.showerror("Error","Please Agree our terms & Condition")
        else:
            try:
                con=mysql.connector.connect(host='localhost',database='employee management',user='Employee',password='employeemanagement')
                cur=con.cursor()
                cur.execute("select * from tblLogin where email=%s",self.email_entry.get())
                row=cur.fetchone()
                if row!=None:
                     messagebox.showerror("Error","User already exit")
                else:
                     cur.execute("insert into tblLogin(fname,lname,email,contact_no,quection,answer,emp_password)values(%s,%s,%s,%s,%s,%s,%s)",(self.fname_entry.get(),
                                         self.lname_entry.get(),
                                         self.email_entry.get(),
                                         self.contact_no_entry.get(),
                                         self.cmb_security_quection.get(),
                                         self.security_answer_entry.get(),
                                         self.password_entry.get()
                                         ))
                     con.commit()
                     con.close()
                     messagebox.showinfo("Success","Register Successfully")
            except Exception as es:
                 messagebox.showerror("Error",f"Error due to:{string(es)}")

           
           
           
           
           
           
           


     
  

























root=Tk()
z=Register(root)
root.mainloop()
