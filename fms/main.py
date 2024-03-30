# To use or import Tkinter
from tkinter import *
from tkinter import ttk
# To display the date and time
import time
# To connect to Database
from sqlite3 import *
# To show the messages
from tkinter import messagebox
# For Mail Functionality
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
# For Validations
import re
from hashlib import sha256
# For Reports
from fpdf import FPDF
import pandas as pd

class Fms:

#--------------------------------------------------- All Login Pages Code Start ------------------------------------------------------------------#    

#--  Main/User Login Page-----------------
    
    def main(fms):
        try:
            fms.scr.destroy()
            fms.scr=Tk()
        except:
            try:
                fms.scr=Tk()
            except:
                pass

        # getting screen width and height of display
        width= fms.scr.winfo_screenwidth() 
        height= fms.scr.winfo_screenheight()
        
        #setting tkinter window size
        fms.scr.geometry("%dx%d" % (width, height))
        
        fms.scr.title("FOOD MANAGEMENT SYSTEM")
 
        # Logo picture   
        fms.loginf1=Frame(fms.scr, bg="#ffffff")
        fms.loginf1.pack(fill=BOTH,expand=YES)

        fms.logo=PhotoImage(file="header.png")
        fms.logo_img = fms.logo.subsample(2,2)
        fms.logo_banner = Label(fms.loginf1, image=fms.logo_img)
        fms.logo_banner.place(x=0,y=0)
        fms.logo_banner.pack(side=LEFT)  

        fms.home=Button(fms.loginf1,text="Home", command=fms.main, bg="#0b1335",cursor="hand2",fg="white",font=("cooper black",14))
        fms.home.place(x=925,y=100)
       
        fms.adlog=Button(fms.loginf1,text="Admin Login",command=fms.Adminlogin,cursor="hand2", bg="#0b1335",fg="white",font=("cooper black",14))
        fms.adlog.place(x=1025,y=100)
       
        fms.abt=Button(fms.loginf1,text="Manager Login", command=fms.Managerlogin, bg="#0b1335",cursor="hand2", fg="white",font=("cooper black",14))
        fms.abt.place(x=1200,y=100)

        # code to display the local time
        fms.localtime=time.asctime(time.localtime(time.time()))
        fms.tim=Label(fms.loginf1,text=fms.localtime,fg="white",font=("cooper black",14),bg="#0b1335")
        fms.tim.place(x=1000,y=50)

        fms.loginf2=Frame(fms.scr,height=1080,width=1920)
        fms.c=Canvas(fms.loginf2,height=1080,width=1920)

        fms.c.pack()
        fms.fmain=PhotoImage(file="main.png")
        fms.c.create_image(650,309,image=fms.fmain)
        fms.c.create_rectangle(350,100,1020,475,fill="#d3ede6",outline="white",width=6)
        fms.log=Label(fms.loginf2,text="USER LOGIN",fg="white",bg="#0b1335",width=27,font=("cooper black",27))
        fms.log.place(x=357,y=110)
        fms.lab1=Label(fms.loginf2,text="User Name",bg="#d3ede6",font=("cooper black",22))
        fms.lab1.place(x=360,y=200)
        fms.user=Entry(fms.loginf2,bg="white",font=("cooper black",22),bd=5)
        fms.user.place(x=650,y=200)
        fms.lab2=Label(fms.loginf2,text="Password",bg="#d3ede6",font=("cooper black",22))
        fms.lab2.place(x=360,y=270)
        fms.pasd=Entry(fms.loginf2,bg="white",font=("cooper black",22),bd=5, show="*")
        fms.pasd.place(x=650,y=270)

        fms.cl=Button(fms.loginf2,text="Clear",cursor="hand2",command=lambda:clear(fms),fg="white",bg="#0b1335",font=("cooper black",20),bd=4)
        fms.cl.place(x=550,y=330)
        
        fms.lg=Button(fms.loginf2,text="Login",cursor="hand2",fg="white",bg="#0b1335",command=fms.userdatabase,font=("cooper black",20),bd=4)
        fms.lg.place(x=700,y=330)
        
        fms.rg=Button(fms.loginf2,text="Click Here to Register",command=fms.Register,fg="white",cursor="hand2",bg="#8c68c1",font=("cooper black",20),bd=6)
        fms.rg.place(x=505,y=400)
        
        def clear(fms):
            fms.user.delete(0,END)
            fms.pasd.delete(0,END)
        
        fms.loginf2.pack(fill=BOTH,expand= YES)        
        fms.scr.mainloop()
         
#--  Admin Login Page ------
        
    def Adminlogin(fms):

        fms.scr.destroy()
        fms.scr=Tk()
        style = ttk.Style()
        style.configure('Red.TLabel', foreground='red')
 
        # getting screen width and height of display
        width= fms.scr.winfo_screenwidth() 
        height= fms.scr.winfo_screenheight()
        
        #setting tkinter window size
        fms.scr.geometry("%dx%d" % (width, height))
        
        fms.scr.title("FOOD MANAGEMENT SYSTEM")
 
        fms.adminf1=Frame(fms.scr, bg="#ffffff")

        fms.logo = PhotoImage(file="logo.png")
        fms.logo_img = fms.logo.subsample(2,2)
        
        fms.logo_banner = Label(fms.adminf1, image=fms.logo_img)
        fms.logo_banner.place(x=0,y=0)
     
        fms.logo_banner.pack(side=LEFT)  

        fms.home=Button(fms.adminf1,text="Home", command=fms.main, bg="#0b1335",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.home.place(x=1075,y=100)

        # code to display the local time
        fms.localtime=time.asctime(time.localtime(time.time()))
        fms.tim=Label(fms.adminf1,text=fms.localtime,fg="white",font=("cooper black",14),bg="#0b1335")
        fms.tim.place(x=1000,y=50)

        fms.adminf1.pack(fill=BOTH,expand=YES)

        fms.adminf2=Frame(fms.scr,height=1080,width=1920)
        fms.c=Canvas(fms.adminf2,height=1080,width=1920)
        fms.c.pack()
        fms.fmain=PhotoImage(file="main.png")
        fms.c.create_image(650,309,image=fms.fmain)
        fms.c.create_rectangle(350,100,1020,425,fill="#d3ede6",outline="white",width=6)
        fms.log=Label(fms.adminf2,text="ADMIN LOGIN",fg="white",bg="#0b1335",width=27,font=("cooper black",27))
        fms.log.place(x=357,y=110)
        fms.lab1=Label(fms.adminf2,text="User Name",bg="#d3ede6",font=("cooper black",22))
        fms.lab1.place(x=360,y=200)
        fms.usera=Entry(fms.adminf2,bg="white",font=("cooper black",22),bd=5)
        fms.usera.place(x=650,y=200)
        fms.lab2=Label(fms.adminf2,text="Password",bg="#d3ede6",font=("cooper black",22))
        fms.lab2.place(x=360,y=270)
        fms.pasda=Entry(fms.adminf2,bg="white",font=("cooper black",22),bd=5, show="*")
        fms.pasda.place(x=650,y=270)
        fms.lg=Button(fms.adminf2,text="Login",cursor="hand2",fg="white",bg="#0b1335",command=fms.admindatabase,font=("cooper black",20,'bold'),bd=5)
        fms.lg.place(x=650,y=350)
        fms.cl=Button(fms.adminf2,text="Back",cursor="hand2",fg="white",bg="#0b1335",command=fms.main,font=("cooper black",20,'bold'),bd=5)
        fms.cl.place(x=360,y=350)
        def clear(fms):
            fms.usera.delete(0,END)
            fms.pasda.delete(0,END)
        fms.rg=Button(fms.adminf2,text="Clear",fg="white",cursor="hand2",bg="#0b1335",command=lambda:clear(fms),bd=5,font=("cooper black",20,'bold'))
        fms.rg.place(x=900,y=350)
        
        fms.adminf2.pack(fill=BOTH,expand= YES)
   
        fms.scr.mainloop()

#--  Manager Login Page ------

    def Managerlogin(fms):

        fms.scr.destroy()
        fms.scr=Tk()
 
        # getting screen width and height of display
        width= fms.scr.winfo_screenwidth() 
        height= fms.scr.winfo_screenheight()
        
        #setting tkinter window size
        fms.scr.geometry("%dx%d" % (width, height))
        
        fms.scr.title("FOOD MANAGEMENT SYSTEM")
 
        fms.managerf1=Frame(fms.scr, bg="#ffffff")

        fms.logo = PhotoImage(file="logo.png")
        fms.logo_img = fms.logo.subsample(2,2)
        
        fms.logo_banner = Label(fms.managerf1, image=fms.logo_img)
        fms.logo_banner.place(x=0,y=0)
     
        fms.logo_banner.pack(side=LEFT)  

        fms.home=Button(fms.managerf1,text="Home", command=fms.main, bg="#0b1335",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.home.place(x=1075,y=100)

        # code to display the local time
        fms.localtime=time.asctime(time.localtime(time.time()))
        fms.tim=Label(fms.managerf1,text=fms.localtime,fg="white",font=("cooper black",14),bg="#0b1335")
        fms.tim.place(x=1000,y=50)
        fms.managerf1.pack(fill=BOTH,expand=YES)


        fms.managerf2=Frame(fms.scr,height=1080,width=1920)
        fms.c=Canvas(fms.managerf2,height=1080,width=1920)
        fms.c.pack()
        fms.fmain=PhotoImage(file="main.png")
        fms.c.create_image(650,309,image=fms.fmain) 
        fms.c.create_rectangle(350,100,1020,425,fill="#d3ede6",outline="white",width=6)
        fms.log=Label(fms.managerf2,text="MANAGER LOGIN",fg="white",bg="#0b1335",width=27,font=("cooper black",27))
        fms.log.place(x=357,y=110)
        fms.lab1=Label(fms.managerf2,text="User Name",bg="#d3ede6",font=("cooper black",22))
        fms.lab1.place(x=360,y=200)
        fms.usera=Entry(fms.managerf2,bg="white",font=("cooper black",22),bd=5)
        fms.usera.place(x=650,y=200)
        fms.lab2=Label(fms.managerf2,text="Password",bg="#d3ede6",font=("cooper black",22))
        fms.lab2.place(x=360,y=270)
        fms.pasda=Entry(fms.managerf2,bg="white",font=("cooper black",22),bd=5, show="*")
        fms.pasda.place(x=650,y=270)
        fms.lg=Button(fms.managerf2,text="Login",cursor="hand2",fg="white",bg="#0b1335",command=fms.managerdatabase,font=("cooper black",20,'bold'),bd=5)
        fms.lg.place(x=650,y=350)
        fms.cl=Button(fms.managerf2,text="Back",cursor="hand2",fg="white",bg="#0b1335",command=fms.main,font=("cooper black",20,'bold'),bd=5)
        fms.cl.place(x=360,y=350)
        def clear(fms):
            fms.usera.delete(0,END)
            fms.pasda.delete(0,END)
        fms.rg=Button(fms.managerf2,text="Clear",fg="white",cursor="hand2",bg="#0b1335",command=lambda:clear(fms),bd=5,font=("cooper black",20,'bold'))
        fms.rg.place(x=900,y=350)
        
        fms.managerf2.pack(fill=BOTH,expand= YES)
   
        fms.scr.mainloop()

#----------------------------------------------------- All Login Pages Code End -----------------------------------------------------------------#    

#------------------------------------------------------User Registration Page Start--------------------------------------------------------------------#
   
    def Register(fms):
        
        fms.scr.destroy()
        fms.scr=Tk()
        
        # getting screen width and height of display
        width= fms.scr.winfo_screenwidth() 
        height= fms.scr.winfo_screenheight()
        
        #setting tkinter window size
        fms.scr.geometry("%dx%d" % (width, height))
        
        fms.scr.title("FOOD MANAGEMENT SYSTEM")
        #fms.scr.resizable(False, False)
        
        fms.regf1=Frame(fms.scr, bg="#ffffff")
        fms.logo = PhotoImage(file="logo.png")
        fms.logo_img = fms.logo.subsample(2,2)
        fms.logo_banner = Label(fms.regf1, image=fms.logo_img)
        fms.logo_banner.place(x=0,y=0)
        fms.logo_banner.pack(side=LEFT)  

        fms.home=Button(fms.regf1,text="Home",command=fms.main,bg="#0b1335",cursor="hand2",fg="white",font=("cooper black",16))
        fms.home.place(x=800,y=100)
        fms.adlog=Button(fms.regf1,text="Admin Login",command=fms.Adminlogin,cursor="hand2",bg="#0b1335",fg="white",font=("cooper black",16))
        fms.adlog.place(x=950,y=100)
        fms.abt=Button(fms.regf1,text="Manager Login",command=fms.Managerlogin,bg="#0b1335",cursor="hand2",fg="white",font=("cooper black",16))
        fms.abt.place(x=1210,y=100)

        # code to display the local time
        fms.localtime=time.asctime(time.localtime(time.time()))
        fms.tim=Label(fms.regf1,text=fms.localtime,fg="white",font=("cooper black",16),bg="#0b1335")
        fms.tim.place(x=925,y=50)

        fms.regf1.pack(fill=BOTH,expand=1)
        
        fms.regf2=Frame(fms.scr,height=1080,width=1920)
        fms.c=Canvas(fms.regf2,height=1080,width=1920)
        fms.c.pack()
                
        fms.fmain = PhotoImage(file="main.png")
        fms.c.create_image(650,300,image=fms.fmain)
        fms.c.create_rectangle(180,110,1150,435,fill="#d3ede6",outline="white",width=6)
    
        fms.log=Label(fms.regf2,text="REGISTRATION",fg="white",bg="#0b1335",width=20,font=("cooper black",27))
        fms.log.place(x=480,y=120)

        fms.lab1=Label(fms.regf2,text="First Name",bg="#d3ede6",font=("cooper black",18))
        fms.lab1.place(x=190,y=200)
        fms.first=Entry(fms.regf2,bg="white",width=15,font=("cooper black",18),bd=5)
        fms.first.place(x=430,y=200)
        
        fms.lab2=Label(fms.regf2,text="Last Name",bg="#d3ede6",font=("cooper black",18))
        fms.lab2.place(x=730,y=200)
        fms.last=Entry(fms.regf2,bg="white",width=15,font=("cooper black",18),bd=5)
        fms.last.place(x=920,y=200)
        
        fms.lab3=Label(fms.regf2,text="User Name",bg="#d3ede6",font=("cooper black",18))
        fms.lab3.place(x=190,y=250)
        fms.usern=Entry(fms.regf2,bg="white",width=15,font=("cooper black",18),bd=5)
        fms.usern.place(x=430,y=250)
        
        fms.lab4=Label(fms.regf2,text="Password",bg="#d3ede6",font=("cooper black",18))
        fms.lab4.place(x=730,y=250)
        fms.passd=Entry(fms.regf2,bg="white",width=15,font=("cooper black",18),bd=5, show="*")
        fms.passd.place(x=920,y=250)
        
        fms.lab5 = Label(fms.regf2, text="Email", bg="#d3ede6", font=("cooper black", 18))
        fms.lab5.place(x=190, y=300)
        fms.email=Entry(fms.regf2,bg="white",width=15,font=("cooper black",18),bd=5)
        fms.email.place(x=430, y=300)

        fms.lab6 = Label(fms.regf2, text="Mobile No.", bg="#d3ede6", font=("cooper black", 18))
        fms.lab6.place(x=730, y=300)
        fms.mob = Entry(fms.regf2, bg="white", width=15, font=("cooper black", 18), bd=5)
        fms.mob.place(x=920, y=300)

        fms.bc=Button(fms.regf2,text="Back",cursor="hand2",command=fms.main,fg="white",bg="#0b1335",font=("cooper black",18),bd=5)
        fms.bc.place(x=370,y=370)
        fms.rg=Button(fms.regf2,text="Register",cursor="hand2",fg="white",bg="#0b1335",command=fms.userReg,font=("cooper black",18),bd=5)
        fms.rg.place(x=610,y=370)
        
        fms.cl=Button(fms.regf2,text="Clear",cursor="hand2",fg="white",bg="#0b1335",command=lambda:clear(fms),font=("cooper black",18),bd=5)
        
        fms.cl.place(x=910,y=370)
        fms.regf2.pack(fill=BOTH,expand=1)
        
        def clear(fms):
            fms.first.delete(0,END)
            fms.last.delete(0,END)
            fms.usern.delete(0,END)
            fms.passd.delete(0,END)
            fms.email.delete(0,END)
            fms.mob.delete(0,END)
        
        fms.scr.mainloop()

#------------------------------------------------------User Registration Page End-----------------------------------------------------------------#

#-------------------------------------------------- Admin Dashboard Code Start -------------------------------------------------------------------#    

#-- View All Managers Page ---
    
    def Viewmanagers(fms):

        fms.scr.destroy()
        fms.scr = Tk()
        style = ttk.Style()
        style.configure('Red.TLabel', foreground='red')
    
        # getting screen width and height of display
        width= fms.scr.winfo_screenwidth() 
        height= fms.scr.winfo_screenheight()
        
        #setting tkinter window size
        fms.scr.geometry("%dx%d" % (width, height))
        
        fms.scr.title("FOOD MANAGEMENT SYSTEM")
        
        fms.managerdashf1= Frame(fms.scr, bg="#ffffff")

        fms.logo = PhotoImage(file="logo.png")
        fms.logo_img1 = fms.logo.subsample(2,2)
        
        fms.logo_banner1 = Label(fms.managerdashf1, image=fms.logo_img1)
        fms.logo_banner1.pack(side=LEFT)  

        fms.managerlabel= Label(text="Weclome to Admin Dashboard!!", bg="#0b1335", fg="white",font=("cooper black",14))
        fms.managerlabel.place(x=1000,y=50)

        fms.logout=Button(fms.managerdashf1,text="LOGOUT", command=fms.main, bg="#0b1335",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.logout.place(x=1075,y=100)
       
        # code to display the local time
        fms.localtime=time.asctime(time.localtime(time.time()))
        fms.tim=Label(fms.managerdashf1,text=fms.localtime,fg="white",font=("cooper black",14),bg="#0b1335")
        fms.managerdashf1.pack(fill=BOTH)

        fms.sidebar = Frame(fms.scr, bg="#d3ede6")
        fms.sidebar.pack(side=LEFT, fill=Y) 
        
        # Add buttons to the sidebar

        fms.viewmanagers= Button(fms.sidebar,text="VIEW MANAGERS", command=fms.Viewmanagers, bg="#f39c12",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.viewmanagers.grid(row=3, column=0, ipadx=11, padx=25, pady=25)

        fms.viewusers= Button(fms.sidebar,text="VIEW USERS", command=fms.Viewusers, bg="#0b1335",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.viewusers.grid(row=5, column=0, ipadx=36, padx=25, pady=25)

        fms.viewdonations= Button(fms.sidebar,text="VIEW DONATIONS", command=fms.Viewdonations, bg="#0b1335",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.viewdonations.grid(row=6, column=0, ipadx=8, padx=25, pady=25)

        fms.viewreports = Button(fms.sidebar,text="REPORTS", command=fms.Viewreports, bg="#0b1335",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.viewreports.grid(row=7, column=0, ipadx=53, padx=25, pady=25)
        
        def show_custom_messages(message):
            # Create a new top-level window
            message_dialog = Toplevel()
            message_dialog.title("Message")
            
            # Set window size and position it in the center of the screen
            window_width = 350
            window_height = 150
            screen_width = message_dialog.winfo_screenwidth()
            screen_height = message_dialog.winfo_screenheight()
            x = (screen_width - window_width) // 2
            y = (screen_height - window_height) // 2
            message_dialog.geometry(f"{window_width}x{window_height}+{x}+{y}")
            
            # Add an icon label in #32CD32 color
            style = ttk.Style()
            style.configure("Error.TLabel", foreground="#32CD32")
            error_icon = ttk.Label(message_dialog, text="\u24D8", style="Error.TLabel", font=("Cooper Black", 24))
            error_icon.pack(pady=10)

            label = Label(message_dialog, text=message, fg="#32CD32", font=("Cooper Black", 12))
            label.pack(padx=10, pady=0)

            # Add an "OK" button to close the dialog
            ok_button = Button(message_dialog, text="OK", command=message_dialog.destroy, width=10, font=("Cooper Black", 12))
            ok_button.pack(pady=10)

        def show_custom_error(message):
            # Create a new top-level window
            error_dialog = Toplevel()
            error_dialog.title("Error Message")
            
            # Set window size and position it in the center of the screen
            window_width = 650
            window_height = 150
            screen_width = error_dialog.winfo_screenwidth()
            screen_height = error_dialog.winfo_screenheight()
            x = (screen_width - window_width) // 2
            y = (screen_height - window_height) // 2
            error_dialog.geometry(f"{window_width}x{window_height}+{x}+{y}")

            # Add an icon label in red color
            style = ttk.Style()
            style.configure("Error.TLabel", foreground="red")
            error_icon = ttk.Label(error_dialog, text="\u26A0", style="Error.TLabel", font=("Cooper Black", 24))
            error_icon.pack(pady=10)

            label = Label(error_dialog, text=message, fg="red", font=("Cooper Black", 12))
            label.pack(padx=10, pady=0)
            
            # Add an "OK" button to close the dialog
            ok_button = Button(error_dialog, text="OK", command=error_dialog.destroy, width=10, font=("Cooper Black", 12))
            ok_button.pack(pady=10)

        # Function to load data into the Treeview
        def managers_data():

            # Clear the existing data in the Treeview
            tree.delete(*tree.get_children())

            # Connect to the database
            conn = connect('fms.db')
            cursor = conn.cursor()

            # Retrieve the managers data from the database
            cursor.execute("SELECT manager_id, first_name, last_name, user_name, department, email FROM managers")
            managers = cursor.fetchall()

            # Insert the data into the Treeview
            for manager in managers:
                tree.insert("", "end", values=(manager[0], manager[1], manager[2], manager[3], manager[4], manager[5]), tags=("my_font"))

            # Close the connection
            conn.close()

        # Function to edit a manager's details
        def edit_managers():

            # Get the selected item from the Treeview
            selected_item = tree.focus()
            
            if not selected_item:
                show_custom_error("Please select manager to edit")
                return

            #Get the values of the selected record
            values = tree.item(selected_item, "values")
            manager_id = values[0]

            def submit():
                # Get values from entry widgets
                first_name = first_name_entry.get()
                last_name = last_name_entry.get()
                user_name = user_name_entry.get()
                department = selected_department.get()
                email = email_entry.get()

                # Validate fields
                if not (first_name and last_name and user_name and department and email):
                    show_custom_error("All fields are required")
                    return

                # Validate email format
                if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
                    show_custom_error("Invalid email format")
                    return

                # Connect to the database
                conn = connect('fms.db')
                cursor = conn.cursor()

                try:
                    # Check if the user_name or email already exists for other managers
                    cursor.execute("SELECT COUNT(*) FROM managers WHERE (user_name=? OR email=?) AND manager_id != ?", (user_name, email, manager_id))
                    existing_managers_count = cursor.fetchone()[0]

                    if existing_managers_count > 0:
                        # User_name or email already exists for other managers, show error message
                        show_custom_error("User name or email already exists. Please choose a different one.")
                    else:
                        # Proceed with updating the manager details
                        # Print the SQL query to verify correctness
                        print(f"Executing EDIT query: EDIT FROM managers WHERE manager_id = {manager_id}")

                        # Update manager in the managers table
                        cursor.execute("UPDATE managers SET first_name=?, last_name=?, user_name=?, department=?, email=? WHERE manager_id=?",
                                    (first_name, last_name, user_name, department, email, manager_id))

                        # Commit the changes
                        conn.commit()

                        # Show success message
                        show_custom_messages("Manager details updated successfully")

                        # Refresh the Treeview
                        managers_data()

                except Exception as e:
                    # Show error message if update fails
                    show_custom_error(f"Failed to update the manager: {str(e)}")

                finally:
                    # Close the connection
                    conn.close()
                    # Close the edit window
                    edit_window.destroy()

            # Create a Toplevel window for editing a manager
            edit_window = Toplevel()
            edit_window.title("Edit Manager")

            # Calculate the center coordinates of the screen
            screen_width = edit_window.winfo_screenwidth()
            screen_height = edit_window.winfo_screenheight()
            window_width = 700
            window_height = 225
            x = (screen_width - window_width) // 2
            y = (screen_height - window_height) // 2

            # Set the geometry of the window to be centered and larger
            edit_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

            # Create labels and entry widgets for each field
            Label(edit_window, text="First Name:", font=("Cooper Black", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
            first_name_entry = Entry(edit_window, font=("Cooper Black", 12))
            first_name_entry.grid(row=0, column=1, padx=10, pady=10)

            Label(edit_window, text="Last Name:", font=("Cooper Black", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
            last_name_entry = Entry(edit_window, font=("Cooper Black", 12))
            last_name_entry.grid(row=1, column=1, padx=10, pady=10)

            Label(edit_window, text="User Name:", font=("Cooper Black", 12)).grid(row=0, column=2, padx=10, pady=10, sticky="e")
            user_name_entry = Entry(edit_window, font=("Cooper Black", 12))
            user_name_entry.grid(row=0, column=3, padx=10, pady=10)
            # user_name_entry.insert(0, values[3])  # Insert the user_name from the selected record

            Label(edit_window, text="Email:", font=("Cooper Black", 12)).grid(row=3, column=0, padx=10, pady=10, sticky="e")
            email_entry = Entry(edit_window, font=("Cooper Black", 12))
            email_entry.grid(row=3, column=1, padx=10, pady=10)
            # email_entry.insert(0, values[5])  # Insert the email from the selected record

            Label(edit_window, text="Department:", font=("Cooper Black", 12)).grid(row=1, column=2, padx=10, pady=10, sticky="e")
            department_options = ["One Central", "Eatry", "Merill", "Dine and Connect", "Catering"]
            selected_department = StringVar(edit_window)
            selected_department.set(department_options[0])
            department_dropdown = OptionMenu(edit_window, selected_department, *department_options)
            department_dropdown.config(font=("Cooper Black", 12))
            department_dropdown.grid(row=1, column=3, padx=10, pady=10, sticky="w")

            # Populate the entry widgets with the selected manager's data
            first_name_entry.insert(0, values[1])
            last_name_entry.insert(0, values[2])
            user_name_entry.insert(0, values[3])
            selected_department.set(values[4])
            email_entry.insert(0, values[5])
            
            # Create a Submit button
            submit_button = Button(edit_window, text="Submit", command=submit, font=("Cooper Black", 12))
            submit_button.grid(row=4, columnspan=4, pady=10)

            # Main loop for the edit window
            edit_window.mainloop()

        # Function to delete a manager
        def delete_managers():
            
            # Get the selected item from the Treeview
            selected_item = tree.focus()

            if not selected_item:
                show_custom_error("Please select manager to delete")
                return

            # Fetch the manager_id from the dictionary 
            values = tree.item(selected_item, "values")
            manager_id = values[0]

            # Connect to the database
            conn = connect('fms.db')
            cursor = conn.cursor()
            
            try:
                # Check if the manager has any donations associated with them
                cursor.execute("SELECT COUNT(*) FROM donation_details WHERE manager_id = ?", (manager_id,))
                donation_count = cursor.fetchone()[0]

                if donation_count > 0:
                    # Manager has donations associated with them, show error message
                    show_custom_error("Cannot delete manager. Manager has donations associated with them.")
                else:
                    # Proceed with deleting the manager
                    # Print the SQL query to verify correctness
                    print(f"Executing DELETE query: DELETE FROM managers WHERE manager_id = {manager_id}")

                    # Delete the record from the managers table
                    cursor.execute("DELETE FROM managers WHERE manager_id = ?", (manager_id,))
                    
                    # Commit the changes
                    conn.commit()

                    # Show success message
                    show_custom_messages("Manager deleted successfully")

                    # Refresh the Treeview
                    managers_data()

            except Exception as e:
                # Show error message if deletion fails
                show_custom_error(f"Failed to delete manager: {str(e)}")

            finally:
                # Close the connection
                conn.close()

        def create_managers_table_if_not_exists():
                conn = connect('fms.db')  # Replace 'your_database.db' with your actual database name
                cursor = conn.cursor()

                # SQL query to create the table if it does not exist
                create_table_query = '''
                CREATE TABLE IF NOT EXISTS managers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    user_name TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    email TEXT NOT NULL,
                    department TEXT NOT NULL
                );
                '''
                cursor.execute(create_table_query)
                conn.commit()
                conn.close()

        # Function to add a new manager
        def add_managers():            
            def submit():
                # Get values from entry widgets
                user_name = user_name_entry.get()
                password = password_entry.get()
                email = email_entry.get()
                first_name = first_name_entry.get()
                last_name = last_name_entry.get()
                department = selected_department.get()

                # Validate fields
                if not (user_name and password and email and first_name and last_name and department):
                    # Example usage
                    show_custom_error("All fields are required")
                    return

                # Validate email format
                if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
                    show_custom_error("Invalid email format")
                    return

                try:                    
                    
                    create_managers_table_if_not_exists()  # Check and create table if not exists

                    # Connect to the database
                    conn = connect('fms.db')
                    cursor = conn.cursor()

                    # Insert new manager into the managers table
                    cursor.execute("INSERT INTO managers (first_name, last_name, user_name, password, email, department) VALUES (?, ?, ?, ?, ?, ?)",
                                  (first_name, last_name, user_name, password, email, department))

                    # Commit the changes
                    conn.commit()

                    # Show success message
                    show_custom_messages("Manager added successfully")

                    # Refresh the Treeview
                    managers_data()

                except Exception as e:
                    # Show error message if insertion fails
                    show_custom_error("Failed to add manager: {str(e)}")
                
                finally:
                    # Close the connection
                    conn.close()
                    # Close the add window
                    add_window.destroy()

            # Create a Toplevel window for adding a new manager
            add_window = Toplevel()
            add_window.title("Add Manager")

            # Calculate the center coordinates of the screen
            screen_width = add_window.winfo_screenwidth()
            screen_height = add_window.winfo_screenheight()
            window_width = 750
            window_height = 225
            x = (screen_width - window_width) // 2
            y = (screen_height - window_height) // 2

            # Set the geometry of the window to be centered and larger
            add_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

             # Create labels and entry widgets for each field
            Label(add_window, text="First Name:", font=("Cooper Black", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
            first_name_entry = Entry(add_window, font=("Cooper Black", 12))
            first_name_entry.grid(row=0, column=1, padx=10, pady=10)

            Label(add_window, text="Last Name:", font=("Cooper Black", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
            last_name_entry = Entry(add_window, font=("Cooper Black", 12))
            last_name_entry.grid(row=1, column=1, padx=10, pady=10)

            Label(add_window, text="User Name:", font=("Cooper Black", 12)).grid(row=2, column=0, padx=10, pady=10, sticky="e")
            user_name_entry = Entry(add_window, font=("Cooper Black", 12))
            user_name_entry.grid(row=2, column=1, padx=10, pady=10)

            Label(add_window, text="Password:", font=("Cooper Black", 12)).grid(row=0, column=2, padx=10, pady=10, sticky="e")
            password_entry = Entry(add_window, font=("Cooper Black", 12))
            password_entry.grid(row=0, column=3, padx=10, pady=10)

            Label(add_window, text="Email:", font=("Cooper Black", 12)).grid(row=2, column=2, padx=10, pady=10, sticky="e")
            email_entry = Entry(add_window, font=("Cooper Black", 12))
            email_entry.grid(row=2, column=3, padx=10, pady=10)

            Label(add_window, text="Department:", font=("Cooper Black", 12)).grid(row=1, column=2, padx=10, pady=10, sticky="e")
            department_options = ["One Central", "Eatry", "Merill", "Dine and Connect", "Catering"]
            selected_department = StringVar(add_window)
            selected_department.set(department_options[0])
            department_dropdown = OptionMenu(add_window, selected_department, *department_options)
            department_dropdown.config(font=("Cooper Black", 12))
            department_dropdown.grid(row=1, column=3, padx=10, pady=10, sticky="w")

            # Create a Submit button
            submit_button = Button(add_window, text="Submit", command=submit, font=("Cooper Black", 12))
            submit_button.grid(row=4, columnspan=4, pady=10)

            # Main loop for the add window
            add_window.mainloop()

        # Create the main content frame
        content_frame = Frame(fms.scr, bg="lightgray")
        content_frame.pack(side=LEFT, fill=BOTH, expand=True)

        # Create a label for the title
        title_label = Label(content_frame, text="VIEW MANAGERS", font=("Cooper Black", 16), bg="#0b1335", fg="white", pady=10)
        title_label.pack(fill=X)
        title_label.pack(pady=(0, 85))

        # Create treeview
        tree = ttk.Treeview(content_frame, columns=("Manager ID", "First Name", "Last Name", "User Name", "Department", "Email"), show="headings", padding=(0, 5))

        # Set the font for the headings
        tree.heading("Manager ID", text="Manager ID", anchor=CENTER)
        tree.heading("First Name", text="First Name", anchor=CENTER)
        tree.heading("Last Name", text="Last Name", anchor=CENTER)
        tree.heading("User Name", text="User Name", anchor=CENTER)
        tree.heading("Department", text="Department", anchor=CENTER)
        tree.heading("Email", text="Email", anchor=CENTER)

        # Configure Treeview style
        style = ttk.Style()
        style.configure("Custom.Treeview", font=("Cooper Black", 12))
        style.configure("Treeview.Row", padding=(0, 5))

        # Set the background color for the headers
        style.configure("Treeview.Heading", background="gray")

        # Define a tag named "my_font" with the desired font
        tree.tag_configure("my_font", font=("Cooper Black", 12))
        tree.pack()

        # Connect to the SQLite3 database
        conn = connect('fms.db')
        cursor = conn.cursor()

        # Fetch and display data
        cursor.execute("SELECT manager_id, first_name, last_name, user_name, department, email FROM managers")
        managers = cursor.fetchall()
        
        for manager in managers:
            
            tree.insert("", END, values=(manager[0], manager[1], manager[2], manager[3], manager[4], manager[5]))

        # Apply the "my_font" tag to all items in the treeview
        for manager in tree.get_children():
            tree.item(manager, tags=("my_font",))

        conn.close()

        # Buttons for CRUD operations

        add_button = Button(content_frame, text="ADD MANAGER", command=add_managers, bg="#f39c12", fg="white", font=("Cooper Black", 12))
        add_button.pack(side=LEFT, padx=35, pady=10)

        edit_button = Button(content_frame, text="EDIT MANAGER", command=edit_managers, bg="#3498db", fg="white", font=("Cooper Black", 12))
        edit_button.pack(side=LEFT, padx=325, pady=10)

        delete_button = Button(content_frame, text="DELETE MANAGER", command=delete_managers, bg="#e74c3c", fg="white", font=("Cooper Black", 12))
        delete_button.pack(side=LEFT, padx=35, pady=10)

        fms.scr.mainloop()
    
#-- View All Users Page ---
    
    def Viewusers(fms):

        fms.scr.destroy()
        fms.scr = Tk()

        # getting screen width and height of display
        width= fms.scr.winfo_screenwidth() 
        height= fms.scr.winfo_screenheight()
        
        #setting tkinter window size
        fms.scr.geometry("%dx%d" % (width, height))
        
        fms.scr.title("FOOD MANAGEMENT SYSTEM")
        
        fms.managerdashf1= Frame(fms.scr, bg="#ffffff")

        fms.logo = PhotoImage(file="logo.png")
        fms.logo_img1 = fms.logo.subsample(2,2)
        
        fms.logo_banner1 = Label(fms.managerdashf1, image=fms.logo_img1)
        fms.logo_banner1.pack(side=LEFT)  

        fms.managerlabel= Label(text="Weclome to Admin Dashboard!!", bg="#0b1335", fg="white",font=("cooper black",14))
        fms.managerlabel.place(x=1000,y=50)

        fms.logout=Button(fms.managerdashf1,text="LOGOUT", command=fms.main, bg="#0b1335",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.logout.place(x=1075,y=100)

        # code to display the local time
        fms.localtime=time.asctime(time.localtime(time.time()))
        fms.tim=Label(fms.managerdashf1,text=fms.localtime,fg="white",font=("cooper black",14),bg="#0b1335")
        fms.managerdashf1.pack(fill=BOTH)

        fms.sidebar = Frame(fms.scr, bg="#d3ede6")
        fms.sidebar.pack(side=LEFT, fill=Y) 
        
        # Add buttons to the sidebar

        fms.viewmanagers= Button(fms.sidebar,text="VIEW MANAGERS", command=fms.Viewmanagers, bg="#0b1335",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.viewmanagers.grid(row=3, column=0, ipadx=11, padx=25, pady=25)

        fms.viewusers= Button(fms.sidebar,text="VIEW USERS", command=fms.Viewusers, bg="#f39c12",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.viewusers.grid(row=5, column=0, ipadx=36, padx=25, pady=25)


        fms.viewdonations= Button(fms.sidebar,text="VIEW DONATIONS", command=fms.Viewdonations, bg="#0b1335",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.viewdonations.grid(row=6, column=0, ipadx=8, padx=25, pady=25)


        fms.viewreports = Button(fms.sidebar,text="REPORTS", command=fms.Viewreports, bg="#0b1335",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.viewreports.grid(row=7, column=0, ipadx=53, padx=25, pady=25)

        # Create the main content frame
        content_frame = Frame(fms.scr, bg="lightgray")
        content_frame.pack(side=LEFT, fill=BOTH, expand=True)

        # Create a label for the title
        title_label = Label(content_frame, text="VIEW USERS", font=("Cooper Black", 16), bg="#0b1335", fg="white", pady=10)
        title_label.pack(fill=X)
        title_label.pack(pady=(0, 85))

        # Create treeview
        tree = ttk.Treeview(content_frame, columns=("User ID", "First Name", "Last Name", "User Name", "Email", "Mobile No"), show="headings", padding=(0, 5))

        # Set the font for the headings
        tree.heading("User ID", text="User ID", anchor=CENTER)
        tree.heading("First Name", text="First Name", anchor=CENTER)
        tree.heading("Last Name", text="Last Name", anchor=CENTER)
        tree.heading("User Name", text="User Name", anchor=CENTER)
        tree.heading("Email", text="Email", anchor=CENTER)
        tree.heading("Mobile No", text="Mobile No", anchor=CENTER)
   
        # Configure Treeview style
        style = ttk.Style()
        style.configure("Custom.Treeview", font=("Cooper Black", 12))
        style.configure("Treeview.Row", padding=(0, 5))

        # Set the background color for the headers
        style.configure("Treeview.Heading", background="gray")

        # Define a tag named "my_font" with the desired font
        tree.tag_configure("my_font", font=("Cooper Black", 12))
        tree.pack()

        # Connect to the SQLite3 database
        conn = connect('fms.db')
        cursor = conn.cursor()

        # Fetch and display data
        cursor.execute("SELECT user_id, first_name, last_name, user_name, email, mobile_no FROM users")
        users = cursor.fetchall()

        for user in users:

            tree.insert("", END, values=(user[0], user[1], user[2], user[3], user[4], user[5]))

        # Apply the "my_font" tag to all items in the treeview
        for user in tree.get_children():
            tree.item(user, tags=("my_font",))

        conn.close()
        fms.scr.mainloop()
        
#-- View All Donations Page ---
    
    def Viewdonations(fms):

        fms.scr.destroy()
        fms.scr = Tk()

        # getting screen width and height of display
        width= fms.scr.winfo_screenwidth() 
        height= fms.scr.winfo_screenheight()
        
        #setting tkinter window size
        fms.scr.geometry("%dx%d" % (width, height))
        
        fms.scr.title("FOOD MANAGEMENT SYSTEM")
        
        fms.managerdashf1= Frame(fms.scr, bg="#ffffff")

        fms.logo = PhotoImage(file="logo.png")
        fms.logo_img1 = fms.logo.subsample(2,2)
        
        fms.logo_banner1 = Label(fms.managerdashf1, image=fms.logo_img1)
        fms.logo_banner1.pack(side=LEFT)  

        fms.managerlabel= Label(text="Weclome to Admin Dashboard!!", bg="#0b1335", fg="white",font=("cooper black",14))
        fms.managerlabel.place(x=1000,y=50)

        fms.logout=Button(fms.managerdashf1,text="LOGOUT", command=fms.main, bg="#0b1335",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.logout.place(x=1075,y=100)

        # code to display the local time
        fms.localtime=time.asctime(time.localtime(time.time()))
        fms.tim=Label(fms.managerdashf1,text=fms.localtime,fg="white",font=("cooper black",14),bg="#0b1335")
        fms.managerdashf1.pack(fill=BOTH)

        fms.sidebar = Frame(fms.scr, bg="#d3ede6")
        fms.sidebar.pack(side=LEFT, fill=Y) 
        
        # Add buttons to the sidebar

        fms.viewmanagers= Button(fms.sidebar,text="VIEW MANAGERS", command=fms.Viewmanagers, bg="#0b1335",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.viewmanagers.grid(row=3, column=0, ipadx=11, padx=25, pady=25)

        fms.viewusers= Button(fms.sidebar,text="VIEW USERS", command=fms.Viewusers, bg="#0b1335",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.viewusers.grid(row=5, column=0, ipadx=36, padx=25, pady=25)

        fms.viewdonations= Button(fms.sidebar,text="VIEW DONATIONS", command=fms.Viewdonations, bg="#f39c12",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.viewdonations.grid(row=6, column=0, ipadx=8, padx=25, pady=25)

        fms.viewreports = Button(fms.sidebar,text="REPORTS", command=fms.Viewreports, bg="#0b1335",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.viewreports.grid(row=7, column=0, ipadx=53, padx=25, pady=25)

        # Create the main content frame
        content_frame = Frame(fms.scr, bg="lightgray")
        content_frame.pack(side=LEFT, fill=BOTH, expand=True)

        # Create a label for the title
        title_label = Label(content_frame, text="VIEW DONATIONS", font=("Cooper Black", 16), bg="#0b1335", fg="white", pady=10)
        title_label.pack(fill=X)
        title_label.pack(pady=(0, 85))

        # Create treeview
        tree = ttk.Treeview(content_frame, columns=("Donation ID",  "Item Name", "Item Type", "Calories", "Amount(Lbs)", "Servings", "Added By", "Status", "Accepted By"), show="headings", padding=(0, 5))     
    
        # Set the font for the headings
        tree.heading("Donation ID", text="Donation ID", anchor=CENTER)
        tree.heading("Item Name", text="Item Name", anchor=CENTER)
        tree.heading("Item Type", text="Item Type", anchor=CENTER)
        tree.heading("Calories", text="Calories", anchor=CENTER)
        tree.heading("Amount(Lbs)", text="Amount(Lbs)", anchor=CENTER)
        tree.heading("Servings", text="Servings", anchor=CENTER)
        tree.heading("Added By", text="Added By", anchor=CENTER)
        tree.heading("Status", text="Status", anchor=CENTER)
        tree.heading("Accepted By", text="Accepted By", anchor=CENTER)

        # Configure Treeview style
        style = ttk.Style()
        style.configure("Custom.Treeview", font=("Cooper Black", 12))
        style.configure("Treeview.Row", padding=(0, 5))

        # Set the background color for the headers
        style.configure("Treeview.Heading", background="gray")

        # Define a tag named "my_font" with the desired font
        tree.tag_configure("my_font", font=("Cooper Black", 12))
        
        # Set the column widths
        tree.column("Donation ID", width=135)
        tree.column("Item Name", width=135)
        tree.column("Item Type", width=135)
        tree.column("Calories", width=135)
        tree.column("Amount(Lbs)", width=135)
        tree.column("Servings", width=135)
        tree.column("Added By", width=135)
        tree.column("Status", width=135)
        tree.column("Accepted By", width=135)

        tree.pack()

       # Connect to the SQLite3 database
        conn = connect('fms.db')
        cursor = conn.cursor()

        # Fetch and display data
        cursor.execute("SELECT donation_id, item_name, item_type, calories, amount_lb, servings, manager_id, donation_status, user_id FROM donation_details")
        donations = cursor.fetchall()
        
        for donation in donations:
            
            # Fetch the manager's user_name from the managers table
            cursor.execute("SELECT user_name FROM managers WHERE manager_id=?", (donation[6],))
            manager_result = cursor.fetchone()
            manager_name = manager_result[0] if manager_result else None  # Assuming manager_id is at index 7

            # Fetch the user's user_name from the users table
            cursor.execute("SELECT user_name FROM users WHERE user_id=?", (donation[8],))
            user_result = cursor.fetchone()
            user_name = user_result[0] if user_result else None  # Assuming user_id is at index 9

            tree.insert("", END, values=(donation[0], donation[1], donation[2], donation[3], donation[4], donation[5], manager_name, donation[7], user_name))

        # Apply the "my_font" tag to all items in the treeview
        for donation in tree.get_children():
            tree.item(donation, tags=("my_font",))

        conn.close()
        fms.scr.mainloop()

#-- View All Reports Page ------
    
    def Viewreports(fms):
        
        fms.scr.destroy()
        fms.scr = Tk()
        
        # getting screen width and height of display
        width= fms.scr.winfo_screenwidth() 
        height= fms.scr.winfo_screenheight()
        
        #setting tkinter window size
        fms.scr.geometry("%dx%d" % (width, height))
        
        fms.scr.title("FOOD MANAGEMENT SYSTEM")
        
        fms.admindashf1= Frame(fms.scr, bg="#ffffff")

        fms.logo = PhotoImage(file="logo.png")
        fms.logo_img1 = fms.logo.subsample(2,2)
        
        fms.logo_banner1 = Label(fms.admindashf1, image=fms.logo_img1)
        fms.logo_banner1.pack(side=LEFT)  

        fms.adminlabel= Label(text="Weclome to Admin Dashboard!!", bg="#0b1335", fg="white",font=("cooper black",14))
        fms.adminlabel.place(x=1000,y=50)

        fms.logout=Button(fms.admindashf1,text="LOGOUT", command=fms.main, bg="#0b1335",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.logout.place(x=1075,y=100)

        # code to display the local time
        fms.localtime=time.asctime(time.localtime(time.time()))
        fms.tim=Label(fms.admindashf1,text=fms.localtime,fg="white",font=("cooper black",14),bg="#0b1335")
        fms.admindashf1.pack(fill=BOTH)

        fms.sidebar = Frame(fms.scr, bg="#d3ede6")
        fms.sidebar.pack(side=LEFT, fill=Y) 
        
        # Add buttons to the sidebar
        
        fms.viewmanagers= Button(fms.sidebar,text="VIEW MANAGERS", command=fms.Viewmanagers, bg="#0b1335",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.viewmanagers.grid(row=3, column=0, ipadx=11, padx=25, pady=25)

        fms.viewusers= Button(fms.sidebar,text="VIEW USERS", command=fms.Viewusers, bg="#0b1335",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.viewusers.grid(row=5, column=0, ipadx=36, padx=25, pady=25)

        fms.viewdonations= Button(fms.sidebar,text="VIEW DONATIONS", command=fms.Viewdonations, bg="#0b1335",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.viewdonations.grid(row=6, column=0, ipadx=8, padx=25, pady=25)

        fms.viewreports = Button(fms.sidebar,text="REPORTS", command=fms.Viewreports, bg="#f39c12",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.viewreports.grid(row=7, column=0, ipadx=53, padx=25, pady=25)

        def show_custom_messages(message):
            # Create a new top-level window
            message_dialog = Toplevel()
            message_dialog.title("Message")
            
            # Set window size and position it in the center of the screen
            window_width = 450
            window_height = 150
            screen_width = message_dialog.winfo_screenwidth()
            screen_height = message_dialog.winfo_screenheight()
            x = (screen_width - window_width) // 2
            y = (screen_height - window_height) // 2
            message_dialog.geometry(f"{window_width}x{window_height}+{x}+{y}")
            
            # Add an icon label in #32CD32 color
            style = ttk.Style()
            style.configure("Error.TLabel", foreground="#32CD32")
            error_icon = ttk.Label(message_dialog, text="\u24D8", style="Error.TLabel", font=("Cooper Black", 24))
            error_icon.pack(pady=10)

            label = Label(message_dialog, text=message, fg="#32CD32", font=("Cooper Black", 12))
            label.pack(padx=10, pady=0)

            # Add an "OK" button to close the dialog
            ok_button = Button(message_dialog, text="OK", command=message_dialog.destroy, width=10, font=("Cooper Black", 12))
            ok_button.pack(pady=10)

        def export_to_pdf(data):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=8)

            # Add table headers
            headers = ["Donation ID",  "Item Name", "Item Type", "Calories", "Amount (lb)", "Servings", "Donation Status"]
            col_width = 24.5
            row_height = 5
            for header in headers:
                pdf.cell(col_width, row_height, header, 1, 0, 'C')
            pdf.ln()

            # Add table data
            for item in data:
                # Extract item values and add them to the PDF
                item_values = tree.item(item, "values")
                for value in item_values:
                    pdf.cell(col_width, row_height, str(value), 1, 0, 'C')
                pdf.ln()

            # Specify the file path for the PDF
            pdf_file_path = "C:/Users/navee/Downloads/git-prjcts/fms/donations_report.pdf"
            pdf.output(pdf_file_path)

            # Show custom message after successful export
            show_custom_messages("Donations PDF file exported successfully.")

        def export_to_excel(data):
            values = []
            for item in data:
                item_values = tree.item(item, "values")
                values.append([item_values[i] for i in range(len(item_values))])  # Convert tuple to list

            # Define column names
            columns = ["Donation ID", "Item Name", "Item Type", "Calories", "Amount (lb)", "Servings", "Donation Status"]

            # Create DataFrame
            df = pd.DataFrame(values, columns=columns)

            # Specify the full path where you want to save the file
            file_path = "C:/Users/navee/Downloads/git-prjcts/fms/donations_report.xlsx"

            # Export to Excel
            try:
            
                df.to_excel(file_path, index=False)
                print("Excel file exported successfully.")
                # Show custom message after successful export
                show_custom_messages("Donations Excel file exported successfully.")
            
            except Exception as e:
                print(f"Error exporting Excel file: {e}")

        def fetch_and_display_data():
            conn = connect('fms.db')
            cursor = conn.cursor()

            cursor.execute("SELECT donation_id, item_name, item_type, calories, amount_lb, servings, donation_status FROM donation_details")
            donations = cursor.fetchall()

            for donation in donations:
                tree.insert("", END, values=(donation[0], donation[1], donation[2], donation[3], donation[4], donation[5], donation[6]))

            for donation in tree.get_children():
                tree.item(donation, tags=("my_font",))

            conn.close()

        # Create the main content frame
        # fms = Tk()
        # fms.scr = Toplevel()
        # Create the main content frame
        content_frame = Frame(fms.scr, bg="lightgray")
        content_frame.pack(side=LEFT, fill=BOTH, expand=True)

        # Create a label for the title
        title_label = Label(content_frame, text="REPORTS", font=("Cooper Black", 16), bg="#0b1335", fg="white", pady=10)
        title_label.pack(fill=X)
        title_label.pack(pady=(0, 85))

        # Your Treeview widget declaration goes here
        tree = ttk.Treeview()
        # Define tree columns
        tree["columns"] = ("Donation ID",  "Item Name", "Item Type", "Calories", "Amount (lb)", "Servings", "Donation Status")
        # Set column headings
        for column in tree["columns"]:
            tree.heading(column, text=column)

        # Fetch and display data
        fetch_and_display_data()

        # Create PDF export button
        pdf_button = Button(content_frame, text="EXPORT DONATIONS to PDF", command=lambda: export_to_pdf(tree.get_children()), bg="#f39c12", fg="white", font=("Cooper Black", 14))
        pdf_button.pack(side=LEFT, padx=(275, 25), pady=0, anchor="center")

        # Create Excel export button
        excel_button = Button(content_frame, text="EXPORT DONATIONS to EXCEL", command=lambda: export_to_excel(tree.get_children()), bg="#3498db", fg="white", font=("Cooper Black", 14))
        excel_button.pack(side=LEFT, padx=(25, 100), pady=0, anchor="center")

     
        fms.scr.mainloop()

#-------------------------------------------------- Admin Dashboard Code End ---------------------------------------------------------------------#    

#-------------------------------------------------- Manager Dashboard Code Start -----------------------------------------------------------------#    

#-- Manager Main Page ------
    
    def Managerdetails(fms, manager_id):

        fms.scr.destroy()
        fms.scr = Tk()
        
        # getting screen width and height of display
        width= fms.scr.winfo_screenwidth() 
        height= fms.scr.winfo_screenheight()
        
        #setting tkinter window size
        fms.scr.geometry("%dx%d" % (width, height))
        
        fms.scr.title("FOOD MANAGEMENT SYSTEM")
        
        fms.managerdashf1= Frame(fms.scr, bg="#ffffff")

        fms.logo = PhotoImage(file="logo.png")
        fms.logo_img1 = fms.logo.subsample(2,2)
        
        fms.logo_banner1 = Label(fms.managerdashf1, image=fms.logo_img1)
        fms.logo_banner1.pack(side=LEFT)  

        fms.managerlabel= Label(text="Weclome to Manager Dashboard!!", bg="#0b1335", fg="white",font=("cooper black",14))
        fms.managerlabel.place(x=1000,y=50)

        fms.logout=Button(fms.managerdashf1,text="LOGOUT", command=fms.main, bg="#0b1335",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.logout.place(x=1075,y=100)


        # code to display the local time
        fms.localtime=time.asctime(time.localtime(time.time()))
        fms.tim=Label(fms.managerdashf1,text=fms.localtime,fg="white",font=("cooper black",14),bg="#0b1335")
        fms.managerdashf1.pack(fill=BOTH)

        fms.sidebar = Frame(fms.scr, bg="#d3ede6")
        fms.sidebar.pack(side=LEFT, fill=Y) 

        fms.profilepage = Button(fms.sidebar,text="VIEW PROFILE", command=lambda:fms.Managerdetails(manager_id), bg="#f39c12",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.profilepage.grid(row=2, column=0, ipadx=25, padx=25, pady=25)
        # fms.viewdonations.pack(padx=50, pady = 25)

        fms.viewdonations= Button(fms.sidebar,text="VIEW DONATIONS", command=lambda:fms.Mviewdonations(manager_id), bg="#0b1335",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.viewdonations.grid(row=3, column=0, ipadx=8, padx=25, pady=25)
        # fms.viewdonations.pack(padx=50, pady = 25)
        
        def show_custom_messages(message):
            # Create a new top-level window
            message_dialog = Toplevel()
            message_dialog.title("Message")
            
            # Set window size and position it in the center of the screen
            window_width = 350
            window_height = 150
            screen_width = message_dialog.winfo_screenwidth()
            screen_height = message_dialog.winfo_screenheight()
            x = (screen_width - window_width) // 2
            y = (screen_height - window_height) // 2
            message_dialog.geometry(f"{window_width}x{window_height}+{x}+{y}")
            
            # Add an icon label in #32CD32 color
            style = ttk.Style()
            style.configure("Error.TLabel", foreground="#32CD32")
            error_icon = ttk.Label(message_dialog, text="\u24D8", style="Error.TLabel", font=("Cooper Black", 24))
            error_icon.pack(pady=10)

            label = Label(message_dialog, text=message, fg="#32CD32", font=("Cooper Black", 12))
            label.pack(padx=10, pady=0)

            # Add an "OK" button to close the dialog
            ok_button = Button(message_dialog, text="OK", command=message_dialog.destroy, width=10, font=("Cooper Black", 12))
            ok_button.pack(pady=10)

        def show_custom_error(message):
            # Create a new top-level window
            error_dialog = Toplevel()
            error_dialog.title("Error Message")
            
            # Set window size and position it in the center of the screen
            window_width = 650
            window_height = 150
            screen_width = error_dialog.winfo_screenwidth()
            screen_height = error_dialog.winfo_screenheight()
            x = (screen_width - window_width) // 2
            y = (screen_height - window_height) // 2
            error_dialog.geometry(f"{window_width}x{window_height}+{x}+{y}")

            # Add an icon label in red color
            style = ttk.Style()
            style.configure("Error.TLabel", foreground="red")
            error_icon = ttk.Label(error_dialog, text="\u26A0", style="Error.TLabel", font=("Cooper Black", 24))
            error_icon.pack(pady=10)

            label = Label(error_dialog, text=message, fg="red", font=("Cooper Black", 12))
            label.pack(padx=10, pady=0)
            
            # Add an "OK" button to close the dialog
            ok_button = Button(error_dialog, text="OK", command=error_dialog.destroy, width=10, font=("Cooper Black", 12))
            ok_button.pack(pady=10)

        # Function to load data into the Treeview
        def manager_data():
            # Clear the existing data in the Treeview
            tree.delete(*tree.get_children())

            # Connect to the database
            conn = connect('fms.db')
            cursor = conn.cursor()

            # Retrieve the manager's data from the database
            cursor.execute("SELECT manager_id, first_name, last_name, user_name, department, email FROM managers WHERE manager_id = ?", (manager_id,))
            manager = cursor.fetchone()

            if manager:
                # Insert the data into the Treeview
                tree.insert("", END, values=(manager[0], manager[1], manager[2], manager[3], manager[4], manager[5]), tags=("my_font"))

            # Close the connection
            conn.close()

        # Function to edit a manager's details
        def edit_manager():
            # Get the selected item from the Treeview
            selected_item = tree.focus()
            
            if not selected_item:
                show_custom_error("Please select manager to edit")
                return

            # Get the values of the selected record
            values = tree.item(selected_item, "values")
            manager_id = values[0]
    
            def submit():
                # Get values from entry widgets
                first_name = first_name_entry.get()
                last_name = last_name_entry.get()
                user_name = user_name_entry.get()
                department = selected_department.get()
                email = email_entry.get()

                # Validate fields
                if not (first_name and last_name and user_name and department and email):
                    show_custom_error("All fields are required")
                    return

                # Validate email format
                if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
                    show_custom_error("Invalid email format")
                    return

                # Connect to the database
                conn = connect('fms.db')
                cursor = conn.cursor()

                try:
                    # Check if the user_name or email already exists for other managers
                    cursor.execute("SELECT COUNT(*) FROM managers WHERE (user_name=? OR email=?) AND manager_id != ?", (user_name, email, manager_id))
                    existing_managers_count = cursor.fetchone()[0]

                    if existing_managers_count > 0:
                        # User_name or email already exists for other managers, show error message
                        show_custom_error("User name or email already exists. Please choose a different one.")
                    else:
                        # Proceed with updating the manager details
                        # Print the SQL query to verify correctness
                        print(f"Executing EDIT query: EDIT FROM managers WHERE manager_id = {manager_id}")

                        # Update manager in the managers table
                        cursor.execute("UPDATE managers SET first_name=?, last_name=?, user_name=?, department=?, email=? WHERE manager_id=?",
                                    (first_name, last_name, user_name, department, email, manager_id))

                        # Commit the changes
                        conn.commit()

                        # Show success message
                        show_custom_messages("Manager details updated successfully")

                        # Refresh the Treeview
                        manager_data()

                except Exception as e:
                    # Show error message if update fails
                    show_custom_error(f"Failed to update the manager details: {str(e)}")

                finally:
                    # Close the connection
                    conn.close()
                    # Close the edit window
                    edit_window.destroy()

            # Create a Toplevel window for editing a manager
            edit_window = Toplevel()
            edit_window.title("Edit Profile")

            # Calculate the center coordinates of the screen
            screen_width = edit_window.winfo_screenwidth()
            screen_height = edit_window.winfo_screenheight()
            window_width = 700
            window_height = 225
            x = (screen_width - window_width) // 2
            y = (screen_height - window_height) // 2

            # Set the geometry of the window to be centered and larger
            edit_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

            # Create labels and entry widgets for each field
            Label(edit_window, text="First Name:", font=("Cooper Black", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
            first_name_entry = Entry(edit_window, font=("Cooper Black", 12))
            first_name_entry.grid(row=0, column=1, padx=10, pady=10)

            Label(edit_window, text="Last Name:", font=("Cooper Black", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
            last_name_entry = Entry(edit_window, font=("Cooper Black", 12))
            last_name_entry.grid(row=1, column=1, padx=10, pady=10)

            Label(edit_window, text="User Name:", font=("Cooper Black", 12)).grid(row=0, column=2, padx=10, pady=10, sticky="e")
            user_name_entry = Entry(edit_window, font=("Cooper Black", 12))
            user_name_entry.grid(row=0, column=3, padx=10, pady=10)
            # user_name_entry.insert(0, values[3])  # Insert the user_name from the selected record

            Label(edit_window, text="Email:", font=("Cooper Black", 12)).grid(row=3, column=0, padx=10, pady=10, sticky="e")
            email_entry = Entry(edit_window, font=("Cooper Black", 12))
            email_entry.grid(row=3, column=1, padx=10, pady=10)
            # email_entry.insert(0, values[5])  # Insert the email from the selected record

            Label(edit_window, text="Department:", font=("Cooper Black", 12)).grid(row=1, column=2, padx=10, pady=10, sticky="e")
            department_options = ["One Central", "Eatry", "Merill", "Dine and Connect", "Catering"]
            selected_department = StringVar(edit_window)
            selected_department.set(department_options[0])
            department_dropdown = OptionMenu(edit_window, selected_department, *department_options)
            department_dropdown.config(font=("Cooper Black", 12))
            department_dropdown.grid(row=1, column=3, padx=10, pady=10, sticky="w")

            # Populate the entry widgets with the selected manager's data
            first_name_entry.insert(0, values[1])
            last_name_entry.insert(0, values[2])
            user_name_entry.insert(0, values[3])
            selected_department.set(values[4])
            email_entry.insert(0, values[5])

            # Create a Submit button
            submit_button = Button(edit_window, text="Submit", command=submit, font=("Cooper Black", 12))
            submit_button.grid(row=4, columnspan=4, pady=10)

            # Main loop for the edit window
            edit_window.mainloop()

        # Create the main content frame
        content_frame = Frame(fms.scr, bg="lightgray")
        content_frame.pack(side=LEFT, fill=BOTH, expand=True)

        # Create a label for the title
        title_label = Label(content_frame, text="VIEW PROFILE", font=("Cooper Black", 16), bg="#0b1335", fg="white", pady=10)
        title_label.pack(fill=X)
        title_label.pack(pady=(0, 85))    

        # Create treeview
        tree = ttk.Treeview(content_frame, columns=("Manager ID", "First Name", "Last Name", "User Name", "Department", "Email"), show="headings", padding=(0, 5))

        # Set the font for the headings
        tree.heading("Manager ID", text="Manager ID", anchor=CENTER)
        tree.heading("First Name", text="First Name", anchor=CENTER)
        tree.heading("Last Name", text="Last Name", anchor=CENTER)
        tree.heading("User Name", text="User Name", anchor=CENTER)
        tree.heading("Department", text="Department", anchor=CENTER)
        tree.heading("Email", text="Email", anchor=CENTER)

        # Configure Treeview style
        style = ttk.Style()
        style.configure("Custom.Treeview", font=("Cooper Black", 12))
        style.configure("Treeview.Row", padding=(0, 5))

        # Set the background color for the headers
        style.configure("Treeview.Heading", background="gray")

        # Define a tag named "my_font" with the desired font
        tree.tag_configure("my_font", font=("Cooper Black", 12))
        tree.pack()

        # Connect to the SQLite3 database
        conn = connect('fms.db')
        cursor = conn.cursor()

        # Retrieve the manager's data from the database
        cursor.execute("SELECT manager_id, first_name, last_name, user_name, department, email FROM managers WHERE manager_id = ?", (manager_id,))
        manager = cursor.fetchone()

        if manager:
           # Insert the manager's data into the Treeview
           tree.insert("", END, values=(manager[0], manager[1], manager[2], manager[3], manager[4], manager[5]))

        # Apply the "my_font" tag to all items in the treeview
        for manager in tree.get_children():
            tree.item(manager, tags=("my_font",))

        edit_button = Button(content_frame, text="EDIT PROFILE", command=edit_manager, bg="#3498db", fg="white", font=("Cooper Black", 12))
        edit_button.pack(side=LEFT, padx=500, pady=10)

        fms.scr.mainloop()

#--- Manager view donations Page -----
    
    def Mviewdonations(fms, manager_id):

        fms.scr.destroy()
        fms.scr = Tk()
        
        # getting screen width and height of display
        width= fms.scr.winfo_screenwidth() 
        height= fms.scr.winfo_screenheight()
        
        #setting tkinter window size
        fms.scr.geometry("%dx%d" % (width, height))
        
        fms.scr.title("FOOD MANAGEMENT SYSTEM")
        
        fms.managerdashf1= Frame(fms.scr, bg="#ffffff")

        fms.logo = PhotoImage(file="logo.png")
        fms.logo_img1 = fms.logo.subsample(2,2)
        
        fms.logo_banner1 = Label(fms.managerdashf1, image=fms.logo_img1)
        fms.logo_banner1.pack(side=LEFT)  

        fms.managerlabel= Label(text="Weclome to Manager Dashboard!!", bg="#0b1335", fg="white",font=("cooper black",14))
        fms.managerlabel.place(x=1000,y=50)

        fms.logout=Button(fms.managerdashf1,text="LOGOUT", command=fms.main, bg="#0b1335",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.logout.place(x=1075,y=100)
    
        # code to display the local time
        fms.localtime=time.asctime(time.localtime(time.time()))
        fms.tim=Label(fms.managerdashf1,text=fms.localtime,fg="white",font=("cooper black",14),bg="#0b1335")
        fms.managerdashf1.pack(fill=BOTH)

        fms.sidebar = Frame(fms.scr, bg="#d3ede6")
        fms.sidebar.pack(side=LEFT, fill=Y) 
        
        # Add buttons to the sidebar

        fms.profilepage = Button(fms.sidebar,text="VIEW PROFILE", command=lambda:fms.Managerdetails(manager_id), bg="#0b1335",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.profilepage.grid(row=2, column=0, ipadx=25, padx=25, pady=25)
        
        fms.viewdonations= Button(fms.sidebar,text="VIEW DONATIONS", command=lambda:fms.Mviewdonations(manager_id), bg="#f39c12",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.viewdonations.grid(row=3, column=0, ipadx=8, padx=25, pady=25)

        def show_custom_messages(message):
            # Create a new top-level window
            message_dialog = Toplevel()
            message_dialog.title("Message")
            
            # Set window size and position it in the center of the screen
            window_width = 350
            window_height = 150
            screen_width = message_dialog.winfo_screenwidth()
            screen_height = message_dialog.winfo_screenheight()
            x = (screen_width - window_width) // 2
            y = (screen_height - window_height) // 2
            message_dialog.geometry(f"{window_width}x{window_height}+{x}+{y}")
            
            # Add an icon label in #32CD32 color
            style = ttk.Style()
            style.configure("Error.TLabel", foreground="#32CD32")
            error_icon = ttk.Label(message_dialog, text="\u24D8", style="Error.TLabel", font=("Cooper Black", 24))
            error_icon.pack(pady=10)

            label = Label(message_dialog, text=message, fg="#32CD32", font=("Cooper Black", 12))
            label.pack(padx=10, pady=0)

            # Add an "OK" button to close the dialog
            ok_button = Button(message_dialog, text="OK", command=message_dialog.destroy, width=10, font=("Cooper Black", 12))
            ok_button.pack(pady=10)

        def show_custom_error(message):
            # Create a new top-level window
            error_dialog = Toplevel()
            error_dialog.title("Error Message")
            
            # Set window size and position it in the center of the screen
            window_width = 650
            window_height = 150
            screen_width = error_dialog.winfo_screenwidth()
            screen_height = error_dialog.winfo_screenheight()
            x = (screen_width - window_width) // 2
            y = (screen_height - window_height) // 2
            error_dialog.geometry(f"{window_width}x{window_height}+{x}+{y}")

            # Add an icon label in red color
            style = ttk.Style()
            style.configure("Error.TLabel", foreground="red")
            error_icon = ttk.Label(error_dialog, text="\u26A0", style="Error.TLabel", font=("Cooper Black", 24))
            error_icon.pack(pady=10)

            label = Label(error_dialog, text=message, fg="red", font=("Cooper Black", 12))
            label.pack(padx=10, pady=0)
            
            # Add an "OK" button to close the dialog
            ok_button = Button(error_dialog, text="OK", command=error_dialog.destroy, width=10, font=("Cooper Black", 12))
            ok_button.pack(pady=10)
        
        # Function to load data into the Treeview
        
        def donation_data():

            #Clear the existing data in the Treeview
            tree.delete(*tree.get_children())

            # Connect to the database
            conn = connect('fms.db')
            cursor = conn.cursor()

            # Retrieve the donation data from the database
            cursor.execute("SELECT donation_id, item_name, item_type, calories, amount_lb, servings, manager_id, donation_status, user_id FROM donation_details WHERE manager_id = ?", (manager_id,))
            donations = cursor.fetchall()

            # Insert the data into the Treeview
            for donation in donations:
                
                # Fetch the manager's user_name from the managers table
                cursor.execute("SELECT user_name FROM managers WHERE manager_id=?", (donation[6],))
                manager_result = cursor.fetchone()
                manager_name = manager_result[0] if manager_result else None  # Assuming manager_id is at index 7

                # Fetch the user's user_name from the users table
                cursor.execute("SELECT user_name FROM users WHERE user_id=?", (donation[8],))
                user_result = cursor.fetchone()
                user_name = user_result[0] if user_result else None  # Assuming user_id is at index 9
                
                # Exclude the manager_id (index 0) and donation_status (index 7) from the display
                tree.insert("", "end", values=(donation[0], donation[1], donation[2], donation[3], donation[4], donation[5], manager_name, donation[7], user_name), tags=("my_font"))

            # Close the connection
            conn.close()

        # Function to send an email notification
        def send_email(recipient, user_name, item_name, item_type, calories, amount_lb, servings):
            # Validate recipient email address
            if not re.match(r"[^@]+@[^@]+\.[^@]+", recipient):
                print(f"Invalid email address: {recipient}")
                return
            
            sender_email = "fms38865@gmail.com"
            sender_password = "ktee vlno ediy uiop"
            subject = "Uploaded Food Donation Updated"
            body = f"Hello {user_name},\n\nA food donation that was previously uploaded has been updated with the following details:\nItem Name: {item_name}\nItem Type: {item_type}\nCalories: {calories}\nAmount (lb): {amount_lb}\nServings: {servings}\n\nCheck it out!\n\nThank you,\nFood Management Team"
            
            # Compose email
            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = recipient
            message['Subject'] = subject
            message.attach(MIMEText(body, 'plain'))

            # Send email
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, recipient, message.as_string())
                server.quit()
                print("Email sent successfully")
            except Exception as e:
                print(f"Failed to send email: {str(e)}") 

        def edit_donation():
            # Get the selected item from the Treeview
            selected_item = tree.focus()
            
            if not selected_item:
                show_custom_error("Please select a donation to edit")
                return

            # Get the values of the selected record
            values = tree.item(selected_item, "values")
            donation_id = values[0]
            donation_status = values[7]  # Assuming donation_status is at index 8

            # Check if the donation has already been accepted
            if donation_status == "accepted":
                show_custom_error("Donation already accepted. You cannot edit it.")
                return

            # Define a function to submit the edited donation details
            def submit():
                # Get values from entry widgets
                # item_no = item_no_entry.get()
                item_name = item_name_entry.get()
                item_type = item_type_entry.get()
                calories = calories_entry.get()
                amount_lb = amount_lb_entry.get()
                servings = servings_entry.get()
                # manager_id = 

                # Validate fields
                if not (item_name and item_type and calories and amount_lb and servings):
                    show_custom_error("All fields are required")
                    return

                # Connect to the database
                conn = connect('fms.db')
                cursor = conn.cursor()

                # Initialize a flag to track whether the update was successful
                update_successful = False

                try:
                    # Validate fields
                    if not ( item_name and item_type and calories and amount_lb and servings):
                        show_custom_error("All fields are required")
                    elif not (calories.isdigit() and amount_lb.isdigit() and servings.isdigit()):
                        show_custom_error("Please enter only digits for Calories, Amount (lb), and Servings.")
                    else:
                        # Update the donation details if donation_status is not "accepted"
                        if donation_status != "accepted":
                            # Print the SQL query to verify correctness
                            print(f"Executing EDIT query: EDIT FROM donation_details WHERE donation_id = {donation_id}")

                            # Update donation details in the donation_details table
                            cursor.execute("UPDATE donation_details SET item_name=?, item_type=?, calories=?, amount_lb=?, servings=? WHERE donation_id=?",
                                        (item_name, item_type, calories, amount_lb, servings, donation_id))

                            # Commit the changes
                            conn.commit()

                            # Set update flag to True
                            update_successful = True

                            # Show success message
                            show_custom_messages("Donation details updated successfully")

                            # Fetch user_name and email from the users table
                            cursor.execute('SELECT user_name, email FROM users')
                            user_data = cursor.fetchall()

                            # Iterate through the result and send emails
                            for user_name, email in user_data: 
                                send_email(email, user_name, item_name, item_type, calories, amount_lb, servings)

                            # Refresh the Treeview
                            donation_data()
                        else:
                            show_custom_error("Donation already accepted. You cannot edit it.")
                                
                except Exception as e:
                    # Show error message if update fails
                    show_custom_error(f"Failed to update the donation details: {str(e)}")

                finally:
                    # Close the connection
                    conn.close()
                    # Close the edit window only if the update was successful
                    if update_successful:
                        edit_window.destroy()

            # Create a Toplevel window for editing a manager
            edit_window = Toplevel()
            edit_window.title("Edit Donation")

            # Calculate the center coordinates of the screen
            screen_width = edit_window.winfo_screenwidth()
            screen_height = edit_window.winfo_screenheight()
            window_width = 725
            window_height = 225
            x = (screen_width - window_width) // 2
            y = (screen_height - window_height) // 2

            # Set the geometry of the window to be centered and larger
            edit_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

            # Create labels and entry widgets for each field
            # Label(edit_window, text="Item No:", font=("Cooper Black", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
            # item_no_entry = Entry(edit_window, font=("Cooper Black", 12))
            # item_no_entry.grid(row=0, column=1, padx=10, pady=10)

            Label(edit_window, text="Item Name:", font=("Cooper Black", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
            item_name_entry = Entry(edit_window, font=("Cooper Black", 12))
            item_name_entry.grid(row=0, column=1, padx=10, pady=10)

            Label(edit_window, text="Item Type:", font=("Cooper Black", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
            item_type_entry = Entry(edit_window, font=("Cooper Black", 12))
            item_type_entry.grid(row=1, column=1, padx=10, pady=10)

            Label(edit_window, text="Calories:", font=("Cooper Black", 12)).grid(row=1, column=2, padx=10, pady=10, sticky="e")
            calories_entry = Entry(edit_window, font=("Cooper Black", 12))
            calories_entry.grid(row=1, column=3, padx=10, pady=10)

            Label(edit_window, text="Amount(Lb):", font=("Cooper Black", 12)).grid(row=0, column=2, padx=10, pady=10, sticky="e")
            amount_lb_entry = Entry(edit_window, font=("Cooper Black", 12))
            amount_lb_entry.grid(row=0, column=3, padx=10, pady=10)

            Label(edit_window, text="Servings:", font=("Cooper Black", 12)).grid(row=2, column=0, padx=10, pady=10, sticky="e")
            servings_entry = Entry(edit_window, font=("Cooper Black", 12))
            servings_entry.grid(row=2, column=1, padx=10, pady=10)

            # Populate the entry widgets with the selected manager's data
            # item_no_entry.insert(0, values[1])
            item_name_entry.insert(0, values[1])
            item_type_entry.insert(0, values[2])
            calories_entry.insert(0, values[3])
            amount_lb_entry.insert(0, values[4])
            servings_entry.insert(0, values[5])
            
            # Create a Submit button
            submit_button = Button(edit_window, text="Submit", command=submit, font=("Cooper Black", 12))
            submit_button.grid(row=4, columnspan=4, pady=10)

            # Main loop for the edit window
            edit_window.mainloop()

        def delete_donation():
            # Get the selected item from the Treeview
            selected_item = tree.focus()
            
            if not selected_item:
                show_custom_error("Please select a donation to delete.")
                return
                
            # Get the values of the selected record
            values = tree.item(selected_item, "values")
            donation_id = values[0]
            donation_status = values[7]  # Assuming donation_status is at index 8

            # Check if the donation has already been accepted
            if donation_status == "accepted":
                show_custom_error("Donation already accepted. You cannot delete it.")
                return

            # Connect to the database
            conn = connect('fms.db')
            cursor = conn.cursor()
            
            try:
                # Print the SQL query to verify correctness
                print(f"Executing DELETE query: DELETE FROM donation_details WHERE donation_id = {donation_id}")

                # Delete the record from the donation_details table
                cursor.execute("DELETE FROM donation_details WHERE donation_id = ?", (donation_id,))
                
                # Commit the changes
                conn.commit()

                # Show success message
                show_custom_messages("Donation deleted successfully")

                # Refresh the Treeview
                donation_data()
            
            except Exception as e:
                # Show error message if deletion fails
                show_custom_error(f"Failed to delete donation: {str(e)}")
            
            finally:
                # Close the connection
                conn.close()
        
        # Function to send an email notification
        def send_mail(recipient, user_name, item_name, item_type, calories, amount_lb, servings):
            
            # Validate recipient email address
            if not re.match(r"[^@]+@[^@]+\.[^@]+", recipient):
                print(f"Invalid email address: {recipient}")
                return
            
            # Email configuration
            sender_email = "fms38865@gmail.com"
            sender_password = "ktee vlno ediy uiop"
            subject = "New Food Donation Uploaded"
            body = f"Hello {user_name},\n\nA new food donation has been added with the following details:\nItem Name: {item_name}\nItem Type: {item_type}\nCalories: {calories}\nAmount (lb): {amount_lb}\nServings: {servings}\n\nCheck it out!\n\nThank you,\nFood Management Team"

            # Compose email
            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = recipient
            message['Subject'] = subject
            message.attach(MIMEText(body, 'plain'))

            # Send email
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, recipient, message.as_string())
                server.quit()
                print("Email sent successfully")
            except Exception as e:
                print(f"Failed to send email: {str(e)}")         
        
        def create_donation_details_table_if_not_exists():
            conn = connect('fms.db')
            cursor = conn.cursor()

            # SQL query to create the table if it does not exist
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS donation_details (
                donation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name TEXT NOT NULL,
                item_type TEXT NOT NULL,
                calories INTEGER NOT NULL,
                amount_lb INTEGER NOT NULL,
                servings INTEGER NOT NULL,
                manager_id INTEGER NOT NULL,
                FOREIGN KEY (manager_id) REFERENCES managers(id)
            );
            '''
            cursor.execute(create_table_query)
            conn.commit()
            conn.close()

        # Function to add a new manager
        def add_donation():
            def submit():
                # Get values from entry widgets
                # item_no = item_no_entry.get()
                item_name = item_name_entry.get()
                item_type = item_type_entry.get()
                calories = calories_entry.get()
                amount_lb = amount_lb_entry.get()
                servings = servings_entry.get()

                # Initialize a flag to track insertion success
                insertion_successful = False

                # Validate fields
                if not ( item_name and item_type and calories and amount_lb and servings):
                    show_custom_error("All fields are required")
                else:
                    try:
                        create_donation_details_table_if_not_exists()  # Check and create table if not exists

                        conn = connect('fms.db')
                        cursor = conn.cursor()

                        # Validate inputs
                        if not ( calories.isdigit() and amount_lb.isdigit() and servings.isdigit()):
                            show_custom_error("Please enter only digits for Calories, Amount (lb), and Servings.")
                        else:
                            # Insert new manager into the managers table
                            cursor.execute("INSERT INTO donation_details (item_name, item_type, calories, amount_lb, servings, manager_id) VALUES (?, ?, ?, ?, ?, ?)",
                                        (item_name, item_type, calories, amount_lb, servings, manager_id))

                            # Commit the changes
                            conn.commit()

                            # Set insertion flag to True
                            insertion_successful = True

                            # Show success message
                            show_custom_messages("Donation added successfully")

                            # Fetch user_name and email from the users table
                            cursor.execute('SELECT user_name, email FROM users')
                            user_data = cursor.fetchall()

                            # Iterate through the result and send emails
                            for user_name, email in user_data: 
                                send_mail(email, user_name, item_name, item_type, calories, amount_lb, servings)

                            # Refresh the Treeview
                            donation_data()

                    except Exception as e:
                        # Show error message if insertion fails
                        show_custom_error(f"Failed to add donation: {e}")

                    finally:
                        # Close the connection
                        conn.close()

                        # Close the add window only if the insertion was successful
                        if insertion_successful:
                            add_window.destroy()
                    
            # Create a Toplevel window for adding a new donation
            add_window = Toplevel()
            add_window.title("Add Donation")

            # Calculate the center coordinates of the screen
            screen_width = add_window.winfo_screenwidth()
            screen_height = add_window.winfo_screenheight()
            window_width = 750
            window_height = 225
            x = (screen_width - window_width) // 2
            y = (screen_height - window_height) // 2

            # Set the geometry of the window to be centered and larger
            add_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

            # Create labels and entry widgets for each field
            # Label(add_window, text="Item No:", font=("Cooper Black", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
            # item_no_entry = Entry(add_window, font=("Cooper Black", 12))
            # item_no_entry.grid(row=0, column=1, padx=10, pady=10)

            Label(add_window, text="Item Name:", font=("Cooper Black", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
            item_name_entry = Entry(add_window, font=("Cooper Black", 12))
            item_name_entry.grid(row=0, column=1, padx=10, pady=10)

            Label(add_window, text="Amount(Lb):", font=("Cooper Black", 12)).grid(row=0, column=2, padx=10, pady=10, sticky="e")
            amount_lb_entry = Entry(add_window, font=("Cooper Black", 12))
            amount_lb_entry.grid(row=0, column=3, padx=10, pady=10)

            Label(add_window, text="Item Type:", font=("Cooper Black", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
            item_type_entry = Entry(add_window, font=("Cooper Black", 12))
            item_type_entry.grid(row=1, column=1, padx=10, pady=10)

            Label(add_window, text="Calories:", font=("Cooper Black", 12)).grid(row=1, column=2, padx=10, pady=10, sticky="e")
            calories_entry = Entry(add_window, font=("Cooper Black", 12))
            calories_entry.grid(row=1, column=3, padx=10, pady=10)

            Label(add_window, text="Servings:", font=("Cooper Black", 12)).grid(row=2, column=0, padx=10, pady=10, sticky="e")
            servings_entry = Entry(add_window, font=("Cooper Black", 12))
            servings_entry.grid(row=2, column=1, padx=10, pady=10)
        
            # Create a Submit button
            submit_button = Button(add_window, text="Submit", command=submit, font=("Cooper Black", 12))
            submit_button.grid(row=3, columnspan=4, pady=10)

            # Main loop for the add window
            add_window.mainloop()

        # Create the main content frame
        content_frame = Frame(fms.scr, bg="lightgray")
        content_frame.pack(side=LEFT, fill=BOTH, expand=True)

        # Create a label for the title
        title_label = Label(content_frame, text="VIEW DONATIONS", font=("Cooper Black", 16), bg="#0b1335", fg="white", pady=10)
        title_label.pack(fill=X)
        title_label.pack(pady=(0, 85))

        # Create treeview
        tree = ttk.Treeview(content_frame, columns=("Donation ID",  "Item Name", "Item Type", "Calories", "Amount(Lbs)", "Servings", "Added By", "Status", "Accepted By"), show="headings", padding=(0, 5))     
    
        # Set the font for the headings
        tree.heading("Donation ID", text="Donation ID", anchor=CENTER)
        
        tree.heading("Item Name", text="Item Name", anchor=CENTER)
        tree.heading("Item Type", text="Item Type", anchor=CENTER)
        tree.heading("Calories", text="Calories", anchor=CENTER)
        tree.heading("Amount(Lbs)", text="Amount(Lbs)", anchor=CENTER)
        tree.heading("Servings", text="Servings", anchor=CENTER)
        tree.heading("Added By", text="Added By", anchor=CENTER)
        tree.heading("Status", text="Status", anchor=CENTER)
        tree.heading("Accepted By", text="Accepted By", anchor=CENTER)
        
        # Configure Treeview style
        style = ttk.Style()
        style.configure("Custom.Treeview", font=("Cooper Black", 12))
        style.configure("Treeview.Row", padding=(0, 5))

        # Set the background color for the headers
        style.configure("Treeview.Heading", background="gray")

        # Define a tag named "my_font" with the desired font
        tree.tag_configure("my_font", font=("Cooper Black", 12))

        # Set the column widths
        tree.column("Donation ID", width=135)
        
        tree.column("Item Name", width=135)
        tree.column("Item Type", width=135)
        tree.column("Calories", width=135)
        tree.column("Amount(Lbs)", width=135)
        tree.column("Servings", width=135)
        tree.column("Added By", width=135)
        tree.column("Status", width=135)
        tree.column("Accepted By", width=135)
        
        tree.pack()

        # Connect to the SQLite3 database
        conn = connect('fms.db')
        cursor = conn.cursor()
        
       # Fetch and display data
        cursor.execute("SELECT donation_id, item_name, item_type, calories, amount_lb, servings, manager_id, donation_status, user_id FROM donation_details WHERE manager_id = ?", (manager_id,))
        donations = cursor.fetchall()
        
        for donation in donations:
            
            # Fetch the manager's user_name from the managers table
            cursor.execute("SELECT user_name FROM managers WHERE manager_id=?", (donation[6],))
            manager_result = cursor.fetchone()
            manager_name = manager_result[0] if manager_result else None  # Assuming manager_id is at index 6

            # Fetch the user's user_name from the users table
            cursor.execute("SELECT user_name FROM users WHERE user_id=?", (donation[8],))
            user_result = cursor.fetchone()
            user_name = user_result[0] if user_result else None  # Assuming user_id is at index 8

            tree.insert("", END, values=(donation[0], donation[1], donation[2], donation[3], donation[4], donation[5], manager_name, donation[7], user_name))

        # Apply the "my_font" tag to all items in the treeview
        for donation in tree.get_children():
            tree.item(donation, tags=("my_font",))
        # Buttons for CRUD operations

        add_button = Button(content_frame, text="ADD DONATION", command=add_donation, bg="#f39c12", fg="white", font=("Cooper Black", 12))
        add_button.pack(side=LEFT, padx=30, pady=10)

        edit_button = Button(content_frame, text="EDIT DONATION", command=edit_donation, bg="#3498db", fg="white", font=("Cooper Black", 12))
        edit_button.pack(side=LEFT, padx=320, pady=10)

        delete_button = Button(content_frame, text="DELETE DONATION", command=delete_donation, bg="#e74c3c", fg="white", font=("Cooper Black", 12))
        delete_button.pack(side=LEFT, padx=30, pady=10)

        conn.close()
        fms.scr.mainloop()

#------------------------------------------------------- Manager Dashboard Code End --------------------------------------------------------------#    

#------------------------------------------------------------- User Dashboard Code Start ---------------------------------------------------------#    

#--  User Main Page------       
    def Userdetails(fms, user_id):

        fms.scr.destroy()
        fms.scr = Tk()

        # getting screen width and height of display
        width= fms.scr.winfo_screenwidth() 
        height= fms.scr.winfo_screenheight()
        
        #setting tkinter window size
        fms.scr.geometry("%dx%d" % (width, height))
        
        fms.scr.title("FOOD MANAGEMENT SYSTEM")
        
        fms.managerdashf1= Frame(fms.scr, bg="#ffffff")

        fms.logo = PhotoImage(file="logo.png")
        fms.logo_img1 = fms.logo.subsample(2,2)
        
        fms.logo_banner1 = Label(fms.managerdashf1, image=fms.logo_img1)
        fms.logo_banner1.pack(side=LEFT)  

        fms.managerlabel= Label(text="Weclome to User Dashboard!!", bg="#0b1335", fg="white",font=("cooper black",14))
        fms.managerlabel.place(x=1000,y=50)

        fms.logout=Button(fms.managerdashf1,text="LOGOUT", command=fms.main, bg="#0b1335",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.logout.place(x=1075,y=100)

        # code to display the local time
        fms.localtime=time.asctime(time.localtime(time.time()))
        fms.tim=Label(fms.managerdashf1,text=fms.localtime,fg="white",font=("cooper black",14),bg="#0b1335")
        fms.managerdashf1.pack(fill=BOTH)

        fms.sidebar = Frame(fms.scr, bg="#d3ede6")
        fms.sidebar.pack(side=LEFT, fill=Y) 
        
        # Add buttons to the sidebar

        fms.profile = Button(fms.sidebar,text="VIEW PROFILE", command=lambda:fms.Userdetails(user_id), bg="#f39c12",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.profile.grid(row=3, column=0, ipadx=0, padx=15, pady=15, sticky="ew")

        fms.viewdonations= Button(fms.sidebar,text="PENDING DONATIONS", command=lambda:fms.Userdonations(user_id), bg="#0b1335",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.viewdonations.grid(row=4, column=0, ipadx=0, padx=15, pady=15, sticky="ew")

        fms.viewaccepteddonations= Button(fms.sidebar,text="ACCEPTED DONATIONS", command=lambda:fms.User_accepted_donations(user_id), bg="#0b1335",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.viewaccepteddonations.grid(row=8, column=0, ipadx=0, padx=15, pady=15, sticky="ew")

        def show_custom_messages(message):
            # Create a new top-level window
            message_dialog = Toplevel()
            message_dialog.title("Message")
            
            # Set window size and position it in the center of the screen
            window_width = 350
            window_height = 150
            screen_width = message_dialog.winfo_screenwidth()
            screen_height = message_dialog.winfo_screenheight()
            x = (screen_width - window_width) // 2
            y = (screen_height - window_height) // 2
            message_dialog.geometry(f"{window_width}x{window_height}+{x}+{y}")
            
            # Add an icon label in #32CD32 color
            style = ttk.Style()
            style.configure("Error.TLabel", foreground="#32CD32")
            error_icon = ttk.Label(message_dialog, text="\u24D8", style="Error.TLabel", font=("Cooper Black", 24))
            error_icon.pack(pady=10)

            label = Label(message_dialog, text=message, fg="#32CD32", font=("Cooper Black", 12))
            label.pack(padx=10, pady=0)

            # Add an "OK" button to close the dialog
            ok_button = Button(message_dialog, text="OK", command=message_dialog.destroy, width=10, font=("Cooper Black", 12))
            ok_button.pack(pady=10)

        def show_custom_error(message):
            # Create a new top-level window
            error_dialog = Toplevel()
            error_dialog.title("Error Message")
            
            # Set window size and position it in the center of the screen
            window_width = 600
            window_height = 150
            screen_width = error_dialog.winfo_screenwidth()
            screen_height = error_dialog.winfo_screenheight()
            x = (screen_width - window_width) // 2
            y = (screen_height - window_height) // 2
            error_dialog.geometry(f"{window_width}x{window_height}+{x}+{y}")
            
            # Set window icon
            # error_dialog.iconbitmap(r"house.ico")

            # Add an icon label in red color
            style = ttk.Style()
            style.configure("Error.TLabel", foreground="red")
            error_icon = ttk.Label(error_dialog, text="\u26A0", style="Error.TLabel", font=("Cooper Black", 24))
            error_icon.pack(pady=10)

            label = Label(error_dialog, text=message, fg="red", font=("Cooper Black", 12))
            label.pack(padx=10, pady=0)
            
            # Add an "OK" button to close the dialog
            ok_button = Button(error_dialog, text="OK", command=error_dialog.destroy, width=10, font=("Cooper Black", 12))
            ok_button.pack(pady=10)
        
        # Function to load data into the Treeview
        def user_data():
            # Clear the existing data in the Treeview
            tree.delete(*tree.get_children())

            # Connect to the database
            conn = connect('fms.db')
            cursor = conn.cursor()

            # Retrieve the manager's data from the database
            cursor.execute("SELECT user_id, first_name, last_name, user_name, email, mobile_no FROM users WHERE user_id = ?", (user_id,))
            user = cursor.fetchone()

            if user:
                # Insert the data into the Treeview
                tree.insert("", END, values=(user[0], user[1], user[2], user[3], user[4], user[5]))

                # Apply the "my_font" tag to all items in the Treeview
                for item in tree.get_children():
                    tree.item(item, tags=("my_font",))

            # Close the connection
            conn.close()

        # Function to edit a manager's details
        def edit_user():
            # Get the selected item from the Treeview
            selected_item = tree.focus()
            
            if not selected_item:
                show_custom_error("Please select user to edit")
                return

            # Get the values of the selected record
            values = tree.item(selected_item, "values")
            user_id = values[0]
            
            def submit():
                # Get values from entry widgets
                first_name = first_name_entry.get()
                last_name = last_name_entry.get()
                user_name = user_name_entry.get()
                email = email_entry.get()
                mobile_no = mobile_no_entry.get()

                # Validate fields
                if not (first_name and last_name and user_name and email and mobile_no):
                    show_custom_error("All fields are required")
                    return

                # Validate email format
                if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
                    show_custom_error("Invalid email format")
                    return

                # Validate mobile number format (10 digits only)
                if not re.match(r'^\d{10}$', mobile_no):
                    show_custom_error("Invalid mobile number format. It should consist of 10 digits only.")
                    return
                
                # Connect to the database
                conn = connect('fms.db')
                cursor = conn.cursor()

                try:
                    # Check if the user_name or email already exists for other users
                    cursor.execute("SELECT COUNT(*) FROM users WHERE (user_name=? OR email=?) AND user_id != ?", (user_name, email, user_id))
                    existing_users_count = cursor.fetchone()[0]

                    if existing_users_count > 0:
                        # User_name or email already exists for other users, show error message
                        show_custom_error("User name or email already exists. Please choose a different one.")
                    else:
                        # Proceed with updating the user details
                        # Print the SQL query to verify correctness
                        print(f"Executing EDIT query: EDIT FROM users WHERE user_id = {user_id}")

                        # Update user in the users table
                        cursor.execute("UPDATE users SET first_name=?, last_name=?, user_name=?, email=?, mobile_no=? WHERE user_id=?",
                                    (first_name, last_name, user_name, email, mobile_no, user_id))

                        # Commit the changes
                        conn.commit()

                        # Show success message
                        show_custom_messages("User details updated successfully")

                        # Refresh the Treeview
                        user_data()

                        # Close the edit window
                        edit_window.destroy()

                except Exception as e:
                    # Show error message if update fails
                    show_custom_error(f"Failed to update user details: {str(e)}")

                finally:
                    # Close the connection
                    conn.close()

            # Create a Toplevel window for editing a user
            edit_window = Toplevel()
            edit_window.title("Edit Profile")

            # Calculate the center coordinates of the screen
            screen_width = edit_window.winfo_screenwidth()
            screen_height = edit_window.winfo_screenheight()
            window_width = 700
            window_height = 225
            x = (screen_width - window_width) // 2
            y = (screen_height - window_height) // 2

            # Set the geometry of the window to be centered and larger
            edit_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

            # Create labels and entry widgets for each field
            Label(edit_window, text="First Name:", font=("Cooper Black", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
            first_name_entry = Entry(edit_window, font=("Cooper Black", 12))
            first_name_entry.grid(row=0, column=1, padx=10, pady=10)

            Label(edit_window, text="Last Name:", font=("Cooper Black", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
            last_name_entry = Entry(edit_window, font=("Cooper Black", 12))
            last_name_entry.grid(row=1, column=1, padx=10, pady=10)

            Label(edit_window, text="User Name:", font=("Cooper Black", 12)).grid(row=0, column=2, padx=10, pady=10, sticky="e")
            user_name_entry = Entry(edit_window, font=("Cooper Black", 12))
            user_name_entry.grid(row=0, column=3, padx=10, pady=10)

            Label(edit_window, text="Email:", font=("Cooper Black", 12)).grid(row=3, column=0, padx=10, pady=10, sticky="e")
            email_entry = Entry(edit_window, font=("Cooper Black", 12))
            email_entry.grid(row=3, column=1, padx=10, pady=10)

            Label(edit_window, text="Mobile No:", font=("Cooper Black", 12)).grid(row=1, column=2, padx=10, pady=10, sticky="e")
            mobile_no_entry = Entry(edit_window, font=("Cooper Black", 12))
            mobile_no_entry.grid(row=1, column=3, padx=10, pady=10)

            # Populate the entry widgets with the selected manager's data
            first_name_entry.insert(0, values[1])
            last_name_entry.insert(0, values[2])
            user_name_entry.insert(0, values[3])
            email_entry.insert(0, values[4])
            mobile_no_entry.insert(0, values[5])
            
            # Create a Submit button
            submit_button = Button(edit_window, text="Submit", command=submit, font=("Cooper Black", 12))
            submit_button.grid(row=4, columnspan=4, pady=10)

            # Main loop for the edit window
            edit_window.mainloop()

        # Create the main content frame
        content_frame = Frame(fms.scr, bg="lightgray")
        content_frame.pack(side=LEFT, fill=BOTH, expand=True)

        # Create a label for the title
        title_label = Label(content_frame, text="VIEW PROFILE", font=("Cooper Black", 16), bg="#0b1335", fg="white", pady=10)
        title_label.pack(fill=X)
        title_label.pack(pady=(0, 85))    

        # Create treeview
        tree = ttk.Treeview(content_frame, columns=("User ID", "First Name", "Last Name", "User Name", "Email", "Mobile No"), show="headings", padding=(0, 5))

        # Set the font for the headings
        tree.heading("User ID", text="User ID", anchor=CENTER)
        tree.heading("First Name", text="First Name", anchor=CENTER)
        tree.heading("Last Name", text="Last Name", anchor=CENTER)
        tree.heading("User Name", text="User Name", anchor=CENTER)
        tree.heading("Email", text="Email", anchor=CENTER)
        tree.heading("Mobile No", text="Mobile No", anchor=CENTER)
        
        # Configure Treeview style
        style = ttk.Style()
        style.configure("Custom.Treeview", font=("Cooper Black", 12))
        style.configure("Treeview.Row", padding=(0, 5))

        # Set the background color for the headers
        style.configure("Treeview.Heading", background="gray")

        # Define a tag named "my_font" with the desired font
        tree.tag_configure("my_font", font=("Cooper Black", 12))
        tree.pack()

        # Connect to the SQLite3 database
        conn = connect('fms.db')
        cursor = conn.cursor()

        # Retrieve the user's data from the database
        cursor.execute("SELECT user_id, first_name, last_name, user_name, email, mobile_no FROM users WHERE user_id = ?", (user_id,))
        user = cursor.fetchone()

        if user:
           # Insert the manager's data into the Treeview
           tree.insert("", END, values=(user[0], user[1], user[2], user[3], user[4], user[5]))

        # Apply the "my_font" tag to all items in the treeview
        for user in tree.get_children():
            tree.item(user, tags=("my_font",))

        edit_button = Button(content_frame, text="EDIT PROFILE", command=edit_user, bg="#3498db", fg="white", font=("Cooper Black", 12))
        edit_button.pack(side=LEFT, padx=550, pady=10)


        fms.scr.mainloop()

#--- User Donations Page -----
        
    def Userdonations(fms, user_id):

        fms.scr.destroy()
        fms.scr = Tk()
        
        # getting screen width and height of display
        width= fms.scr.winfo_screenwidth() 
        height= fms.scr.winfo_screenheight()
        
        #setting tkinter window size
        fms.scr.geometry("%dx%d" % (width, height))
        
        fms.scr.title("FOOD MANAGEMENT SYSTEM")
        
        fms.managerdashf1= Frame(fms.scr, bg="#ffffff")

        fms.logo = PhotoImage(file="logo.png")
        fms.logo_img1 = fms.logo.subsample(2,2)
        
        fms.logo_banner1 = Label(fms.managerdashf1, image=fms.logo_img1)
        fms.logo_banner1.pack(side=LEFT)  

        fms.managerlabel= Label(text="Weclome to User Dashboard!!", bg="#0b1335", fg="white",font=("cooper black",14))
        fms.managerlabel.place(x=1000,y=50)

        fms.logout=Button(fms.managerdashf1,text="LOGOUT", command=fms.main, bg="#0b1335",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.logout.place(x=1075,y=100)
       
        fms.localtime=time.asctime(time.localtime(time.time()))
        fms.tim=Label(fms.managerdashf1,text=fms.localtime,fg="white",font=("cooper black",14),bg="#0b1335")
        fms.managerdashf1.pack(fill=BOTH)

        fms.sidebar = Frame(fms.scr, bg="#d3ede6")
        fms.sidebar.pack(side=LEFT, fill=Y) 
        
        # Add buttons to the sidebar

        fms.profile = Button(fms.sidebar,text="VIEW PROFILE", command=lambda:fms.Userdetails(user_id), bg="#0b1335",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.profile.grid(row=3, column=0, ipadx=0, padx=15, pady=15, sticky="ew")

        fms.viewdonations= Button(fms.sidebar,text="PENDING DONATIONS", command=lambda:fms.Userdonations(user_id), bg="#f39c12",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.viewdonations.grid(row=4, column=0, ipadx=0, padx=15, pady=15, sticky="ew")

        fms.viewaccepteddonations= Button(fms.sidebar,text="ACCEPTED DONATIONS", command=lambda:fms.User_accepted_donations(user_id), bg="#0b1335",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.viewaccepteddonations.grid(row=8, column=0, ipadx=0, padx=15, pady=15, sticky="ew")

        def show_custom_messages(message):
            # Create a new top-level window
            message_dialog = Toplevel()
            message_dialog.title("Message")
            
            # Set window size and position it in the center of the screen
            window_width = 350
            window_height = 150
            screen_width = message_dialog.winfo_screenwidth()
            screen_height = message_dialog.winfo_screenheight()
            x = (screen_width - window_width) // 2
            y = (screen_height - window_height) // 2
            message_dialog.geometry(f"{window_width}x{window_height}+{x}+{y}")
            
            # Add an icon label in #32CD32 color
            style = ttk.Style()
            style.configure("Error.TLabel", foreground="#32CD32")
            error_icon = ttk.Label(message_dialog, text="\u24D8", style="Error.TLabel", font=("Cooper Black", 24))
            error_icon.pack(pady=10)

            label = Label(message_dialog, text=message, fg="#32CD32", font=("Cooper Black", 12))
            label.pack(padx=10, pady=0)

            # Add an "OK" button to close the dialog
            ok_button = Button(message_dialog, text="OK", command=message_dialog.destroy, width=10, font=("Cooper Black", 12))
            ok_button.pack(pady=10)

        def show_custom_error(message):
            # Create a new top-level window
            error_dialog = Toplevel()
            error_dialog.title("Error Message")
            
            # Set window size and position it in the center of the screen
            window_width = 350
            window_height = 150
            screen_width = error_dialog.winfo_screenwidth()
            screen_height = error_dialog.winfo_screenheight()
            x = (screen_width - window_width) // 2
            y = (screen_height - window_height) // 2
            error_dialog.geometry(f"{window_width}x{window_height}+{x}+{y}")
            
            # Set window icon
            # error_dialog.iconbitmap(r"house.ico")

            # Add an icon label in red color
            style = ttk.Style()
            style.configure("Error.TLabel", foreground="red")
            error_icon = ttk.Label(error_dialog, text="\u26A0", style="Error.TLabel", font=("Cooper Black", 24))
            error_icon.pack(pady=10)

            label = Label(error_dialog, text=message, fg="red", font=("Cooper Black", 12))
            label.pack(padx=10, pady=0)
            
            # Add an "OK" button to close the dialog
            ok_button = Button(error_dialog, text="OK", command=error_dialog.destroy, width=10, font=("Cooper Black", 12))
            ok_button.pack(pady=10)

        # Function to load data into the Treeview
        def load_donations():
            # Clear the existing data in the Treeview
            tree.delete(*tree.get_children())

            # Connect to the SQLite3 database
            conn = connect('fms.db')
            cursor = conn.cursor()

            try:
                # Fetch and display pending donations
                cursor.execute("SELECT donation_id, item_name, item_type, calories, amount_lb, servings, manager_id, donation_status FROM donation_details WHERE donation_status = 'pending'")
                pending_donations = cursor.fetchall()

                for donation in pending_donations:
                    # Fetch the manager's user_name from the managers table
                    cursor.execute("SELECT user_name FROM managers WHERE manager_id=?", (donation[6],))
                    manager_name = cursor.fetchone()[0]  # Assuming manager_id is at index 7

                    # Set the status color based on the donation status
                    status_color = 'red'  # Assuming pending donations are marked in red

                    # Insert a checkbox in the first column for selecting the donation
                    tree.insert("", END, values=(donation[0], donation[1], donation[2], donation[3], donation[4], donation[5], manager_name, donation[7]), tags=("my_font", status_color))

                # Apply the "my_font" tag to all items in the treeview
                for donation in tree.get_children():
                    tree.item(donation, tags=("my_font", status_color))

            except Exception as e:
                # Show error message if retrieval fails
                show_custom_error(f"Failed to load donations: {str(e)}")

            finally:
                # Close the connection
                conn.close()

        # code to accept the donation
        def accept_donation(user_id):
            # Get the selected item from the Treeview
            selected_item = tree.focus()
            if not selected_item:
                show_custom_error("Please select a donation to accept.")
                return

            # Get the donation_id of the selected donation
            donation_id = tree.item(selected_item, "values")[0]

            # Connect to the database
            conn = connect('fms.db')
            cursor = conn.cursor()

            try:
                # Check if the donation is already accepted
                donation_status = tree.item(selected_item, "values")[7]  # Assuming status is at index 7
                if donation_status == 'accepted':
                    show_custom_messages("Donation already accepted")
                else:
                    # Update the donation_status to 'accepted' in the donation_details table
                    cursor.execute("UPDATE donation_details SET donation_status = 'accepted', user_id = ? WHERE donation_id = ?", (user_id, donation_id,))
                    conn.commit()

                    # Get manager details
                    cursor.execute("SELECT managers.user_name, managers.email FROM managers JOIN donation_details ON managers.manager_id = donation_details.manager_id WHERE donation_details.donation_id = ?", (donation_id,))
                    manager_details = cursor.fetchone()
                    manager_name, manager_email = manager_details

                    # Get user_name and donation details
                    cursor.execute("SELECT users.user_name, donation_details.* FROM users JOIN donation_details ON users.user_id = donation_details.user_id WHERE donation_id = ?", (donation_id,))
                    user_details = cursor.fetchone()
                    user_name = user_details[0]
                    donation_id, item_name, item_type, calories, amount_lb, servings = user_details[1:7]

                    # Compose email
                    sender_email = "fms38865@gmail.com"
                    sender_password = "ktee vlno ediy uiop"
                    subject = "Donation Accepted"
                    message = f"Hello {manager_name},\n\nYour food donation has been accepted by {user_name} with the following details:\n\nItem Name: {item_name}\nItem Type: {item_type}\nCalories: {calories}\nAmount (lb): {amount_lb}\nServings: {servings}\n\nThank you,\nFood Management Team"
                    
                    # Send email to the manager
                    msg = MIMEMultipart()
                    msg['From'] = sender_email
                    msg['To'] = manager_email
                    msg['Subject'] = subject
                    msg.attach(MIMEText(message, 'plain'))

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(sender_email, sender_password)
                    server.sendmail(sender_email, manager_email, msg.as_string())
                    server.quit()

                    # Show success message
                    show_custom_messages("Donation accepted successfully")

                    # Refresh the Treeview
                    load_donations()

            except Exception as e:
                # Show error message if the update fails
                show_custom_error(f"Failed to accept donation: {str(e)}")

            finally:
                # Close the connection
                conn.close()

        # Create the main content frame
        content_frame = Frame(fms.scr, bg="lightgray")
        content_frame.pack(side=LEFT, fill=BOTH, expand=True)

        # Create a label for the title
        title_label = Label(content_frame, text="VIEW PENDING DONATIONS", font=("Cooper Black", 16), bg="#0b1335", fg="white", pady=10)
        title_label.pack(fill=X)
        title_label.pack(pady=(0, 85))

        # Create treeview
        tree = ttk.Treeview(content_frame, columns=("Donation ID", "Item Name", "Item Type", "Calories", "Amount(Lbs)", "Servings", "Added By", "Status"), show="headings", padding=(0, 5))

        # Set the font for the headings
        tree.heading("Donation ID", text="Donation ID", anchor=CENTER)
        tree.heading("Item Name", text="Item Name", anchor=CENTER)
        tree.heading("Item Type", text="Item Type", anchor=CENTER)
        tree.heading("Calories", text="Calories", anchor=CENTER)
        tree.heading("Amount(Lbs)", text="Amount(Lbs)", anchor=CENTER)
        tree.heading("Servings", text="Servings", anchor=CENTER)
        tree.heading("Added By", text="Added By", anchor=CENTER)
        tree.heading("Status", text="Status", anchor=CENTER)

        # Configure Treeview style
        style = ttk.Style()
        style.configure("Custom.Treeview", font=("Cooper Black", 12))
        style.configure("Treeview.Row", padding=(0, 5))

        # Set the background color for the headers
        style.configure("Treeview.Heading", background="gray")

        # Define a tag named "my_font" with the desired font
        tree.tag_configure("my_font", font=("Cooper Black", 12))

        # Set the column widths
        tree.column("Donation ID", width=150)
        tree.column("Item Name", width=150)
        tree.column("Item Type", width=150)
        tree.column("Calories", width=150)
        tree.column("Amount(Lbs)", width=150)
        tree.column("Servings", width=150)
        tree.column("Added By", width=150)
        tree.column("Status", width=150)

        tree.pack()
        
        # Connect to the SQLite3 database
        conn = connect('fms.db')
        cursor = conn.cursor()

        # Fetch and display pending donations
        cursor.execute("SELECT donation_id, item_name, item_type, calories, amount_lb, servings, manager_id, donation_status, user_id FROM donation_details WHERE donation_status = 'pending'")
        pending_donations = cursor.fetchall()

        for donation in pending_donations:
            # Fetch the manager's user_name from the managers table
            cursor.execute("SELECT user_name FROM managers WHERE manager_id=?", (donation[6],))
            manager_name = cursor.fetchone()[0]

            # Set the status color based on the donation status
            status_color = 'red'  # Assuming pending donations are marked in red

            # Insert the data into the Treeview with the status color
            tree.insert("", END, values=(donation[0], donation[1], donation[2], donation[3], donation[4], donation[5], manager_name, donation[7]), tags=("my_font", status_color))

        # Apply the "my_font" tag to all items in the treeview
        for donation in tree.get_children():
            tree.item(donation, tags=("my_font", status_color))

        # Button to accept the selected donation
        accept_button = Button(content_frame, text="ACCEPT DONATION", command=lambda: accept_donation(user_id), bg="#2ecc71", fg="white", font=("Cooper Black", 12))
        accept_button.pack(side=LEFT, padx=500, pady=10)

        conn.close()
        fms.scr.mainloop()

#--- User Accepted Donations Page -----
        
    def User_accepted_donations(fms, user_id):
        fms.scr.destroy()
        fms.scr = Tk()
        
        # getting screen width and height of display
        width= fms.scr.winfo_screenwidth() 
        height= fms.scr.winfo_screenheight()
        
        #setting tkinter window size
        fms.scr.geometry("%dx%d" % (width, height))
        
        fms.scr.title("FOOD MANAGEMENT SYSTEM")
        
        fms.managerdashf1= Frame(fms.scr, bg="#ffffff")

        fms.logo = PhotoImage(file="logo.png")
        fms.logo_img1 = fms.logo.subsample(2,2)
        
        fms.logo_banner1 = Label(fms.managerdashf1, image=fms.logo_img1)
        fms.logo_banner1.pack(side=LEFT)  

        fms.managerlabel= Label(text="Weclome to User Dashboard!!", bg="#0b1335", fg="white",font=("cooper black",14))
        fms.managerlabel.place(x=1000,y=50)

        fms.logout=Button(fms.managerdashf1,text="LOGOUT", command=fms.main, bg="#0b1335",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.logout.place(x=1075,y=100)
       
        fms.localtime=time.asctime(time.localtime(time.time()))
        fms.tim=Label(fms.managerdashf1,text=fms.localtime,fg="white",font=("cooper black",14),bg="#0b1335")
        fms.managerdashf1.pack(fill=BOTH)

        fms.sidebar = Frame(fms.scr, bg="#d3ede6")
        fms.sidebar.pack(side=LEFT, fill=Y) 
        
        # Add buttons to the sidebar

        fms.profile = Button(fms.sidebar,text="VIEW PROFILE", command=lambda:fms.Userdetails(user_id), bg="#0b1335",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.profile.grid(row=3, column=0, ipadx=0, padx=15, pady=15, sticky="ew")

        fms.viewdonations= Button(fms.sidebar,text="PENDING DONATIONS", command=lambda:fms.Userdonations(user_id), bg="#0b1335",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.viewdonations.grid(row=4, column=0, ipadx=0, padx=15, pady=15, sticky="ew")

        fms.viewaccepteddonations= Button(fms.sidebar,text="ACCEPTED DONATIONS", command=lambda:fms.User_accepted_donations(user_id), bg="#f39c12",cursor="hand2",
                      fg="white",font=("cooper black",14))
        fms.viewaccepteddonations.grid(row=8, column=0, ipadx=0, padx=15, pady=15, sticky="ew")

        # Create the main content frame
        content_frame = Frame(fms.scr, bg="lightgray")
        content_frame.pack(side=LEFT, fill=BOTH, expand=True)

        # Create a label for the title
        title_label = Label(content_frame, text="VIEW ACCEPTED DONATIONS", font=("Cooper Black", 16), bg="#0b1335", fg="white", pady=10)
        title_label.pack(fill=X)
        title_label.pack(pady=(0, 85))

        # Create treeview
        tree = ttk.Treeview(content_frame, columns=("Donation ID", "Item Name", "Item Type", "Calories", "Amount(Lbs)", "Servings", "Added By", "Status"), show="headings", padding=(0, 5))

        # Set the font for the headings
        tree.heading("Donation ID", text="Donation ID", anchor=CENTER)
        tree.heading("Item Name", text="Item Name", anchor=CENTER)
        tree.heading("Item Type", text="Item Type", anchor=CENTER)
        tree.heading("Calories", text="Calories", anchor=CENTER)
        tree.heading("Amount(Lbs)", text="Amount(Lbs)", anchor=CENTER)
        tree.heading("Servings", text="Servings", anchor=CENTER)
        tree.heading("Added By", text="Added By", anchor=CENTER)
        tree.heading("Status", text="Status", anchor=CENTER)

        # Configure Treeview style
        style = ttk.Style()
        style.configure("Custom.Treeview", font=("Cooper Black", 12))
        style.configure("Treeview.Row", padding=(0, 5))

        # Set the background color for the headers
        style.configure("Treeview.Heading", background="gray")

        # Define a tag named "my_font" with the desired font
        tree.tag_configure("my_font", font=("Cooper Black", 12))

        # Set the column widths
        tree.column("Donation ID", width=100)
        tree.column("Item Name", width=150)
        tree.column("Item Type", width=150)
        tree.column("Calories", width=150)
        tree.column("Amount(Lbs)", width=150)
        tree.column("Servings", width=150)
        tree.column("Added By", width=150)
        tree.column("Status", width=150)

        tree.pack()
        
        # Connect to the SQLite3 database
        conn = connect('fms.db')
        cursor = conn.cursor()

        # Fetch and display pending donations
        cursor.execute("SELECT donation_id, item_name, item_type, calories, amount_lb, servings, manager_id, donation_status, user_id FROM donation_details WHERE donation_status = 'accepted'AND user_id = ?", (user_id,))
        pending_donations = cursor.fetchall()

        for donation in pending_donations:
            # Fetch the manager's user_name from the managers table
            cursor.execute("SELECT user_name FROM managers WHERE manager_id=?", (donation[6],))
            manager_name = cursor.fetchone()[0]

            # Set the status color based on the donation status
            status_color = 'red'  # Assuming pending donations are marked in red

            # Insert the data into the Treeview with the status color
            tree.insert("", END, values=(donation[0], donation[1], donation[2], donation[3], donation[4], donation[5], manager_name, donation[7]), tags=("my_font", status_color))

        # Apply the "my_font" tag to all items in the treeview
        for donation in tree.get_children():
            tree.item(donation, tags=("my_font", status_color))

        # Button to accept the selected donation
        # accept_button = Button(content_frame, text="ACCEPT DONATION", command=lambda: accept_donation(user_id), bg="#2ecc71", fg="white", font=("Cooper Black", 12))
        # accept_button.pack(side=LEFT, padx=500, pady=10)

        conn.close()
        fms.scr.mainloop()

#-------------------------------------------------------------- User Dashboard Code End ----------------------------------------------------------#    

#-------------------------------------------------------------- Database Connections Code Start --------------------------------------------------#               

    def validate_email(fms, email):
        # Regular expression pattern for email validation
        pattern = r'^[a-zA-Z0-9_.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]*$'
        return re.match(pattern, email) is not None
    
    def validate_mobile_number(fms, mobile_no):
        return mobile_no.isdigit() and len(mobile_no) == 10

    def userReg(fms):
        def resultreg():
            first_name = fms.first.get()
            last_name = fms.last.get()
            user_name = fms.usern.get()
            password = fms.passd.get()
            email = fms.email.get()
            mobile_no = fms.mob.get()
            return first_name, last_name, user_name, password, email, mobile_no
        
        fms.credreg = resultreg()
        
        fms.con = connect("fms.db")
        fms.cur = fms.con.cursor()
        
        try:
            fms.cur.execute('''CREATE TABLE IF NOT EXISTS users (
                            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            first_name VARCHAR(50) NOT NULL,
                            last_name VARCHAR(50) NOT NULL,
                            user_name VARCHAR(50) NOT NULL,
                            password VARCHAR(50) NOT NULL,
                            email VARCHAR(50),
                            mobile_no VARCHAR(50) NOT NULL
                        )''')
        except Exception as e:
            print(e)

        # Check if the username and email already exist
        fms.cur.execute("SELECT count(*) FROM users WHERE user_name=? OR email=?", (fms.credreg[2], fms.credreg[4]))
        count = fms.cur.fetchone()[0]

        if count > 0:
            messagebox.showerror("Error", "Username or email already exists.", icon='error')
        elif "" in fms.credreg[:6]:
            messagebox.showerror("Error", "Empty entry is not allowed", icon='error')
        elif not fms.validate_email(fms.credreg[4]):
            messagebox.showerror("Error", "Invalid email address", icon='error')
        elif not fms.validate_mobile_number(fms.credreg[5]):
            messagebox.showerror("Error", "Invalid mobile number format. It should consist of 10 digits only.", icon='error')
   
        else:
            try:
                fms.cur.execute("INSERT INTO users (first_name, last_name, user_name, password, email, mobile_no) VALUES (?, ?, ?, ?, ?, ?)",
                                (fms.credreg[0], fms.credreg[1], fms.credreg[2], fms.credreg[3], fms.credreg[4], fms.credreg[5]))
                fms.con.commit()
                messagebox.showinfo("Success", "You have successfully registered", icon="info")
                fms.main()
                fms.scr.destroy()  # Destroy the registration window
            except Exception as e:
                print(e)  
    
    def userlog(fms):
        fms.loguser=fms.user.get()
        fms.logpass=fms.pasd.get()
        return fms.loguser,fms.logpass

    def userdatabase(fms):
        
        fms.credlog=fms.userlog()
        fms.con=connect("fms.db")
        fms.cur=fms.con.cursor()
        
        x=fms.cur.execute("select count(*), user_id from users where user_name=%r and password=%r"%(fms.credlog[0],fms.credlog[1]))
        count, user_id = list(x)[0]

        if count == 0:
           if fms.credlog[0]=="" or fms.credlog[1]=="":
            messagebox.showerror("Error", "Empty entry is not allowed", icon='error')
           else:
            messagebox.showerror("Error", "You are not registered yet", icon='error')
                
        else:
            messagebox.showinfo("Success", "You have successfully logged in", icon="info")        
            # Assuming you have user_id here
            fms.Userdetails(user_id)
            # fms.Userdonations(user_id)
    
    def resultadmin(fms):
        fms.loguser=fms.usera.get()
        fms.logpass=fms.pasda.get()
        return fms.loguser,fms.logpass
    
    def admindatabase(fms):

        fms.credadm=fms.resultadmin()
        
        fms.con=connect("fms.db")
        
        fms.cur=fms.con.cursor()
        x=fms.cur.execute("select count(*) from admin where user_name=%r and password=%r"%(fms.credadm[0],fms.credadm[1]))

        if list(x)[0][0]==0:
            if fms.credadm[0]=="" or fms.credadm[1]=="":
                messagebox.showerror("Error", "Empty entry is not allowed", icon='error')
            else:
                messagebox.showerror("Error", "Invalid credentials!", icon='error')
            
        else:
            messagebox.showinfo("Success", "You have successfully logged in", icon="info")          
            fms.Viewmanagers()
    
    def resultmanager(fms):
        fms.loguser=fms.usera.get()
        fms.logpass=fms.pasda.get()
        return fms.loguser,fms.logpass
    
    def managerdatabase(fms):
      
        #code for checking credentials
        fms.credmanager = fms.resultmanager()
        fms.con = connect("fms.db")
        fms.cur = fms.con.cursor()
        
        x = fms.cur.execute("select count(*), manager_id from managers where user_name=%r and password=%r" % (fms.credmanager[0], fms.credmanager[1]))
        count, manager_id = list(x)[0]

        if count == 0:
            if fms.credmanager[0] == "" or fms.credmanager[1] == "":
                messagebox.showerror("Error", "Empty entry is not allowed", icon='error')
            else:
                messagebox.showerror("Error", "Please contact your administrator to register your account.", icon='error')
        else:
                messagebox.showinfo("Success", "You have successfully logged in", icon="info")
                fms.Managerdetails(manager_id)

#-------------------------------------------------------------- Database Connections Code End ----------------------------------------------------#    
x=Fms()
x.main()
