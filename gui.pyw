import joblib as jb
import pandas as pd
import tkinter as tk
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt
from tkinter import ttk

data=pd.read_csv('crop data.csv')

d={}
for i in data["State_Name"].unique():
    d[i]=list(data[data["State_Name"]==i]["District_Name"].unique())
    
s_n=list(data["State_Name"].unique())
d_n=list(data["District_Name"].unique())
s=list(data["Season"].unique())
c=list(data["Crop"].unique())

rfr1=jb.load("3054rfr.sav")
r=tk.Tk()
r.geometry("845x440")

def fun6():
    f3.destroy()
    f1=tk.Frame(r)
    f1.place(x=0,y=0,width=845,height=440)
    fun1()
    

def fun3():
    global a1
    global a2
    #global a3
    global a4
    global a5
    global a6,f3
    f2.destroy()
    f3=tk.Frame(r)
    f3.place(x=0,y=0,width=850,height=480)
    background_image=ImageTk.PhotoImage(file='crop.jpeg')
    background_label = tk.Label(f3,image=background_image)
    background_label.image=background_image
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    a1=s_n.index(a1)
    a2=d_n.index(a2)
    a4=s.index(a4)
    a5=c.index(a5)
    global rfr1
    l=[]
    for i in range(len(c)):
        a={}
        a={'State_Name':pd.Series(a1),'District_Name':pd.Series(a2),'Crop_Year':pd.Series(2020),'Season':pd.Series(a4),'Crop':pd.Series(a5),'Area':pd.Series(a6)}
        a["Crop"]=i
        x_input=pd.DataFrame(a)
        p=rfr1.predict(x_input)
        l.append(p)
    print("\n\n\n",l)
    a={}
    a={'State_Name':pd.Series(a1),'District_Name':pd.Series(a2),'Crop_Year':pd.Series(2020),'Season':pd.Series(a4),'Crop':pd.Series(a5),'Area':pd.Series(a6)}
    x_input=pd.DataFrame(a)
    print("\n\n\n",x_input)
    pre=rfr1.predict(x_input)
    pre=pre[0]
    print("\n\n\nyour output",pre)
    l14=tk.Label(f3,text="",font=("monaco",20,"bold"),bg="seagreen1")
    l14.place(x=135,y=65)
    l14.config(text=f"The predited production value\nfor given details is given below\n{pre} tons")  
    b5=tk.Button(f3,text="predict again",font=("monaco",20,"bold"),fg="green",command=fun6)
    b5.place(x=300,y=350)
    
def fun5():
    f4.destroy()
    f1=tk.Frame(r)
    f1.place(x=0,y=0,width=845,height=440)
    fun1()

def fun4():
    f2.destroy()
    global f4
    f4=tk.Frame(r,bg="salmon",width=845,height=440)
    f4.place(x=0,y=0)
    l_f4=tk.Label(text="Please enter the correct values\nand please do not leave anything empty",font=("monaco",20,"bold"),fg="firebrick1",bg="bisque")
    l_f4.place(x=85,y=170)
    b_f4=tk.Button(text="<--back",font=("monaco",20,"bold"),fg="firebrick1",command=fun5)
    b_f4.place(x=40,y=340)

def fun2():
    c=check()
    if(c==1):
        fun3()
    else:
        fun4()

def check():
    global a1,a2,a3,a4,a5,a6
    a1=str(e1.get())
    a2=str(e2.get())
    a4=str(e4.get())
    a5=str(e5.get())
    try:
        if a1 not in s_n:
            raise
        if a2 not in d[a1]:
            raise
        if a4 not in s:
            raise
        if a5 not in c:
            raise
        #a3=float(e3.get())
        a6=float(e6.get())
        return 1
    except:
        return 0
def select_dis(a):
    global a1
    print(a)
    a1=e1.get()
    e2.delete(0,"end")
    e2.configure(values=d[a1])
    

def fun1():
    global e1,e2,e3,e4,e5,e6,e7,e8,f2
    f1.destroy()
    f2=tk.Frame(r)
    f2.place(x=0,y=0,width=850,height=480)
    background_image=ImageTk.PhotoImage(file='crop.jpeg')
    background_label = tk.Label(f2,image=background_image)
    background_label.image=background_image
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    xref=100
    yref=50
    x1ref=480
    l1=tk.Label(f2,text="State Name",fg="green",font=("monaco",20,"bold"))
    l1.place(x=xref,y=yref)
    e1=ttk.Combobox(f2,values=s_n)
    e1.place(x=xref,y=yref+35)
    e1.bind("<<ComboboxSelected>>",select_dis)
    l2=tk.Label(f2,text="District Name",fg="green",font=("monaco",20,"bold"))
    l2.place(x=xref,y=yref+90)
    e2=ttk.Combobox(f2,values=["select state name"])
    e2.place(x=xref,y=yref+125)
    
    l4=tk.Label(f2,text="Season",fg="green",font=("monaco",20,"bold"))
    l4.place(x=x1ref,y=yref)
    e4=ttk.Combobox(f2,values=s)
    e4.place(x=x1ref,y=yref+35)
    l5=tk.Label(f2,text="Crop",fg="green",font=("monaco",20,"bold"))
    l5.place(x=x1ref,y=yref+90)
    e5=ttk.Combobox(f2,values=c)
    e5.place(x=x1ref,y=yref+125)
    l6=tk.Label(f2,text="Area",fg="green",font=("monaco",20,"bold"))
    l6.place(x=250,y=yref+180)
    e6=tk.Entry(f2,font=("monaco",20,"bold"))
    e6.place(x=250,y=yref+215)    
    b2=tk.Button(f2,text="predict",font=("monaco",25,"bold"),fg="green",command=fun2)
    b2.place(x=330,y=360)
        
f1=tk.Frame(r)
f1.place(x=0,y=0,width=850,height=480)
background_image=ImageTk.PhotoImage(file='crop.jpeg')
background_label = tk.Label(f1,image=background_image)
background_label.image=background_image
background_label.grid(column=0,row=0)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
b1=tk.Button(f1,text="  Predict \ncrop production",font=("monaco",25,"bold"),command=fun1)
b1.config(fg="green",justify="center",relief="groove")
b1.place(x=250,y=152)
r.mainloop()
