Python
Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.
Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming. Python is often described as a "batteries included" language due to its comprehensive standard library.
Python was conceived in the late 1980s as a successor to the ABC language. Python 2.0, released in 2000, introduced features like list comprehensions and a garbage collection system capable of collecting reference cycles. Python 3.0, released in 2008, was a major revision of the language that is not completely backward-compatible, and much Python 2 code does not run unmodified on Python 3.
The Python 2 language, i.e. Python 2.7.x, is "sunsetting" on January 1, 2020 (after extension; first planned for 2015), and the Python team of volunteers will not fix security issues, or improve it in other ways after that date. With the end-of-life, only Python 3.5.x and later will be supported.
Python interpreters are available for many operating systems. A global community of programmers develops and maintains CPython, an open source reference implementation. A non-profit organization, the Python Software Foundation, manages and directs resources for Python and CPython development.
Since 2003, Python has consistently ranked in the top ten most popular programming languages in the TIOBE Programming Community Index where, as of December 2018, it is the third most popular language (behind Java, and C). It was selected Programming Language of the Year in 2007, 2010, and 2018.
An empirical study found that scripting languages, such as Python, are more productive than conventional languages, such as C and Java, for programming problems involving string manipulation and search in a dictionary, and determined that memory consumption was often "better than Java and not much worse than C or C++".
Large organizations that use Python include Wikipedia, Google, Yahoo!, CERN, NASA, Facebook, Amazon, Instagram, Spotify and some smaller entities like ILM and ITA. The social news networking site Reddit is written entirely in Python.
Python can serve as a scripting language for web applications, e.g., via mod_wsgi for the Apache web server. With Web Server Gateway Interface, a standard API has evolved to facilitate these applications. Web frameworks like Django, Pylons, Pyramid, TurboGears, web2py, Tornado, Flask, Bottle and Zope support developers in the design and maintenance of complex applications. Pyjs and IronPython can be used to develop the client-side of Ajax-based applications. SQLAlchemy can be used as data mapper to a relational database. Twisted is a framework to program communications between computers, and is used (for example) by Dropbox.
Libraries such as NumPy, SciPy and Matplotlib allow the effective use of Python in scientific computing, with specialized libraries such as Biopython and Astropy providing domain-specific functionality. SageMath is a mathematical software with a notebook interface programmable in Python: its library covers many aspects of mathematics, including algebra, combinatorics, numerical mathematics, number theory, and calculus.
Python has been successfully embedded in many software products as a scripting language, including in finite element method software such as Abaqus, 3D parametric modeler like FreeCAD, 3D animation packages such as 3ds Max, Blender, Cinema 4D, Lightwave, Houdini, Maya, modo, MotionBuilder, Softimage, the visual effects compositor Nuke, 2D imaging programs like GIMP, Inkscape, Scribus and Paint Shop Pro, and musical notation programs like scorewriter and capella. GNU Debugger uses Python as a pretty printer to show complex structures such as C++ containers. Esri promotes Python as the best choice for writing scripts in ArcGIS. It has also been used in several video games, and has been adopted as first of the three available programming languages in Google App Engine, the other two being Java and Go.
Python is commonly used in artificial intelligence projects with the help of libraries like TensorFlow, Keras and Scikit-learn. As a scripting language with modular architecture, simple syntax and rich text processing tools, Python is often used for natural language processing.
Many operating systems include Python as a standard component. It ships with most Linux distributions, AmigaOS 4, FreeBSD (as a package), NetBSD, OpenBSD (as a package) and macOS and can be used from the command line (terminal). Many Linux distributions use installers written in Python: Ubuntu uses the Ubiquity installer, while Red Hat Linux and Fedora use the Anaconda installer. Gentoo Linux uses Python in its package management system, Portage.
Python is used extensively in the information security industry, including in exploit development.
Most of the Sugar software for the One Laptop per Child XO, now developed at Sugar Labs, is written in Python. The Raspberry Pi single-board computer project has adopted Python as its main user-programming language.
LibreOffice includes Python, and intends to replace Java with Python. Its Python Scripting Provider is a core feature since Version 4.0 from 7 February 2013.



Advantages of Python
•	Extensive Support Libraries
It provides large standard libraries that include the areas like string operations, Internet, web service tools, operating system interfaces and protocols. Most of the highly used programming tasks are already scripted into it that limits the length of the codes to be written in Python.
•	Integration Feature
Python integrates the Enterprise Application Integration that makes it easy to develop Web services by invoking COM or COBRA components. It has powerful control capabilities as it calls directly through C, C++ or Java via Jython. Python also processes XML and other markup languages as it can run on all modern operating systems through same byte code.
•	Improved Programmer’s Productivity
The language has extensive support libraries and clean object-oriented designs that increase two to ten fold of programmer’s productivity while using the languages like Java, VB, Perl, C, C++ and C#.
•	Productivity
With its strong process integration features, unit testing framework and enhanced control capabilities contribute towards the increased speed for most applications and productivity of applications. It is a great option for building scalable multi-protocol network applications.


Disadvantages of Python
•	Difficulty in Using Other Languages
The Python lovers become so accustomed to its features and its extensive libraries, so they face problem in learning or working on other programming languages. Python experts may see the declaring of cast “values” or variable “types”, syntactic requirements of adding curly braces or semi colons as an onerous task.
•	Weak in Mobile Computing
Python has made its presence on many desktop and server platforms, but it is seen as a weak language for mobile computing. This is the reason very few mobile applications are built in it like Carbonnelle.
•	Gets Slow in Speed
Python executes with the help of an interpreter instead of the compiler, which causes it to slow down because compilation and execution help it to work normally. On the other hand, it can be seen that it is fast for many web applications too.
•	Run-time Errors
The Python language is dynamically typed so it has many design restrictions that are reported by some Python developers. It is even seen that it requires more testing time, and the errors show up when the applications are finally run.



Contact Management System
A contact management system is a software program that enables users to easily store and find contact information, such as names, addresses and telephone numbers. They are contact-centric databases that provide a fully integrated approach to tracking of all information and communication activities linked to contacts.



A contact management system (CMS) may be chosen because it is thought to provide the following advantages: 
•	Centralized repository of contact information
•	Ready to use database with searching
•	Sales tracking
•	Email integration
•	Scheduling of appointments and meetings
•	Document management
•	Notes and conversation management
•	Customizable fields
•	Import/export utility



Source Code

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
