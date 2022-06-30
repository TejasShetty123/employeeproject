from tkinter import * 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os
import mysql.connector
from mysql.connector import Error



class Loginadmin_Window():
  def __init__(self,root):
    self.root=root
    self.root.title("Login")
    self.root.geometry("1550x800")
  
    img=Image.open(r"./images/bg6.jpg")
    img=img.resize((1550,800),Image.ANTIALIAS)
    self.bg=ImageTk.PhotoImage(img)

    lbl_bg=Label(self.root,image=self.bg)
    lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)


    btnback=Button(root,text="Back",font=("times new roman", 10, "bold"),relief=RIDGE,fg="white",bg="black",command=lambda:self.BackFunction(root))
    btnback.place(x=5,y=5,width=70,height=40)


    frame=Frame(self.root,bg="black")
    frame.place(x=540,y=170,width=360,height=450)

    img1=Image.open(r"./images/login.jpg ")
    img1=img1.resize((100, 100), Image.ANTIALIAS)
    self.photoimage1=ImageTk.PhotoImage(img1)
    lblimg1=Label(image = self.photoimage1, bg="black", borderwidth=0)
    lblimg1.place(x=660,y=175, width=100, height=100)


    str=Label(frame, text="Admin/Employee", font=("times new roman", 20, "bold"),fg="white", bg="black")
    str.place(x=125,y=100)

      #label------------------
    username_lbl=Label(frame, text="Username", font=("times new roman", 15,"bold"), fg="white", bg="black")
    username_lbl.place(x=70,y=155)
    self.txtuser=ttk.Entry(frame, font= ("times new roman",15,"bold"))
    self.txtuser.place(x=40,y= 180, width=270)

    password_lbl=Label(frame, text="Password", font=("times new roman", 15,"bold"),fg="white",bg="black")
    password_lbl.place(x=70, y=225)

    self.txtpass=ttk.Entry(frame, font=("times new roman", 15,"bold"),show='*')
    self.txtpass.place(x=40, y=250, width=270)

    

  
    check_button=Checkbutton(frame,text="show password",command=self.show_password)
    check_button.place(x=40,y=290)




    #icon image------------
    img2=Image.open(r"./images/username_icon.png ")
    img2=img2.resize((25,25), Image.ANTIALIAS)
    self.photoimage2=ImageTk.PhotoImage(img2)
    lblimg1=Label(image = self.photoimage2, bg="black", borderwidth=0)
    lblimg1.place(x=580,y=323, width=25, height=25)

    img3=Image.open(r"./images/password_icon.png ")
    img3=img3.resize((25, 25), Image.ANTIALIAS)
    self.photoimage3=ImageTk.PhotoImage(img3)
    lblimg1=Label(image = self.photoimage3, bg="black", borderwidth=0)
    lblimg1.place(x=580,y=393, width=25, height=25)

   
    
   




    #Login button
    loginbtn=Button(frame,text="Login",font=("times new roman", 20, "bold"),command=self.login,bd=3,relief=RIDGE,fg="white",bg="red",activebackground="red",activeforeground="black")
    loginbtn.place(x=110,y=350,width=120,height=55)


  def BackFunction(self,root):
    root.withdraw()
    os.system("py .\Homepage.py")
    root.deiconify()

  

  def login(self):
    if self.txtuser.get()=="" or self.txtpass.get()=="":
      messagebox.showerror("Error","all fields are required")
    else:
      try:
        con=mysql.connector.connect(host='localhost',database='employee management',user='Employee',password='employeemanagement')
        cur=con.cursor()
        cur.execute("Select * from tblLogin where Username='"+self.txtuser.get()+"' and password="+ self.txtpass.get())
        row=cur.fetchall()
        print(row)
        if row==[]:
          messagebox.showerror("Invalid","invalid username and password")
        else:
          messagebox.showinfo("Success","login successfully")
          self.root.destroy()
          import AdminMenu
        con.close()
      except Exception as es:
         messagebox.showerror("Error",f"Error due to: {str(es)}")

  def show_password(self):
    if self.txtpass.cget('show') == '*':
      self.txtpass.config(show='')
    else:
      self.txtpass.config(show='*')
     
  
   
    


        


root=Tk()
a= Loginadmin_Window(root)
root.mainloop()




    


