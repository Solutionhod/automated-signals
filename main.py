from email.message import EmailMessage
import ssl
import smtplib

email_sender = "email@gmail.com"
email_password = "password101"
subject = "Your Subject"
body = """
Hi there, 
This is a testing code. Congratulations! 
You just won $1,000,000.00. Click on this link to make claim: https://www.nybenonly.com 
"""
email_receiver = ""
with open("contacts.txt", "r") as contacts_file:
    emails = contacts_file.readlines()
em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body)
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as connection:
    connection.login(email_sender, email_password)
    for email in emails:
        email_receiver = email.strip()
        result = connection.sendmail(email_sender, email_receiver, em.as_string())
