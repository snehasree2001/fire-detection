import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
 

def sendmail(usermailid):
    
    img_data = open("test.jpg", 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'Fire Detection Image Mail123'
    msg['From'] = 'nvijraj@gmail.com'
    msg['To'] = usermailid
    print("in func")
    text = MIMEText("This is test mail")
    msg.attach(text)
    image = MIMEImage(img_data, name="Fire_detection.jpg")
    msg.attach(image)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('nvijraj@gmail.com','Mithun12345')
    s.sendmail('nvijraj@gmail.com', usermailid, msg.as_string())
   
    s.quit()
  
    print("Sent Successfully")
   
