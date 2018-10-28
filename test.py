from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    phone = request.values.get('From', None)
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body == 'hello':
        print(phone)
        resp.message("Hi!" + phone)
    elif body == 'bye':
        resp.message("Goodbye")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)


# from flask import Flask, request, redirect
# from twilio.twiml.messaging_response import MessagingResponse

# app = Flask(__name__)

# @app.route("/sms", methods=['GET', 'POST'])
# def sms_reply():
#     """Respond to incoming calls with a simple text message."""
#     # Start our TwiML response
#     resp = MessagingResponse()

#     # Add a message
#     resp.message("The Robots are coming! Head for the hills!")

#     return str(resp)

# if __name__ == "__main__":
#     app.run(debug=True)


# import mysql.connector

# test = {}
# test["yeet"] = []
# test["yeet"].append("yeeeeet")


# print(test["yeet"])

# # mydb = mysql.connector.connect(
# #   host="localhost",
# #   user="root",
# #   passwd="MySQL0l09802",
# #   database="sluggrubhub"
# # )

# # mycursor = mydb.cursor()

# # mycursor.execute("SHOW TABLES")

# # for x in mycursor:
# #   print(x)

# # for x in mycursor:
# #   print(x) 

# # import datetime


# # currentDate = datetime.datetime.now()
# # plusOne = currentDate + datetime.timedelta(days = 2)

# # print(currentDate)
# # print(plusOne)


