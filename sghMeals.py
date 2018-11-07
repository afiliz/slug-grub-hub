import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import pickle
from sghData import *

def getMeals(url, breakfast, lunch, dinner, latenight):
    resp = urllib.request.urlopen(url).read()

    soup = BeautifulSoup(resp, 'html.parser')

    table = soup.find('table')
    myTables = soup.findAll("table", {"cellspacing": 1}) #get the breakfast, lunch, and dinner tables, all with cellspacing: 0
    
    for x, table in enumerate(myTables):
        myDivs = table.findAll("div", {"class": "menusamprecipes"})
        
        for div in myDivs:
            if x == 0:
                breakfast.append(div.text)
            elif x == 1:
                lunch.append(div.text)
            elif x == 2:
                dinner.append(div.text)
            elif x == 3:
                latenight.append(div.text)

def getDiningHallMeals(dhURLS, dhBreakfast, dhLunch, dhDinner, dhLateNight):
    print("Got meals")
    for x in range (0, 8):
        key = ""
        if x == 0:
            key = "current"
        elif x == 1:
            key = "plusOne"
        elif x == 2:
            key = "plusTwo"
        elif x == 3:
            key = "plusThree"
        elif x == 4:
            key = "plusFour"
        elif x == 5:
            key = "plusFive"
        elif x == 6:
            key = "plusSix"
        elif x == 7:
            key = "plusSeven"
        # else:
        #     key = ""
        getMeals(dhURLS[x], dhBreakfast[key], dhLunch[key], dhDinner[key], dhLateNight[key])

# now working!
def updateAllMeals():
    for x, urlList in enumerate(URLS):
        getDiningHallMeals(urlList, diningHalls[x][0], diningHalls[x][1], diningHalls[x][2], diningHalls[x][3])
        

def checkMealInDH(meal, dh, plusWeekDay):
    dhBreakfast = diningHalls[dh][0][plusWeekDay]
    dhLunch = diningHalls[dh][1][plusWeekDay]
    dhDinner = diningHalls[dh][2][plusWeekDay]
    dhLateNight = diningHalls[dh][3][plusWeekDay]

    result = []

    if meal in dhBreakfast:
        result.append("breakfast")

    if meal in dhLunch:
        result.append("lunch")

    if meal in dhDinner:
        result.append("dinner")

    if meal in dhLateNight:
        result.append("lateNight")

    return result

def checkAllMealsInDH(meals, dh, plusWeekDay):
    result = []

    for meal in meals:
        times = checkMealInDH(meal, dh, plusWeekDay)
        if not times:
            continue
        else:
            for time in times:
                entry = (meal, dh, time)
                result.append(entry)

    return result

dhNames = {}
dhNames[0] = "9/10"
dhNames[1] = "Co/S"
dhNames[2] = "Cr/M"
dhNames[3] = "P/K"
dhNames[4] = "Ca/O"

def turnTupleIntoString(tuple):
    result = tuple[0] + " - " + dhNames[tuple[1]] + "\n"
    trueResult = ""
    if tuple[2] == "breakfast":
        trueResult = "yes"
    else:
        trueResult = "no"
    # print(tuple[2])
    # print(result)
    # print(trueResult)
    if tuple[2] == "breakfast":
        return [0, result]
        # print("added breakfast")
    if tuple[2] == "lunch":
        return [1, result]
        # print("added lunch")
    if tuple[2] == "dinner":
        return [2, result]
        # print("added dinner")
    if tuple[2] == "lateNight":
        return [3, result]
        # print("added latenight")


def getMealsCheckString(meals, dhs, plusWeekDay):
    breakfastString = "Breakfast:\n"
    lunchString = "Lunch:\n"
    dinnerString = "Dinner:\n"
    lateNightString = "Late Night:\n"

    for dh in dhs:
        mealsForDH = checkAllMealsInDH(meals, dh, plusWeekDay)
        # print(mealsForDH)
        for tupl in mealsForDH:
            print(tupl)
            resultString = turnTupleIntoString(tupl)
            if resultString[0] == 0:
                breakfastString += resultString[1]
            if resultString[0] == 1:
                lunchString += resultString[1]
            if resultString[0] == 2:
                dinnerString += resultString[1]
            if resultString[0] == 3:
                lateNightString += resultString[1]

    result = ""

    if breakfastString != "Breakfast:\n":
        result += breakfastString
    if lunchString != "Lunch:\n":
        result += lunchString
    if dinnerString != "Dinner:\n":
        result += dinnerString
    if lateNightString != "Late Night:\n":
        result += lateNightString

    return result

# to implement
# def pickleAllMeals():
#     with open(newfile, 'wb') as fi:
#         # dump your data into the file
#         pickle.dump(diningHalls, fi)

