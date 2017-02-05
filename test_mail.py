# Update the four lines after where it says Settings: below
# With your email address, password, smtp server and 
# one of the three following encryption Options:
#   1 = No encryption
#   2 = SSL
#   3 = TLS

#Settings:
YourEmailAddress = "abk7997@gmail.com"
YourPassword     = "abk_MAILSTUFF_1906"
smtp_server      = "smtp.gmail.com"
Option = 2

#Do not change any of the following code
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import smtplib

#Sender/Recipient Information
addr_to = YourEmailAddress
addr_from = YourEmailAddress    
attachment = "test" #Text message

#Image-specific code
fp = open(attachment, 'rb')
img = MIMEImage(fp.read())
fp.close()
img.add_header("Content-ID", "<{}>".format(attachment))

msg = MIMEMultipart()
msg['To'] = YourEmailAddress
msg['From'] = "Pi Security"
msg['Subject'] = 'PrivateEyePi Alert'

#Text-specific code
msg.attach(MIMEText(attachment))
msg.attach(img)

#Option 1 - No Encryption
if Option==1:
        s = smtplib.SMTP(smtp_server)
elif Option==2:
#Option 2 - SSL
        s = smtplib.SMTP_SSL(smtp_server, 465)
elif Option==3:
#Option 3 - TLS
        s = smtplib.SMTP(smtp_server,587)
        s.ehlo()
        s.starttls()
        s.ehlo()
else:
        s = smtplib.SMTP(smtp_server)
s.login(YourEmailAddress,YourPassword)
s.sendmail(YourEmailAddress, YourEmailAddress, msg.as_string()) #SEND 
s.quit()
