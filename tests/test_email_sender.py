# tests/test_email_sender.py

import pytest
from src.email_sender import send_email

def test_send_email():
    result = send_email('Test Subject', 'Test Body', 'email@test_domain.com')

    assert result == True