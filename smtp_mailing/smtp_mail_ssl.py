#!/usr/bin/python

import smtplib, ssl
from email.mime.text import MIMEText

sender = 'creedfarmone@outlook.com'
receivers = ['trainingcellid@proton.me']

port = 587
user = 'creedfarmone@outlook.com'
password = 'creed5farm@one'

msg = MIMEText('This is test mail')

msg['Subject'] = 'Test mail'
msg['From'] = 'creedfarmone@outlook.com'
msg['To'] = 'trainingcellid@proton.me'

#context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.live.com", port) as server:

    server.login(user, password)
    server.sendmail(sender, receivers, msg.as_string())
    print('mail successfully sent')
