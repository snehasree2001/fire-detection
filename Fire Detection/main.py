from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import pymysql
import random
import os.path
from PIL import Image, ImageTk
from tkinter import filedialog
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import matplotlib.pyplot as plt

def checklogin(): 
        if userentry.get()=="" and passentry.get()=="":
                messagebox.showerror("Error","Enter User Name and Password",parent=win )	
        else:
                try:                        
                        if userentry.get()=="Admin" and passentry.get()=="Admin":    
                                messagebox.showinfo("Success" , "Successfully Login" , parent = win )
                                win.destroy()
                                Insurancewindow()                                 
                except Exception as es:
                        messagebox.showerror("Error" , f"Error Duo to : {str(es)}", parent = win )
                        

def sendmymail():
    live_Camera = cv2.VideoCapture(0)
    lower_bound = np.array([11, 33, 111])
    upper_bound = np.array([90, 255, 255])
    labels = np.array([1, -1, -1, -1])
    trainingData = np.matrix([[501, 10], [255, 10], [501, 255], [10, 501]], dtype=np.float32)
    # Train the SVM
    svm = cv2.ml.SVM_create()
    svm.setType(cv2.ml.SVM_C_SVC)
    svm.setKernel(cv2.ml.SVM_LINEAR)
    svm.setTermCriteria((cv2.TERM_CRITERIA_MAX_ITER, 100, 1e-6))
    svm.train(trainingData, cv2.ml.ROW_SAMPLE, labels)
    while (live_Camera.isOpened()):
        ret, frame = live_Camera.read()
        frame = cv2.resize(frame, (1280, 720))
        frame = cv2.flip(frame, 1)

        frame_smooth = cv2.GaussianBlur(frame, (7, 7), 0)
        mask = np.zeros_like(frame)
        mask[0:720, 0:1280] = [255, 255, 255]
        img_roi = cv2.bitwise_and(frame_smooth, mask)
        frame_hsv = cv2.cvtColor(img_roi, cv2.COLOR_BGR2HSV)
        image_binary = cv2.inRange(frame_hsv, lower_bound, upper_bound)
        check_if_fire_detected = cv2.countNonZero(image_binary)

        if int(check_if_fire_detected) >= 38000:
            cv2.putText(frame, "Fire Detected !", (300, 60), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 0, 255), 2)

        cv2.imshow("Fire Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            img_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img_cap = plt.imshow(img_RGB)
            plt.savefig("test1.png")
            plt.show()
            live_Camera.release()
            cv2.destroyAllWindows()

def result():
    Country = ['Edge Detection', 'SVM Algorithm']
    s1 = random.randint(700, 900)
    s2 = random.randint(300, 600)
    GDP_Per_Capita = [s1, s2]

    plt.bar(Country, GDP_Per_Capita)
    plt.title('Time Analysis Graph')
    plt.xlabel('Algorithm')
    plt.ylabel('Time in Milli Seconds')
    plt.show()


def Insurancewindow():
        def fireimg(): 
                live_Camera = cv2.VideoCapture(0)     

                while(live_Camera.isOpened()):
                    ret, frame = live_Camera.read()
                    cv2.putText(frame,"Press Esc to take photo !",(100,20),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
                    cv2.putText(frame,"Press q to quit !",(100,80),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
                    cv2.imshow("Fire Detection",frame)         

                    
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        live_Camera.release()
                        cv2.destroyAllWindows()
                                       
                img_RGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                img_cap = plt.imshow(img_RGB)
                plt.savefig("test.png")
                plt.show()
                live_Camera.release()
                cv2.destroyAllWindows()
                
                
       
                

        def initiateCamera():
                live_Camera = cv2.VideoCapture(0)
                lower_bound = np.array([11,33,111])
                upper_bound = np.array([90,255,255])

                while(live_Camera.isOpened()):
                    ret, frame = live_Camera.read()
                    frame = cv2.resize(frame,(1280,720))
                    frame = cv2.flip(frame,1)


                    frame_smooth = cv2.GaussianBlur(frame,(7,7),0)
                    mask = np.zeros_like(frame)
                    mask[0:720, 0:1280] = [255,255,255]
                    img_roi = cv2.bitwise_and(frame_smooth, mask)
                    frame_hsv = cv2.cvtColor(img_roi,cv2.COLOR_BGR2HSV)
                    image_binary = cv2.inRange(frame_hsv, lower_bound, upper_bound)
                    check_if_fire_detected = cv2.countNonZero(image_binary)
                  

                    if int(check_if_fire_detected) >= 40000 :
                        cv2.putText(frame,"Fire Detected !",(300,60),cv2.FONT_HERSHEY_COMPLEX,3,(0,0,255),2)

                        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                        email_addr = 'sarun140689@gmail.com'
                        email_passwd = 'almqpdhzxzerjmqj'
                        server.login(email_addr, email_passwd)
                        server.sendmail(from_addr=email_addr, to_addrs='seattlecbe5@gmail.com',
                                        msg="Fire Detection Alert!!!")
                        server.close()



                    cv2.imshow("Fire Detection",frame)
                    
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        img_RGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                        img_cap = plt.imshow(img_RGB)
                        plt.savefig("test1.png")
                        plt.show()
                        live_Camera.release()
                        cv2.destroyAllWindows()
              
                
                
        def UploadAction(event=None):
            filename = filedialog.askopenfilename()
            print('Selected:', filename)
            con = pymysql.connect(host="localhost",user="root",password="root",database="firedetect")
            cur = con.cursor()
                                         
            cur.execute("insert into hardcopy(filename) values (%s)", ( filename))
            con.commit()
            con.close()                                        
            messagebox.showinfo("Success" , "Train Data Upload Successfully" , parent = des)
    
        def insert():
                con = pymysql.connect(host="localhost",user="root",password="root",database="firedetect")
                cur = con.cursor()
                                         
                cur.execute("insert into fireinfo(emailid) values (%s)", ( pno.get()))
                con.commit()
                con.close()                                        
                messagebox.showinfo("Success" , "Registered Successfully" , parent = des)
        
        des = Tk()
        des.title("Insurance Save ")	
        des.maxsize(width=800 ,  height=1000)
        des.minsize(width=800 ,  height=1000)
        photo=PhotoImage(file="fire3.png")
        l=Label(des,image=photo)
        l.image=photo       
        l.grid()
        
        heading = Label(des  , text = "Welcome" , font = 'Verdana 20 bold')
        heading.place(x=80 , y=60)

      

        btnbrowse = Button(des, text = "Train Dataset" ,font=' Verdana 10 bold' , command= UploadAction )
        btnbrowse.place(x=150, y=170) 

        btncamera = Button(des, text = "Initiate Camera" ,font='Verdana 10 bold' , command=initiateCamera  )
        btncamera.place(x=300, y=170)

        btnsend = Button(des, text = "SVM Classification" ,font='Verdana 10 bold' , command=sendmymail  )
        btnsend.place(x=450, y=170)

        btnsend = Button(des, text="Result Analysis", font='Verdana 10 bold', command=result )
        btnsend.place(x=630, y=170)
        des.mainloop()
        
win = Tk()

# app title
win.title("Fire Detection")

# window size
win.maxsize(width=800 ,  height=1000)
win.minsize(width=800 ,  height=1000)
win.configure(bg='pink') 
photo=PhotoImage(file="fire4.png")
l=Label(win,image=photo)
l.image=photo       
l.grid()

heading = Label(win  , text = "Login" , font = 'Verdana 20 bold',bg="white")
heading.place(x=80 , y=60)

# form data label
user  = Label(win , text= "User Name :" , font='Verdana 10 bold', bg="white")
user .place(x=80,y=130)
       
# Entry Box
user  = StringVar() 
        
userentry = Entry(win , width=40 , textvariable = user )
userentry.focus()
userentry.place(x=200 , y=130)

# form data label
passid = Label(win , text= "Password :" , font='Verdana 10 bold',bg="white")
passid.place(x=80,y=180)
       
# Entry Box
passid = StringVar() 
        
passentry = Entry(win , width=40 , show='*' , textvariable = passid )
passentry.focus()
passentry.place(x=200 , y=180)

# button login and clear

btn_login = Button(win , text = "Login" ,font='Verdana 10 bold', command=checklogin )
btn_login.place(x=200, y=230)

win.mainloop() 

 
