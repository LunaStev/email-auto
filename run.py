from src.email_sender import send_email
from src.scheduler import start_scheduler

if __name__ == "__main__":
    send_email('Test Subject', 'Test Body', 'example@example.com')

    start_scheduler()