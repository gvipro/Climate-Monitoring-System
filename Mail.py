import smtplib #Library to login to to gmail account
import time #Time functions
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#Gmail login details
gmail_username = 'smartberrypi2021@gmail.com' #change this to match your gmail account
gmail_password = '9907021405Aa'  #change this to match your gmail password

#Email Variables
SMTPserver = 'smtp.gmail.com' #Email Server 
SMTPport   = 587 #Server Port 


class Emailer:
    def sendMail(self):
        
        sendTo           = 'up898793@myport.ac.uk' 
        emailSubject     = "Climate changes!"
        emailContent     = "Units have changed " + time.ctime() + "." + " login online to check status."
        
        #Create Headers
        emailData            = MIMEMultipart() #Create an object from MultiPart
        emailData['Subject'] = emailSubject #
        emailData['To']      = sendTo
        emailData['From']    = gmail_username
 
        #Attach our text data  
        emailData.attach(MIMEText(emailContent))
  
        #Connect to Gmail Server
        session = smtplib.SMTP(SMTPserver, SMTPport)
        session.ehlo()
        session.starttls()
        session.ehlo()
  
        #Login to Gmail using the specified username and password
        session.login(gmail_username, gmail_password)
  
        #Send Email & Exit
        session.sendmail(gmail_username, sendTo, emailData.as_string())
        session.quit