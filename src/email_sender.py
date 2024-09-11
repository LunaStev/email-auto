# File responsible for the email sending functionality

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from src.config.settings import *

# Function to send an email
def send_email(subject, body, to_email):
    # Compose the email
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject

    # Add the email body
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server, login, and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls() # Start a secure connection
            server.login(SENDER_EMAIL, SENDER_PASSWORD) # Log in
            server.sendmail(SENDER_EMAIL, to_email, msg.as_string()) # Send the email
        print("Email sent successfully.")
        return True
    except Exception as event:
        # Print an error if the email sending files
        print(f'Failed to send email: {event}')
        return False