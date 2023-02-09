import smtplib

sender = "sender@protonmail.com"
receiver = "reciever@proton.me"

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

This is a test e-mail message."""

with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
    server.login("serverid", "serverpass")
    server.sendmail(sender, receiver, message)
    print("done")