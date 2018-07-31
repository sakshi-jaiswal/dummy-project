from tkinter import Tk,StringVar,ttk
from tkinter import *
from tkinter import messagebox
import time
import datetime
root=Tk()
root.title("attendence management system")
root.geometry('1350x650+0+0')
root.configure(background='black')
LeftMayFrame=Frame(root,width=1000,height=650,bd=8,relief='raised')
LeftMayFrame.pack(side=LEFT)
RightMayFrame=Frame(root,width=350,height=650,bd=8,relief='raised')
RightMayFrame.pack(side=RIGHT)


LeftMayFrame1=Frame(LeftMayFrame,width=1000,height=100,bd=8,relief='raised')
LeftMayFrame1.pack(side=TOP)
LeftMayFrame2=Frame(LeftMayFrame,width=1000,height=550,bd=8,relief='raised')
LeftMayFrame2.pack(side=TOP)


RightMayFrame1=Frame(RightMayFrame,width=350,height=350,bd=8,relief='raised')
RightMayFrame1.pack(side=TOP)
RightMayFrame2=Frame(RightMayFrame,width=1000,height=350,bd=8,relief='raised')
RightMayFrame2.pack(side=TOP)

cont=Canvas(RightMayFrame2,width=350,height=425,bg='black')
cont.grid(row=0,column=0)
image5=PhotoImage(file="images.png")
image=cont.create_image(200,200,image=image5)


cont=Canvas(RightMayFrame1,width=350,height=425,bg='black')
cont.grid(row=0,column=0)
image1=PhotoImage(file="25.png")
##image=cont.create_image(200,200,image=image1)

def pic1():
    image=cont.create_image(200,200,image=image1)
image2=PhotoImage(file="22.png")
def pic2():
    image=cont.create_image(200,200,image=image2)
image3=PhotoImage(file="23.png")
def pic3():
    image=cont.create_image(200,200,image=image3)
image4=PhotoImage(file="24.png")

def pic4():
    image=cont.create_image(200,200,image=image4)
#image5=PhotoImage(file="11.png")

DateofOrder=StringVar()
value0=StringVar()
value1=StringVar()
value2=StringVar()
value3=StringVar()
value4=StringVar()
value5=StringVar()
value6=StringVar()
value7=StringVar()
value8=StringVar()
value9=StringVar()
value10=StringVar()
value11=StringVar()
value12=StringVar()
#######################################
#---------------------
def mark_register():
    if value0.get()=='P':
        
        value1.set("P")
        value2.set("P")
        value3.set("P")
        value4.set("P")
        value5.set("P")
        value6.set("P")
        value7.set("P")
        value8.set("P")
        value9.set("P")
        value10.set("P")
        value11.set("P")
        value12.set("P")
    elif value0.get()=='A':
        
        value1.set("A")
        value2.set("A")
        value3.set("A")
        value4.set("A")
        value5.set("A")
        value6.set("A")
        value7.set("A")
        value8.set("A")
        value9.set("A")
        value10.set("A")
        value11.set("A")
        value12.set("A")
    elif value0.get()=='L':
        
        value1.set("L")
        value2.set("L")
        value3.set("L")
        value4.set("L")
        value5.set("L")
        value6.set("L")
        value7.set("L")
        value8.set("L")
        value9.set("L")
        value10.set("L")
        value11.set("L")
        value12.set("L")
    elif value0.get()=='S':
        
        value1.set("S")
        value2.set("S")
        value3.set("S")
        value4.set("S")
        value5.set("S")
        value6.set("S")
        value7.set("S")
        value8.set("S")
        value9.set("S")
        value10.set("S")
        value11.set("S")
        value12.set("S")
    elif value0.get()=='0':
##    else:
        value1.set("0")
        value2.set("0")
        value3.set("0")
        value4.set("0")
        value5.set("0")
        value6.set("0")
        value7.set("0")
        value8.set("0")
        value9.set("0")
        value10.set("0")
        value11.set("0")
        value12.set("0")
        
        
        
    
def reset():
    value0.set(" ")
    value1.set(" ")
    value2.set(" ")
    value3.set(" ")
    value4.set(" ")
    value5.set(" ")
    value6.set(" ")
    value7.set(" ")
    value8.set(" ")
    value9.set(" ")
    value10.set(" ")
    value11.set(" ")
    value12.set(" ")
      
    
def qExit():
    qExit=messagebox.askyesno("Exit system","do u wanna exit")
    if qExit>0:
        root.destroy()
        return

    
DateofOrder.set(time.strftime("%d/%m/%Y"))

lblNo=Label(LeftMayFrame1,text="No",bd=16,)
lblNo.place(x=0,y=0)
lblStudentNo=Label(LeftMayFrame1,text="Student No",bd=16)
lblStudentNo.place(x=100,y=0)
lblStudentName=Label(LeftMayFrame1,text="Student Name.",bd=16)
lblStudentName.place(x=200,y=0)

lblCourseCode=Label(LeftMayFrame1,text="Course Code",bd=16)
lblCourseCode.place(x=300,y=0)

box=ttk.Combobox(LeftMayFrame1,textvariable=value0,state='readonly')
box['values']=(' ','P','L','0','A','S')
box.current(0)
box.place(x=400,y=15)
btnFill=Button(LeftMayFrame1,text='fill',padx=2,pady=2,bd=2,fg='black',width=12,height=1,command=mark_register).place(x=600,y=15)
btnReset=Button(LeftMayFrame1,text='reset',padx=2,pady=2,bd=2,fg='black',width=12,height=1,command=reset).place(x=700,y=15)
btnExit=Button(LeftMayFrame1,text='exit',padx=2,pady=2,bd=2,fg='black',width=12,height=1,command=qExit).place(x=800,y=15)
lblDateoforder=Label(LeftMayFrame1,textvariable=DateofOrder,padx=2,pady=2,bd=2,fg='black',bg='white',relief='sunken')
lblDateoforder.place(x=900,y=17)
################################
lblNo=Label(LeftMayFrame2,text="001",bd=16,)
lblNo.place(x=0,y=20)

lblStudent_No_1=Label(LeftMayFrame2,text="15IT28",bd=16)
lblStudent_No_1.place(x=100,y=20)

lblStudent_Name=Label(LeftMayFrame2,text="avi jaiswal",bd=16)
lblStudent_Name.place(x=200,y=20)
lblCourse_Code=Label(LeftMayFrame2,text="23",bd=16)
lblCourse_Code.place(x=300,y=20)
box=ttk.Combobox(LeftMayFrame2,textvariable=value1,state='readonly')
box['values']=(' ','P','L','0','A','S')
box.current(0)
box.place(x=400,y=30)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg='black',width=12,height=1,command=pic1).place(x=600,y=30)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg='black',width=12,height=1,command=pic2).place(x=700,y=30)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg='black',width=12,height=1,command=pic3).place(x=800,y=30)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg='black',width=10,height=1,command=pic4).place(x=900,y=30)
##
##
lblNo=Label(LeftMayFrame2,text="001",bd=16,)
lblNo.place(x=0,y=50)

lblStudent_No_1=Label(LeftMayFrame2,text="15IT28",bd=16)
lblStudent_No_1.place(x=100,y=50)

lblStudent_Name=Label(LeftMayFrame2,text="avi jaiswal",bd=16)
lblStudent_Name.place(x=200,y=50)
lblCourse_Code=Label(LeftMayFrame2,text="23",bd=16)
lblCourse_Code.place(x=300,y=50)
box=ttk.Combobox(LeftMayFrame2,textvariable=value2,state='readonly')
box['values']=(' ','P','L','0','A','S')
box.current(0)
box.place(x=400,y=55)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg='black',width=12,height=1,command=pic1).place(x=600,y=55)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg='black',width=12,height=1,command=pic2).place(x=700,y=55)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg='black',width=12,height=1,command=pic3).place(x=800,y=55)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg='black',width=10,height=1,command=pic4).place(x=900,y=55)
##
###
lblNo=Label(LeftMayFrame2,text="001",bd=16,)
lblNo.place(x=0,y=80)

lblStudent_No_1=Label(LeftMayFrame2,text="15IT28",bd=16)
lblStudent_No_1.place(x=100,y=80)

lblStudent_Name=Label(LeftMayFrame2,text="avi jaiswal",bd=16)
lblStudent_Name.place(x=200,y=80)
lblCourse_Code=Label(LeftMayFrame2,text="23",bd=16)
lblCourse_Code.place(x=300,y=80)
box=ttk.Combobox(LeftMayFrame2,textvariable=value3,state='readonly')
box['values']=(' ','P','L','0','A','S')
box.current(0)
box.place(x=400,y=85)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg='black',width=12,height=1,command=pic1).place(x=600,y=85)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg='black',width=12,height=1,command=pic2).place(x=700,y=85)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg='black',width=12,height=1,command=pic3).place(x=800,y=85)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg='black',width=10,height=1,command=pic4).place(x=900,y=85)
##
##



