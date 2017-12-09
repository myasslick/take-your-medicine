import os

from twilio.rest import Client

if __name__ == "__main__":
    account = os.environ["TWILIO_ACCOUNT"]
    token = os.environ["TWILIO_TOKEN"]
    sender_number = os.environ["TWILIO_SENDER_PHONE_NUMBER"]
    receiver_number = os.environ["TWILIO_RECIVER_PHONE_NUMBER"]

    client = Client()
