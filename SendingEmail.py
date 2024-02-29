from email.message import EmailMessage
import ssl
import smtplib
from Passwords import emailPassword



email_sender = 'mustaphaossama2000@gmail.com'

def sendEmail(senderEmail, reciverEmail, subject, body):
    em = EmailMessage()
    senderEmail = email_sender
    em['From'] = senderEmail
    em['To'] = reciverEmail
    em['subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(senderEmail, emailPassword)
        smtp.sendmail(senderEmail,reciverEmail,em.as_string())