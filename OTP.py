import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import password1 as p1
import random
inp=input('Entr Reciver mail id:')
subj=input('Subject')
a=random.randint(1001,9999)
mail_content = 'OTP for request From KKKweb:'+' '+str(a)
sender_address = 'webscrapingcs12345@gmail.com'
sender_pass = p1.Pass()
receiver_address = inp
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = ''
message.attach(MIMEText(mail_content, 'plain'))
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls() 
session.login(sender_address, sender_pass)
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Sucess')
