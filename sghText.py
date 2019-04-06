from twilio.rest import Client
from sghDB import *
from sghMeals import generateMealsCheckString, updateAllMeals
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


# issue: the quickstart guide for getting receiving to work wasn't clear, the video was better


def convertDHArrToNums(dhArr):
    dhResult = []
    for dh in dhArr:
        if dh == "C9/C10" or dh == "College9/College10" or dh == "9/10" or dh == "College 9/College 10":
            dhResult.append(0)
        elif dh == "Cowell/Stevenson" or dh == "Cow/Stev" or dh == "C/St" or dh == "Co/S":
            dhResult.append(1)
        elif dh == "Crown/Merrill" or dh == "Cro/Mer" or dh == "Cr/Me" or dh == "Cr/M":
            dhResult.append(2)
        elif dh == "Porter/Kresge" or dh == "Por/Kres" or dh == "P/K" or dh == "Po/Kr":
            dhResult.append(3)
        elif dh == "Carson/Oakes" or dh == "Ca/Oa" or dh == "Car/Oak" or dh == "Ca/O":
            dhResult.append(4)

    return dhResult

def sendDailyNotificationToUser(number):
    foodString = getUserFoodString(number)
    dhString = getUserDiningHallsString(number)

    foodArr = getEntryArray(foodString)
    dhArr = convertDHArrToNums(getEntryArray(dhString))
    print(foodArr)

    result = generateMealsCheckString(foodArr, dhArr, "current")

    if not result:
        print("No result string for " + number)
    else:
        sendText(number, result)

def sendAllDailyNotifications(numList):
    for num in numList:
        sendDailyNotificationToUser(num)

def sendHelpMessage(number):
    sendText(number, "Slug Grub Hub Functions:\n\n Add fav food: ADD FOOD {food1, food2,...}\nAdd fav dining hall: ADD DH {dh1, dh2,...}\nDisplay SGH Functions: HELP\n\nSlug Grub Hub will notify you daily at 9am and weekly on Sunday at 8pm.")


resultArr = getNumberArr()

print(resultArr)
# updateAllMeals()
# sendDailyNotificationToUser('+14086211865')
