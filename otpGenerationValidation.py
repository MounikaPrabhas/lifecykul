import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
from twilio.rest import Client
import math


account_sid = 'ACbc037be290d46857be30c2b3c78fdd9e' # Replace with your Twilio account SID
auth_token = '9e5c7797a35c9c5a056c0a54842eacc8' # Replace with your Twilio auth token
twilio_number = '+15076232677'
client = Client(account_sid, auth_token)



# Generate OTP
def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


# Send OTP via email
def sendOTPviaEmail(otp, recipient_email):
    sender_email = "your_sender_email@gmail.com"
    password = "your_email_password"
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = "Your OTP for verification"
    body = "Your OTP is " + otp
    message.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    text = message.as_string()
    server.sendmail(sender_email, recipient_email, text)
    server.quit()


# Send OTP via SMS
def sendOTPviaSMS(otp, recipient_mobile_number):
    account_sid = 'ACbc037be290d46857be30c2b3c78fdd9e' # Replace with your Twilio account SID
    auth_token = '9e5c7797a35c9c5a056c0a54842eacc8'
    client = Client(account_sid, auth_token)
    client.messages.create(
        body="Your OTP is " + otp,
        from_=twilio_number,
        to=recipient_mobile_number
    )

# Verify OTP
def verifyOTP(otp, user_input):
    if otp == user_input:
        return True
    else:
        return False
