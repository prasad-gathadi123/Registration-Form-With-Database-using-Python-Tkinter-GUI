from tkinter import *
import tkinter.messagebox
from functools import partial
from tkinter import *
from PIL import Image , ImageTk
import time
import datetime as dt
from time import *
import datetime
import tkinter.messagebox
import mysql.connector
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase
from email import encoders


mydb = mysql.connector.connect(
		host="localhost",          #this informatio is defferent in your case
		user="root",
		passwd="",
		database = "registration"
		)
mycursor = mydb.cursor()
def raise_frame(frame):
    frame.tkraise()
#root = tk.Tk()
main_win = Tk()
main_win.geometry('600x700')
main_win.title("Registration Form")

def main():
    t = datetime.datetime.now()
    time_now = t.strftime("%c")
    fourth_frame = Frame(main_win)
    fourth_frame.place(x=0, y=0, width=600, height=700)

    third_frame = Frame(main_win)
    third_frame.place(x=0, y=0, width=600, height=700)

    second_frame = Frame(main_win)
    second_frame.place(x=0, y=0, width=600, height=700)

    first_frame = Frame(main_win)
    first_frame.place(x=0, y=0, width=600, height=700)
     
    def new():
        l0n = Label(first_frame, text="Registration",width=20,font=("bold", 20))
        l0n.place(x=120,y=50)
        id = StringVar()
        fn = StringVar()
        ln = StringVar()
        emid = StringVar()
        mono = StringVar()
        radio_var = StringVar()
        d = StringVar()
        m = StringVar()
        y = StringVar()
        def printt() :
            idno = id.get()
            first = fn.get()
            last = ln.get()
            emailid = emid.get()
            gender = radio_var.get()
            DOB = d.get()+'-'+m.get()+'-'+y.get()
            mno = mono.get()
            t = datetime.datetime.now()
            time_now = t.strftime("%c")
            #tkinter.messagebox.showinfo("Welcome",'User is Successfully Signed up !! \nDetails send to Your Registered Email Id. ')
            mycursor.execute('CREATE TABLE IF NOT EXISTS info (idno varchar(5), first varchar(55) , last varchar(55) , emailid varchar(55) ,mno varchar(11) , gender varchar(8) , DOB varchar(15) ,Regtime varchar(55))')
            mycursor.execute('INSERT INTO info (idno,first, last,emailid,mno,gender,DOB,Regtime) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)',(idno,first.upper() , last.upper() , emailid , mno, gender , DOB ,time_now))

            try :
                email_id = emailid
                toaddr = email_id
                me = ''      ##Here Enter Your email id
                subject='Registration Confirmed'
                msg = MIMEMultipart()
                msg['Subject'] = subject
                msg['From'] = me
                msg['To'] = toaddr
                body ="Congratulation !!! "+ first.upper() +" "+ last.upper() +" \nYour Registration is confirmed . Your details are as follows  :\n"+ "Position Number  :  "+idno+"\n"+"Name  :  "+first.upper()+ "\t" +last.upper() +"\n"+"Email id  :  "+ emailid +"\n"+"Mobile Number  : "+mno+"\n"+"Gender  :  "+ gender+"\n"+ "Date of Birth  :  "+DOB+"\n"+time_now +"\nThank you for registration ."
                msg.attach(MIMEText(body, 'plain'))
                server = smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login(user = 'Enter your email id',password='Enter password')
                server.send_message(msg)
                server.quit()
                print("-------------------------------------------------------------------------------------------")
                print(f"position number : {idno}")
                print(f"Name   :   {first} {last}")
                print(f"Email id  :  {emailid}")
                print(f"Gender  :  {gender}")
                print(f"Mobile Number  : {mno}")
                print(f"Date of Birth  :  {DOB}")
                print("-------------------------------------------------------------------------------------------")
                tkinter.messagebox.showinfo("Welcome",'User is Successfully Signed up !! \nDetails send to Your Registered Email Id. ')
                mydb.commit()
                mycursor.close()
            except :
                tkinter.messagebox.showinfo("Error",'Please Enter Valid Email Id ')

            #exit(1)
            

            
        l11n = Label(first_frame , text = "idno      :   " , width = 18 , font=("helvetica",12,"bold"))
        l11n.place(x = 110,y=110)
        e11n = Entry(first_frame,textvar=id)
        e11n.place(x = 320 , y= 110)
        
        l1n = Label(first_frame , text = "First Name      :   " , width = 18 , font=("helvetica",12,"bold"))
        l1n.place(x = 110,y=140)
        e1n = Entry(first_frame,textvar=fn)
        e1n.place(x = 320 , y= 140)

        l2n = Label(first_frame , text = "Last Name      :   " , width = 18 , font=("helvetica",12,"bold"))
        l2n.place(x = 110,y=190)
        e2n = Entry(first_frame,textvar=ln)
        e2n.place(x = 320 , y= 190)

        l3n = Label(first_frame , text = "Email Id           :   " , width = 18 , font=("helvetica",12,"bold"))
        l3n.place(x = 110,y=240)
        e3n = Entry(first_frame,textvar=emid)
        e3n.place(x = 320 , y= 240)

        l4n = Label(first_frame , text = "Date Of Birth   :   " , width = 18 , font=("helvetica",12,"bold"))
        l4n.place(x = 110,y=290)

        list1 = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
        dd1 = OptionMenu(first_frame , d,*list1)
        d.set("Day")
        dd1.config(width = 2)
        dd1.place(x = 320 , y = 290)
        list2 = ['Jan' ,'Feb','Mar','April','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        dd2 = OptionMenu(first_frame , m,*list2)
        m.set("Mon")
        dd2.config(width = 2)
        dd2.place(x = 380 , y = 290)
        list3 = ['1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005',]
        dd3 = OptionMenu(first_frame , y,*list3)
        y.set("Year")
        dd3.config(width = 2)
        dd3.place(x = 440 , y = 290)


        l5n = Label(first_frame , text = "Mobile Number  :   " , width = 18 , font=("helvetica",12,"bold"))
        l5n.place(x = 110,y=340)
        e5n = Entry(first_frame,textvar=mono)
        e5n.place(x = 320 , y= 340)

        r = Label(first_frame , text = "Gender              :   " , width = 18 , font=("helvetica",12,"bold"))
        r.place(x = 110,y=390)

        r1 = Radiobutton(first_frame, text = "Male" , variable = radio_var , value = "Male").place(x = 320 , y = 390)
        r2 = Radiobutton(first_frame , text = "Female" , variable = radio_var , value = "Female").place(x = 380 , y = 390)



        Button(first_frame, text='SUBMIT',width=20,bg='brown',fg='white', command=printt).place(x=110,y=450)
        Button(first_frame, text='EXIT',width=20,bg='brown',fg='white', command=ex).place(x=320,y=450)


        Button(first_frame, text='CLICK HERE TO UPDATE',width=20,bg='brown',fg='white', command=update).place(x=40,y=580)
        Button(first_frame, text='CLICK HERE TO DELETE',width=20,bg='brown',fg='white', command=delete).place(x=230,y=580)
        Button(first_frame, text='CLICK HERE TO VIEW',width=20,bg='brown',fg='white', command=view).place(x=420,y=580)
        Button(first_frame, text="HOME",width=20,bg='white',fg='black', command=main).place(x=10,y=10) 

        raise_frame(first_frame)
    def update():
        emid = StringVar()
        update_frame = Frame(second_frame)
        update_frame.place(x=0, y=0, width=600, height=700)

        def update_inner() :
            emid1 = StringVar()
            mono = StringVar()                
            emailid = emid.get()
            raise_frame(update_frame)
            def update_in() :
                emailid1 = emid1.get()
                mno = mono.get()     
                mycursor = mydb.cursor()
                sql_select_query = """Update info set emailid = %s , mno = %s where emailid = %s"""
                change = (emailid1 , mno , emailid)
                mycursor.execute(sql_select_query, change)
                mydb.commit()
                print(emailid + "\t" + emailid1 + "\t" + mno)
                l5u = Label(update_frame , text = "Your Details is Updated Successfully. " , width = 40 , font=("helvetica",12,"bold"))
                l5u.place(x = 110,y=450)
            
            l3u = Label(second_frame , text = "Enter Updated Details " , width = 40 , font=("helvetica",12,"bold"))
            l3u.place(x = 95,y=100)
            
            l2u = Label(update_frame , text = "Enter New Email Id   :   " , width = 20 , font=("helvetica",12,"bold"))
            l2u.place(x = 110,y=240)
            e2u = Entry(second_frame,textvar=emid1)
            e2u.place(x = 320 , y= 240)

            
            l4u = Label(update_frame , text = "Enter New MoNo   :   " , width = 20 , font=("helvetica",12,"bold"))
            l4u.place(x = 110,y=290)
            e4u = Entry(second_frame,textvar=mono)
            e4u.place(x = 320 , y= 290)
            Button(second_frame, text='Update',width=20,bg='brown',fg='white',command=update_in).place(x=120,y=350)
            Button(second_frame, text='Back',width=20,bg='brown',fg='white',command=update).place(x=300,y=350)

            

        l1u = Label(second_frame , text = "Enter Old Email Id           :   " , width = 20 , font=("helvetica",12,"bold"))
        l1u.place(x = 110,y=240)
        e1u = Entry(second_frame,textvar=emid)
        e1u.place(x = 320 , y= 240)
            
        raise_frame(first_frame)
        Button(second_frame, text='Submit',width=20,bg='brown',fg='white',command=update_inner).place(x=230,y=350)

        
        l1 = Label(second_frame, text="UPDATE WINDOW",width=20,font=("bold", 20))
        l1.place(x=120,y=50)
        Button(second_frame, text="HOME",width=20,bg='white',fg='black', command=main).place(x=10,y=10)
        #Button(second_frame, text='Submit',width=20,bg='brown',fg='white',command=update_inner).place(x=230,y=500)
        Button(second_frame, text="CLICK HERE TO NEW",width=20,bg='brown',fg='white', command=new).place(x=40,y=580) 
        Button(second_frame, text="CLICK HERE TO DELETE",width=20,bg='brown',fg='white', command=delete).place(x=230,y=580) 
        Button(second_frame, text="CLICK HERE TO VIEW",width=20,bg='brown',fg='white', command=view).place(x=420,y=580) 
       # tkinter.messagebox.showinfo("Welcome to page 2")
        raise_frame(second_frame)
    def delete():
        emid = StringVar()
        Button(third_frame, text="HOME",width=20,bg='white',fg='black', command=main).place(x=10,y=10)
        l1d = Label(third_frame, text="DELETE WINDOW ",width=20,font=("bold", 20))
        l1d.place(x=120,y=50)
        def remove():
            emailid = emid.get()
            try :
                mycursor = mydb.cursor()
                sql_select_query = """select * from info where emailid = %s"""
                mycursor.execute(sql_select_query, (emailid,))
                myresult = mycursor.fetchall()
                for i in myresult :
                    print(i[2])
                mycursor.execute('DELETE FROM info WHERE (first,last)  in (VALUES(%s,%s)) ', (i[1],i[2]) )
                mydb.commit()
                l3d = Label(third_frame , text = "Your Account Successfully Deleted !  " , width = 40 , font=("helvetica",12,"bold"))
                l3d.place(x = 80,y=300)
                l4d = Label(third_frame , text = "Thank You ! " , width = 40 , font=("helvetica",12,"bold"))
                l4d.place(x = 80,y=320)
            except :
                t = "You have entered wrong information."
                Label(third_frame , text = t , width = 40 , font=("helvetica",12,"bold")).place(x = 80,y=300)
            tkinter.messagebox.askquestion("Delete ?",'Do You Want to Delete  ?')
                
        l1v = Label(third_frame , text = "Enter Email ID      :   " , width = 18 , font=("helvetica",12,"bold"))
        l1v.place(x = 110,y=140)
        e1v = Entry(third_frame,textvar=emid)
        e1v.place(x = 320 , y= 140)

        Button(third_frame, text='Submit',width=20,bg='brown',fg='white',command=remove).place(x=130,y=230)
        Button(third_frame, text='Exit',width=20,bg='brown',fg='white',command=ex).place(x=300,y=230)

        Button(third_frame, text="CLICK HERE TO UPDATE",width=20,bg='brown',fg='white', command=update).place(x=40,y=580) 
        Button(third_frame, text="CLICK HERE TO NEW",width=20,bg='brown',fg='white', command=new).place(x=230,y=580) 
        Button(third_frame, text="CLICK HERE TO VIEW",width=20,bg='brown',fg='white', command=view).place(x=420,y=580) 
        raise_frame(third_frame)

    def view():
        emid1 = StringVar()
        def show():
            emailid1 = emid1.get()
            Label(fourth_frame , text = " \t\t\t\t\t\t\t\t\t\t"  , font=("helvetica",11,"bold")).place(x = 10,y=300)
            try :
                mycursor = mydb.cursor()
                sql_select_query = """select * from info where emailid = %s"""
                mycursor.execute(sql_select_query, (emailid1,))
                myresult = mycursor.fetchall()
                for i in myresult :
                    print(i[2])                
                mycursor.execute('SELECT idno,first, last,emailid,mno,gender,DOB FROM info WHERE (first,last) IN (VALUES (%s,%s))',(i[1],i[2]))
                myresult = mycursor.fetchall()
                Label(fourth_frame , text = " \t\t\t\t\t\t\t"  , font=("helvetica",11,"bold")).place(x = 10,y=300)
                for i in myresult :
                    Label(fourth_frame , text = "idno | Name  |   Email ID  |     Mo No   |    Gender    |     Date Of Birth    "  , font=("helvetica",11,"bold")).place(x = 10,y=257)
                    Label(fourth_frame , text = "-------------------------------------------------------------------------------------------------------------"  , font=("helvetica",11,"bold")).place(x = 10,y=280)
                    Label(fourth_frame , text = i  , font=("helvetica",11,"bold")).place(x = 10,y=300)
                mydb.commit()
                mycursor.close()
            except:
                t = "You have entered wrong information."
                Label(fourth_frame , text = t , width = 40 , font=("helvetica",12,"bold")).place(x = 100,y=300)
                
        l1v = Label(fourth_frame , text = "Enter Email ID      :   " , width = 18 , font=("helvetica",12,"bold"))
        l1v.place(x = 110,y=140)
        e1v = Entry(fourth_frame,textvar=emid1)
        e1v.place(x = 320 , y= 140)
        
        Button(fourth_frame, text='SUBMIT',width=20,bg='brown',fg='white',command = show).place(x=120,y=200)
        Button(fourth_frame, text='EXIT',width=20,bg='brown',fg='white',command = ex).place(x=320,y=200) 
        
        Button(fourth_frame, text="HOME",width=20,bg='white',fg='black', command=main).place(x=10,y=10)
        l3 = Label(fourth_frame, text="VIEW WINDOW ",width=20,font=("bold", 20))
        l3.place(x=120,y=50)

        Button(fourth_frame, text="CLICK HERE TO UPDATE",width=20,bg='brown',fg='white', command=update).place(x=40,y=580) 
        Button(fourth_frame, text="CLICK HERE TO NEW",width=20,bg='brown',fg='white', command=new).place(x=230,y=580) 
        Button(fourth_frame, text="CLICK HERE TO DELETE",width=20,bg='brown',fg='white', command=delete).place(x=420,y=580) 
        raise_frame(fourth_frame)
    def ex():
        tkinter.messagebox.askquestion("Exit ?",'Do You Want to Exit ?')
        exit()

    date = dt.datetime.now()
    w = Label(main_win, text=f"{dt.datetime.now():%a, %b %d %Y}", fg="white", bg="black", font=("helvetica", 10))
    w.place(x = 20, y=20)
    l1m = Label(main_win, text="Welcome To ",width=40,font=("bold", 16))
    l1m.place(x=50,y=50)
    l2m = Label(main_win, text="Registration System",width=40,font=("bold", 16))
    l2m.place(x=50,y=80)

    Button(main_win, text="CLICK HERE TO NEW",width=20,bg='brown',fg='white', command=new).place(x=230,y=200) 
    Button(main_win, text="CLICK HERE TO UPDATE",width=20,bg='brown',fg='white', command=update).place(x=230,y=250) 
    Button(main_win, text="CLICK HERE TO DELETE",width=20,bg='brown',fg='white', command=delete).place(x=230,y=300) 
    Button(main_win, text="CLICK HERE TO VIEW",width=20,bg='brown',fg='white', command=view).place(x=230,y=350) 
    Button(main_win, text="EXIT",width=20,bg='brown',fg='white', command=ex).place(x=230,y=400) 

    main_win.mainloop()



if __name__ == "__main__":
    main()
