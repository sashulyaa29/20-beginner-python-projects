from email.message import EmailMessage
# Пароль берём из отдельного файла
from app2 import password
import ssl
import smtplib

email_sender = "fakemail@gmail.com"
email_password = password
email_receiver = ""

subject = "Не забудьте подписаться"
body = """
Когда будете смотреть видео, пожалуйста нажмите кнопку подписаться
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())