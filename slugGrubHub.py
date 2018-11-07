import datetime
from sghData import *
from sghMeals import *
from sghText import sendText

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

updateAllMeals()

# sendText(14086211865, "Test texterino")

# for x in range(0, 8):
#     print(x)
# # getMeals(C9_C10_URLS[4], c9_c10_breakfast["current"], c9_c10_lunch["current"], c9_c10_dinner["current"], c9_c10_lateNight["current"])



print(c9_c10_breakfast["current"])
print(c9_c10_lunch["current"])
print(c9_c10_dinner["current"])
print(c9_c10_lateNight["current"])
print(C9_C10_URLS[0])

print(cow_stev_breakfast["current"])
print(cow_stev_lunch["current"])
print(cow_stev_dinner["current"])
print(cow_stev_lateNight["current"])
print(COW_STEV_URLS[0])

print(port_kres_breakfast["current"])
print(port_kres_lunch["current"])
print(port_kres_dinner["current"])
print(port_kres_lateNight["current"])
print(PORT_KRES_URLS[0])



meals = ["Belgian Waffles", "Cage Free Scrambled Eggs", "Cheese Pizza", "BBQ Wings"]
dhs = [0, 1, 3]

result = getMealsCheckString(meals, dhs, "current")

print(result)

# #times = checkMealInDH("Steamed Rice", 1, "plusSeven")
# result = checkAllMealsInDH(meals, 1, "plusSeven")
# print(result)

# print(C9_C10_URLS[4])
# print(URLS)

# Special thanks to Mom for the "Hub" part of the Slug Grub Hub name (even though I realized Grub Hub was a thing after I created the repo)
# Also special thanks to some of my friends for helping beta test Slug Grub Hub
