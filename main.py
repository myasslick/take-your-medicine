import datetime
import os

from twilio.rest import Client

CHECKIN_MSG_TEMPLATE = (
    '{date} ({day})\n' +
    'Please confirm you have taken your medicine today (Yes/No).'
)

def make_checkin_message():
    today = datetime.datetime.today()
    weekday = today.strftime("%a")
    date = "%s/%s" %(today.month, today.day)

    return CHECKIN_MSG_TEMPLATE.format(date=date,
        day=weekday)

if __name__ == "__main__":
    account = os.environ["TWILIO_ACCOUNT"]
    token = os.environ["TWILIO_AUTH_TOKEN"]
    twilio_number = os.environ["TWILIO_PHONE_NUMBER"]
    home_number = os.environ["TWILIO_HOME_PHONE_NUMBER"]

    client = Client(account, token)
    checkin_message = make_checkin_message()

    message = client.messages.create(from_=twilio_number,
        to=home_number, body=checkin_message)
