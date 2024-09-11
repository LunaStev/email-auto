# Scheduler for periodically executing email sending

import schedule, time
from src.email_sender import send_email

# Function to send a weekly newsletter
def send_newsletter():
    send_email('Weekly Newsletter', 'Here is the weekly update!', 'sobi15@naver.com')

# Function to start the scheduler
def start_scheduler():
    # Schedule the newsletter to be sent every Monday at 9:00 AM
    schedule.every().monday.at("09:00")

    print("Scheduler started. Waiting for tasks...")

    # Infinite loop to keep the scheduler running
    while True:
        schedule.run_pending()
        time.sleep(1)