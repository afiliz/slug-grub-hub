import datetime
import os
from sghData import *
from sghText import sendHelpMessage
from sghDB import *
from sghMeals import updateAllMeals, generateMealsCheckString
from sghText import sendText
from flask import Flask, request, redirect, session
from twilio.twiml.messaging_response import MessagingResponse

# TODO: see if moving dictionaries to database would be better
# TODO:
# - Add documentation
# - Add scheduling - day and College
# - add mysql database for phone users
# - add start and stop subscription for users
# - add favorite per user

def updateDates():
    global currentDate, plusOneDate, plusTwoDate, plusThreeDate, plusFourDate, plusFiveDate, plusSixDate, plusSevenDate 
    currentDate = datetime.datetime.now()
    plusOneDate = currentDate + datetime.timedelta(days = 1)
    plusTwoDate = currentDate + datetime.timedelta(days = 2)
    plusThreeDate = currentDate + datetime.timedelta(days = 3)
    plusFourDate = currentDate + datetime.timedelta(days = 4)
    plusFiveDate = currentDate + datetime.timedelta(days = 5)
    plusSixDate = currentDate + datetime.timedelta(days = 6)
    plusSevenDate = currentDate + datetime.timedelta(days = 7)

# updateAllMeals()

# # sendText(14086211865, "Test texterino")

# # for x in range(0, 8):
# #     print(x)
# # # getMeals(C9_C10_URLS[4], c9_c10_breakfast["current"], c9_c10_lunch["current"], c9_c10_dinner["current"], c9_c10_lateNight["current"])



# print(c9_c10_breakfast["current"])
# print(c9_c10_lunch["current"])
# print(c9_c10_dinner["current"])
# print(c9_c10_lateNight["current"])
# print(C9_C10_URLS[0])

# print(cow_stev_breakfast["current"])
# print(cow_stev_lunch["current"])
# print(cow_stev_dinner["current"])
# print(cow_stev_lateNight["current"])
# print(COW_STEV_URLS[0])

# print(port_kres_breakfast["current"])
# print(port_kres_lunch["current"])
# print(port_kres_dinner["current"])
# print(port_kres_lateNight["current"])
# print(PORT_KRES_URLS[0])

isInApp = False

# TODO: May need to use resp.message() instead of sendText() here

# receives texts and makes appropriate responses
app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    phone = request.values.get('From', None)
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    isUser = checkForUser(phone)

    if not isUser:
        sendText(phone, "Thanks for using Slug Grub Hub! Please tell me what I should call you.")
        session['newUser'] = False


    if not session['newUser'] and isInApp == True:
        createNewUser(body, phone)
        sendText(phone, "Great to meet you " + body + "! Here's how to use Slug Grub Hub:")
        sendHelpMessage(phone)

    if isUser:
        command = body.split(" ")
        if command[1] == "DH" or command[1] == "dh":
            command.pop(0)
            command.pop(0)
            newDH = ''.join(command)
            addDHToUser(newDH, phone)
            sendText(phone, "Added " + newDH + " to your favorite dining halls.")
        if command[1] == "food" or command[1] == "Food" or command[1] == "FOOD":
            command.pop(0)
            command.pop(0)
            newFood = ''.join(command)
            addFoodToUser(newFood, phone)
            sendText(phone, "Added " + newFood + " to your favorite foods.")

    

    # Determine the right reply for this message
    # if body == 'hello':
    #     print(phone)
    #     resp.message("Hi!" + phone)
    # elif body == 'bye':
    #     resp.message("Goodbye")

    isInApp = True

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

# meals = ["tomate"]
# dhs = [0, 1, 3]

# result = generateMealsCheckString(meals, dhs, "current")

# print(result)

# if not result:
#     print("no result")
# sendText(os.environ.get('PERSONAL_NUMBER'), result)
# #times = checkMealInDH("Steamed Rice", 1, "plusSeven")
# result = checkAllMealsInDH(meals, 1, "plusSeven")
# print(result)

# print(C9_C10_URLS[4])
# print(URLS)


# Special thanks to my Mom for the "Hub" part of the Slug Grub Hub name (even though I realized Grub Hub was a thing after I created the repo)
# Also special thanks to some of my friends for helping beta test Slug Grub Hub
