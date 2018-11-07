from twilio.rest import Client

account_sid = ''
auth_token = ''

def sendText(toNumber, message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body = message,
        from_ ='+',
        to = toNumber
    )
