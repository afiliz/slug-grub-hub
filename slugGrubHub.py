from twilio.rest import Client
import datetime
from sghURLS import *
from sghMeals import *

# TODO: see if moving dictionaries to database would be better
# TODO:
# - Add documentation
# - Add scheduling - day and College
# - add mysql database for phone users
# - add start and stop subscription for users
# - add favorite per user

account_sid = 'account_sid'
auth_token = 'auth_token'

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

def sendText(toNumber, message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body = message,
        from_ ='+18316071845',
        to = toNumber
    )

# getAllMeals()
getMeals(C9_C10_URLS[4], c9_c10_breakfast["current"], c9_c10_lunch["current"], c9_c10_dinner["current"], c9_c10_lateNight["current"])

print(c9_c10_breakfast["current"])
print(c9_c10_lunch["current"])
print(c9_c10_dinner["current"])
print(c9_c10_lateNight["current"])
print(C9_C10_URLS[4])

# Special thanks to Mom for the "Hub" part of the Slug Grub Hub name
# Also special thanks to some of my friends for helping beta test Slug Grub Hub