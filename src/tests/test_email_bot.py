
from ..email_bot import EmailBot
import pytest

def test_fetch_message():
    test = EmailBot()
    test.fetch_messages()
    test.messages

def test_display_messages():
    test = EmailBot()
    test.fetch_messages()
    test.display_messages()


