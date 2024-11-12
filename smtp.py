import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

otp = random.randint(1111,9999)

smtp_server = "smtp.gmail.com"
smtp_port = 587
mailusername = "bhuvanachowdary8125@gmail.com"
mailpassword = "uxlm aayv xvou wqoq"
from_email = "bhuvanachowdary8125@gmail.com"
to_email = input("Enter mail id: ")
subject = "OTP For Verification"
body = f"Otp for Verification is {otp}\n\nThanks for choosing codegnan"
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(body,'plain'))

server = smtplib.SMTP(smtp_server,smtp_port)
server.starttls()
server.login(mailusername,mailpassword)
server.send_message(msg)

verifyotp = int(input(f"Enter OTP sent to your mail ({to_email}): "))
if verifyotp == otp:
    print("Verification sucessfull")
else:
    print("Verification Failed")
