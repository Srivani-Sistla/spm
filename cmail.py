'''import smtplib
from smtplib import SMTP
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('srivanisistal5@gmail.com ','xwbkkcwcecwjazqb')
    msg=EmailMessage()
    msg['From']='srivanisistla5@gmail.com'
    msg['Subject']='Account Sign up OTP'
    msg['To']=to
    msg.set_content(body)
    server.send_message(msg)
    server.quit()'''

#dciiwtkzifbhacxf

import smtplib
from smtplib import SMTP
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('srivanisistla5@gmail.com','dciiwtkzifbhacxf')
    msg=EmailMessage()
    msg['From']='srivanisistla5@gmail.com'
    msg['Subject']=subject
    msg['To']=to
    msg.set_content(body)
    server.send_message(msg)
    server.quit()

    







        
    
