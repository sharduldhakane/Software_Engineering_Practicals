import random
import re
import smtplib
sender_email = "anyscientist2002@gmail.com"
sender_password = "wqen tpbi yicl pnrq"
reciever_email = str(input("Enter E-mail ID to recieve OTP "))
otp = ''
for i in range(5):
    otp += str(random.randint(0, 9))
try:
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login(sender_email, sender_password)
    message = "OTP is " + str(otp)
    smtp.sendmail(sender_email, reciever_email, message)
    smtp.quit()
    print("Email sent successfully!")
except Exception as ex:
    print("Something went wrong....", ex)
reciever_OTP = str(input("Enter the OTP you recieved: "))
if reciever_OTP == otp:
    print("OTP Validated Successfully!")
else:
    print("Please Enter a valid OTP!!!")
