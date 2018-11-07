from twilio.rest import Client

account_sid = 'ACe363635a022a5e400703021bcfe99272'
auth_token = '3ec886b86657c33be81b1bf1a042512b'

def sendText(toNumber, message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body = message,
        from_ ='+14805317720',
        to = toNumber
    )
