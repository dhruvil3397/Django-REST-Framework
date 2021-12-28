# Sending an email with the data
import smtplib
from email.message import EmailMessage

msg =  EmailMessage()
msg['Subject'] = 'Welcome'
msg['From'] = ''
msg['To'] = 'ds@yopmail.com'
msg.set_content('Hello, I am Dhruvil soni')

with smtplib.SMTP_SSL('smtp.gmail.com',465) as server :
    server.login("","")
    server.send_message(msg)

print("Email Sent!!!")
