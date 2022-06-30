from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class EmpLeave:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Employee management system")

        lbl_title=Label(self.root,text='EMPLOYEE MANAGEMENT SYSTEM',font=('times new roman',37,'bold'),fg='blue',bg='white')
        lbl_title.place(x=0,y=0,width=1500, height=50)


        btnback=Button(root,text="Back",font=("times new roman", 10, "bold"),relief=RIDGE,fg="white",bg="black",command=lambda:self.BackFunction(root))
        btnback.place(x=5,y=5,width=70,height=40)

        img1=Image.open(r"./images/login.jpg ")
        img1=img1.resize((50, 50), Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image = self.photoimage1, bg="white", borderwidth=0)
        lblimg1.place(x=210,y=0, width=100, height=50)

        img_frame=Frame(self.root,bg="blue")
        img_frame.place(x=0,y=55,width=1380,height=250)
        
        leave_frame=Frame(self.root,bg="white")
        leave_frame.place(x=0,y=300,width=1380,height=400)

        #empid
        lbl_EmpId=Label(leave_frame,text="Emp Id",font=('arial','11','bold',),bg='white' )
        lbl_EmpId.grid(row=0,column=0,padx=2,sticky=W,pady=5)

        txt_EmpId=ttk.Entry(leave_frame,width=22,font=('arial','11','bold'),)
        txt_EmpId.grid(row=0,column=1,sticky=W,padx=5,pady=5)

        #leave type
        lbl_leavetype=Label(leave_frame,text="Leavetype",font=('arial','11','bold',),bg='white' )
        lbl_leavetype.grid(row=1,column=0,padx=2,sticky=W,pady=5)

        combo_leavetype=ttk.Combobox(leave_frame,font=('arial','11','bold'),width=20,state="readonly")
        combo_leavetype[ 'value']=('Select','CL')
        combo_leavetype.current()
        combo_leavetype.grid(row=1, column=1, padx=2, pady=5, sticky=W)

         #no of days
        lbl_No_of_days=Label(leave_frame,text="No_Of_Days",font=('arial','11','bold',),bg='white' )
        lbl_No_of_days.grid(row=2,column=0,padx=2,sticky=W,pady=5)

        txt_No_of_days=ttk.Entry(leave_frame,width=22,font=('arial','11','bold'),)
        txt_No_of_days.grid(row=2,column=1,sticky=W,padx=5,pady=5)

         #leave available
        lbl_leaveavailable=Label(leave_frame,text="Leave Available",font=('arial','11','bold',),bg='white' )
        lbl_leaveavailable.grid(row=3,column=0,padx=2,sticky=W,pady=5)

        txt_leaveavailable=ttk.Entry(leave_frame,width=22,font=('arial','11','bold'),)
        txt_leaveavailable.grid(row=3,column=1,sticky=W,padx=5,pady=5)

         #leave reason
        lbl_leavereason=Label(leave_frame,text="Leave Reason",font=('arial','11','bold',),bg='white' )
        lbl_leavereason.grid(row=0,column=2,padx=2,sticky=W,pady=5)

        combo_leavereason=ttk.Combobox(leave_frame,font=('arial','11','bold'),width=20,state="readonly")
        combo_leavereason[ 'value']=('Select','Relatives Wedding','not feeling well')
        combo_leavereason.current()
        combo_leavereason.grid(row=0, column=3, padx=2, pady=5, sticky=W)

         #leave available
        lbl_applied_on=Label(leave_frame,text="Applied On",font=('arial','11','bold',),bg='white' )
        lbl_applied_on.grid(row=1,column=2,padx=2,sticky=W,pady=5)

        txt_applied_on=ttk.Entry(leave_frame,width=22,font=('arial','11','bold'),)
        txt_applied_on.grid(row=1,column=3,sticky=W,padx=5,pady=5)

        #leave from
        lbl_leave_from=Label(leave_frame,text="Leave From",font=('arial','11','bold',),bg='white' )
        lbl_leave_from.grid(row=2,column=2,padx=2,sticky=W,pady=5)

        txt_leave_from=ttk.Entry(leave_frame,width=22,font=('arial','11','bold'),)
        txt_leave_from.grid(row=2,column=3,sticky=W,padx=5,pady=5)

          #leave To
        lbl_leave_to=Label(leave_frame,text="Leave To",font=('arial','11','bold',),bg='white' )
        lbl_leave_to.grid(row=3,column=2,padx=2,sticky=W,pady=5)

        txt_leave_to=ttk.Entry(leave_frame,width=22,font=('arial','11','bold'),)
        txt_leave_to.grid(row=3,column=3,sticky=W,padx=5,pady=5)

        ####button submit###########
        btnsubmit=Button(leave_frame,text="Submit",font=('times new roman',15,'bold'),width=13,bg='blue',fg='black')
        btnsubmit.grid(row=4,column=1,padx=10,pady=5)




        




















root=Tk()
obj=EmpLeave(root) 
root.mainloop()