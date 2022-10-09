from datetime import datetime
import hashlib
from typing import Optional
from src.cruds import users as u_cruds
from src.schemas import users as u_schemas
from sqlalchemy.orm import Session
import os
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def email_sender(receiver_email: str, message_html: str, topic: str):
    
    port = os.environ["PORT"]
    sender_email = os.environ["SENDER_EMAIL"]
    password = os.environ["EMAIL_PASS"]
    message = MIMEMultipart("alternative")
    message['Subject'] = topic
    message['From'] = "Equipe Paylog"
    message['To'] = receiver_email

    html = MIMEText(message_html, 'html')
    message.attach(html)
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
    return "success"