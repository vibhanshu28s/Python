import os
from tkinter import *

def take():

    #Global Variables---------------------------------
    
    global firstname
    global lastname
    global gender
    global age
    global address
    global contact
    global take_screen
    
    #Global Entries-----------------------------------

    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    
    take_screen= Toplevel(main_screen)
    take_screen.title("Add Contact")
    os.system("cls")

    #Defining Label-----------------------------------

    l1=Label(take_screen,text="First Name")
    l1.grid(row=0,column=0)

    l2=Label(take_screen,text="Last Name")
    l2.grid(row=1,column=0)

    l3=Label(take_screen,text="Gender")
    l3.grid(row=2,column=0)

    l4=Label(take_screen,text="Age")
    l4.grid(row=3,column=0)

    l5=Label(take_screen,text="Address")
    l5.grid(row=4,column=0)

    l6=Label(take_screen,text="Contact")
    l6.grid(row=5,column=0)

    #Defining Entry-----------------------------------

    firstname=StringVar()
    e1=Entry(take_screen,textvariable=firstname)
    e1.grid(row=0,column=1)

    lastname=StringVar()
    e2=Entry(take_screen,textvariable=lastname)
    e2.grid(row=1,column=1)

    gender=StringVar()
    e3=Entry(take_screen,textvariable=gender)
    e3.grid(row=2,column=1)

    age=StringVar()
    e4=Entry(take_screen,textvariable=age)
    e4.grid(row=3,column=1)

    address=StringVar()
    e5=Entry(take_screen,textvariable=address)
    e5.grid(row=4,column=1)

    contact=StringVar()
    e6=Entry(take_screen,textvariable=contact)
    e6.grid(row=5,column=1)

    #Button ADD-----------------------------------
    b1=Button(take_screen,text="ADD",width=12,command=add)
    b1.grid(row=6,column=2)
    
    
def add():
    first_name=firstname.get()
    last_name=lastname.get()
    gender1=gender.get()
    age1=age.get()
    address1=address.get()
    contact1=contact.get()
    
    
    file=open("data.txt","a")
    file.write(first_name)
    
    file.write("\n")
    file.write(last_name)

    file.write("\n")
    file.write(gender1)

    file.write("\n")
    file.write(age1)

    file.write("\n")
    file.write(address1)

    file.write("\n")
    file.write(contact1)
    file.write("\n")
    
    file.close()

    
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    
    #Label message-----------------------------------
    l0=Label(take_screen,text="Contact Added Sucessfully")
    l0.grid(row=7,column=2)

    
def deleteall():
    os.system("cls")
    try:
        os.remove("data.txt")
        print("Deleted")

    except:
        print("Already Deleted")



def show():
    os.system("cls")
    try:
        file=open("data.txt","r")
        f=file.readline()
        cnt=0
        while f:
            f=file.readline()
            cnt+=1

        cnt=int(cnt/6)
        print(cnt)
        file.close()
     
        i=1
        file=open("data.txt","r")
        os.system("cls")
        while(i<=cnt):
            print("----------------------------------------------------------")
            print("{}.".format(i))
            print("First name=",file.readline().strip())
            print("Last name=",file.readline().strip())
            print("Gender=",file.readline().strip())
            print("Age=",file.readline().strip())
            print("Address=",file.readline().strip())
            print("Contact=",file.readline().strip())
            print("----------------------------------------------------------")
            i+=1
        file.close()
    except:
        print()
        print("Empty!")
 

    
def mainscreen():
    global main_screen
    main_screen=Tk() 
    main_screen.title("Main Screen")
        
    l1=Label(text="*****Contact Management System*****")
    l1.grid(row=0,column=2)
        
    b1=Button(text="ADD Contact",width=12,command=take)
    b1.grid(row=1,column=2)

    b2=Button(text="Display Contact",width=12,command=show)
    b2.grid(row=2,column=2)

    b3=Button(text="Delete All",width=12,command=deleteall)
    b3.grid(row=3,column=2)

    b4=Button(text="Exit",width=12,command=main_screen.destroy)
    b4.grid(row=4,column=2)
 
    main_screen.mainloop()
mainscreen()
'''
Developed By -
Vibhanshu Kumar Singh
'''
