import random
import re
import smtplib

reciever_email = 'aryannyadav2002@gmail.com' #str(input("Enter E-mail ID to recieve OTP "))
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
sender_email = "anyscientist2002@gmail.com"
sender_password = "wqen tpbi yicl pnrq"
def validate_email():
    if re.fullmatch(regex, reciever_email):
        # print("E-Mail is Valid")
        # generate_OTP()
        return True
    else:
        # print("E-Mail ia Invalid!")
        return False


def generate_OTP():
    otp = ''
    for i in range(4):
        otp += str(random.randint(0, 9))
    # sendOTP(otp)
    return otp


def sendOTP(otp):
    try:
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login(sender_email, sender_password)
        message = "OTP is "+str(otp)
        smtp.sendmail(sender_email, reciever_email, message)
        smtp.quit()
        # print("Email sent successfully!")
        # validate_OTP(otp)
        return True
    except Exception as ex:
        # print("Something went wrong....", ex)
        return False


def validate_OTP(otp):
    reciever_OTP = str(input("Enter the OTP you recieved: "))
    if reciever_OTP == otp:
        return True
        # print("OTP Validated Successfully!")
    else:
        return False
        # print("Please Enter a valid OTP!!!")
#Do not hard code variables i.e. use variables instead of direct variables
#Arrange imported libraries in ascending order
#validate_email()
