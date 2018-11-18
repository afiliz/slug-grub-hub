from twilio.rest import Client
import os

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

def sendText(toNumber, message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body = message,
        from_ = os.environ.get('TWILIO_SGH_NUMBER'),
        to = toNumber
    )
