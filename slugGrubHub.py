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



print(c9_c10_breakfast["plusThree"])
print(c9_c10_lunch["plusThree"])
print(c9_c10_dinner["plusThree"])
print(c9_c10_lateNight["plusThree"])
print(C9_C10_URLS[3])

print(port_kres_breakfast["plusFour"])
print(port_kres_lunch["plusFour"])
print(port_kres_dinner["plusFour"])
print(port_kres_lateNight["plusFour"])
print(PORT_KRES_URLS[4])

print(cow_stev_breakfast["plusSeven"])
print(cow_stev_lunch["plusSeven"])
print(cow_stev_dinner["plusSeven"])
print(cow_stev_lateNight["plusSeven"])
print(COW_STEV_URLS[7])



# print(C9_C10_URLS[4])
# print(URLS)

# Special thanks to Mom for the "Hub" part of the Slug Grub Hub name (even though I realized Grub Hub was a thing after I created the repo)
# Also special thanks to some of my friends for helping beta test Slug Grub Hub
