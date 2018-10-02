import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
from twilio.rest import Client
import datetime

# TODO: see if moving dictionaries to database would be better
# TODO:
# - Add documentation
# - Add scheduling - day and College
# - add mysql database for phone users
# - add start and stop subscription for users
# - add favorite per user

account_sid = 'account_sid'
auth_token = 'auth_token'

currentDate = datetime.datetime.now()
plusOneDate = currentDate + datetime.timedelta(days = 1)
plusTwoDate = currentDate + datetime.timedelta(days = 2)
plusThreeDate = currentDate + datetime.timedelta(days = 3)
plusFourDate = currentDate + datetime.timedelta(days = 4)
plusFiveDate = currentDate + datetime.timedelta(days = 5)
plusSixDate = currentDate + datetime.timedelta(days = 6)
plusSevenDate = currentDate + datetime.timedelta(days = 7)

# Lists containing all of the college dining halls' urls
# Uses datetime to get the URLs of all the days of the week
# Might switch this all to a database
C9_C10_URLS = ['https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(currentDate.month) + '%2F' + str(currentDate.day) + '%2F' + str(currentDate.year) + '&locationNum=40&locationName=%20Colleges+Nine+%26+Ten+Dining+Hall&naFlag=', 
               'https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(plusOneDate.month) + '%2F' + str(plusOneDate.day) + '%2F' + str(plusOneDate.year) + '&locationNum=40&locationName=%20Colleges+Nine+%26+Ten+Dining+Hall&naFlag=',
               'https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(plusTwoDate.month) + '%2F' + str(plusTwoDate.day) + '%2F' + str(plusTwoDate.year) + '&locationNum=40&locationName=%20Colleges+Nine+%26+Ten+Dining+Hall&naFlag=',
               'https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(plusThreeDate.month) + '%2F' + str(plusThreeDate.day) + '%2F' + str(plusThreeDate.year) + '&locationNum=40&locationName=%20Colleges+Nine+%26+Ten+Dining+Hall&naFlag=',
               'https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(plusFourDate.month) + '%2F' + str(plusFourDate.day) + '%2F' + str(plusFourDate.year) + '&locationNum=40&locationName=%20Colleges+Nine+%26+Ten+Dining+Hall&naFlag=',
               'https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(plusFiveDate.month) + '%2F' + str(plusFiveDate.day) + '%2F' + str(plusFiveDate.year) + '&locationNum=40&locationName=%20Colleges+Nine+%26+Ten+Dining+Hall&naFlag=',
               'https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(plusSixDate.month) + '%2F' + str(plusSixDate.day) + '%2F' + str(plusSixDate.year) + '&locationNum=40&locationName=%20Colleges+Nine+%26+Ten+Dining+Hall&naFlag=',
               'https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(plusSevenDate.month) + '%2F' + str(plusSevenDate.day) + '%2F' + str(plusSevenDate.year) + '&locationNum=40&locationName=%20Colleges+Nine+%26+Ten+Dining+Hall&naFlag='
]

COW_STEV_URLS = ['https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(currentDate.month) + '%2F' + str(currentDate.day) + '%2F' + str(currentDate.year) + '&locationNum=05&locationName=Cowell+Stevenson+Dining+Hall&naFlag=', 
               'https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(plusOneDate.month) + '%2F' + str(plusOneDate.day) + '%2F' + str(plusOneDate.year) + '&locationNum=05&locationName=Cowell+Stevenson+Dining+Hall&naFlag=',
               'https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(plusTwoDate.month) + '%2F' + str(plusTwoDate.day) + '%2F' + str(plusTwoDate.year) + '&locationNum=05&locationName=Cowell+Stevenson+Dining+Hall&naFlag=',
               'https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(plusThreeDate.month) + '%2F' + str(plusThreeDate.day) + '%2F' + str(plusThreeDate.year) + '&locationNum=05&locationName=Cowell+Stevenson+Dining+Hall&naFlag=',
               'https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(plusFourDate.month) + '%2F' + str(plusFourDate.day) + '%2F' + str(plusFourDate.year) + '&locationNum=05&locationName=Cowell+Stevenson+Dining+Hall&naFlag=',
               'https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(plusFiveDate.month) + '%2F' + str(plusFiveDate.day) + '%2F' + str(plusFiveDate.year) + '&locationNum=05&locationName=Cowell+Stevenson+Dining+Hall&naFlag=',
               'https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(plusSixDate.month) + '%2F' + str(plusSixDate.day) + '%2F' + str(plusSixDate.year) + '&locationNum=05&locationName=Cowell+Stevenson+Dining+Hall&naFlag=',
               'https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(plusSevenDate.month) + '%2F' + str(plusSevenDate.day) + '%2F' + str(plusSevenDate.year) + '&locationNum=05&locationName=Cowell+Stevenson+Dining+Hall&naFlag='
]

CROW_MER_URLS = ['https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(currentDate.month) + '%2F' + str(currentDate.day) + '%2F' + str(currentDate.year) + '&locationNum=20&locationName=Crown+Merrill+Dining+Hall&naFlag=', 
               'https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(plusOneDate.month) + '%2F' + str(plusOneDate.day) + '%2F' + str(plusOneDate.year) + '&locationNum=20&locationName=Crown+Merrill+Dining+Hall&naFlag=',
               'https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(plusTwoDate.month) + '%2F' + str(plusTwoDate.day) + '%2F' + str(plusTwoDate.year) + '&locationNum=20&locationName=Crown+Merrill+Dining+Hall&naFlag=',
               'https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(plusThreeDate.month) + '%2F' + str(plusThreeDate.day) + '%2F' + str(plusThreeDate.year) + '&locationNum=20&locationName=Crown+Merrill+Dining+Hall&naFlag=',
               'https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(plusFourDate.month) + '%2F' + str(plusFourDate.day) + '%2F' + str(plusFourDate.year) + '&locationNum=20&locationName=Crown+Merrill+Dining+Hall&naFlag=',
               'https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(plusFiveDate.month) + '%2F' + str(plusFiveDate.day) + '%2F' + str(plusFiveDate.year) + '&locationNum=20&locationName=Crown+Merrill+Dining+Hall&naFlag=',
               'https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(plusSixDate.month) + '%2F' + str(plusSixDate.day) + '%2F' + str(plusSixDate.year) + '&locationNum=20&locationName=Crown+Merrill+Dining+Hall&naFlag=',
               'https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(plusSevenDate.month) + '%2F' + str(plusSevenDate.day) + '%2F' + str(plusSevenDate.year) + '&locationNum=20&locationName=Crown+Merrill+Dining+Hall&naFlag='
]

PORT_KRES_URLS = ['https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(currentDate.month) + '%2F' + str(currentDate.day) + '%2F' + str(currentDate.year) + '&locationNum=25&locationName=Porter+Kresge+Dining+Hall&naFlag=', 
               'https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(plusOneDate.month) + '%2F' + str(plusOneDate.day) + '%2F' + str(plusOneDate.year) + '&locationNum=25&locationName=Porter+Kresge+Dining+Hall&naFlag=',
               'https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(plusTwoDate.month) + '%2F' + str(plusTwoDate.day) + '%2F' + str(plusTwoDate.year) + '&locationNum=25&locationName=Porter+Kresge+Dining+Hall&naFlag=',
               'https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(plusThreeDate.month) + '%2F' + str(plusThreeDate.day) + '%2F' + str(plusThreeDate.year) + '&locationNum=25&locationName=Porter+Kresge+Dining+Hall&naFlag=',
               'https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(plusFourDate.month) + '%2F' + str(plusFourDate.day) + '%2F' + str(plusFourDate.year) + '&locationNum=25&locationName=Porter+Kresge+Dining+Hall&naFlag=',
               'https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(plusFiveDate.month) + '%2F' + str(plusFiveDate.day) + '%2F' + str(plusFiveDate.year) + '&locationNum=25&locationName=Porter+Kresge+Dining+Hall&naFlag=',
               'https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(plusSixDate.month) + '%2F' + str(plusSixDate.day) + '%2F' + str(plusSixDate.year) + '&locationNum=25&locationName=Porter+Kresge+Dining+Hall&naFlag=',
               'https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(plusSevenDate.month) + '%2F' + str(plusSevenDate.day) + '%2F' + str(plusSevenDate.year) + '&locationNum=25&locationName=Porter+Kresge+Dining+Hall&naFlag='
]

CAR_OAK_URLS = ['https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(currentDate.month) + '%2F' + str(currentDate.day) + '%2F' + str(currentDate.year) + '&locationNum=30&locationName=Rachel+Carson+Oakes+Dining+Hall&naFlag=', 
               'https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(plusOneDate.month) + '%2F' + str(plusOneDate.day) + '%2F' + str(plusOneDate.year) + '&locationNum=30&locationName=Rachel+Carson+Oakes+Dining+Hall&naFlag=',
               'https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(plusTwoDate.month) + '%2F' + str(plusTwoDate.day) + '%2F' + str(plusTwoDate.year) + '&locationNum=30&locationName=Rachel+Carson+Oakes+Dining+Hall&naFlag=',
               'https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(plusThreeDate.month) + '%2F' + str(plusThreeDate.day) + '%2F' + str(plusThreeDate.year) + '&locationNum=30&locationName=Rachel+Carson+Oakes+Dining+Hall&naFlag=',
               'https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(plusFourDate.month) + '%2F' + str(plusFourDate.day) + '%2F' + str(plusFourDate.year) + '&locationNum=30&locationName=Rachel+Carson+Oakes+Dining+Hall&naFlag=',
               'https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(plusFiveDate.month) + '%2F' + str(plusFiveDate.day) + '%2F' + str(plusFiveDate.year) + '&locationNum=30&locationName=Rachel+Carson+Oakes+Dining+Hall&naFlag=',
               'https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(plusSixDate.month) + '%2F' + str(plusSixDate.day) + '%2F' + str(plusSixDate.year) + '&locationNum=30&locationName=Rachel+Carson+Oakes+Dining+Hall&naFlag=',
               'https://nutrition.sa.ucsc.edu/menuSamp.asp?myaction=read&sName=&dtdate=' + str(plusSevenDate.month) + '%2F' + str(plusSevenDate.day) + '%2F' + str(plusSevenDate.year) + '&locationNum=30&locationName=Rachel+Carson+Oakes+Dining+Hall&naFlag='
]

# plusTwo = CROW_MER_URLS[7]

# (Unused) Current date urls, doesn't utilize the datetime library
C9_C10_URL = 'https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=40&locationName=Colleges+Nine+%26+Ten+Dining+Hall&sName=&naFlag='
COW_STEV_URL = 'https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=05&locationName=Cowell+Stevenson+Dining+Hall&sName=&naFlag='
CROW_MER_URL = 'https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=20&locationName=Crown+Merrill+Dining+Hall&sName=&naFlag='
PORT_KRES_URL = 'https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=25&locationName=Porter+Kresge+Dining+Hall&sName=&naFlag='
CAR_OAK_URL = 'https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=30&locationName=Rachel+Carson+Oakes+Dining+Hall&sName=&naFlag='
url = ''
favorites = ["Chicken Tenders", "Cheese Pizza"]
URLS = [C9_C10_URL, COW_STEV_URL, CROW_MER_URL, PORT_KRES_URL, CAR_OAK_URL]

#all breakfast, lunch, and dinner meals will be in these lists
breakfast = []
lunch = []
dinner = []

# Each dining hall has 3 dictionaries, each containing keys that hash lists containing meals for each day (Mon, etc)
# Those 3 dictionaries are then contained in 
c9_c10_breakfast = {}
c9_c10_lunch = {}
c9_c10_dinner = {}
C9_C10 = [c9_c10_breakfast, c9_c10_lunch, c9_c10_dinner]
c9_c10_breakfast["current"] = []
c9_c10_breakfast["plusOne"] = []
c9_c10_breakfast["plusTwo"] = []
c9_c10_breakfast["plusThree"] = []
c9_c10_breakfast["plusFour"] = []
c9_c10_breakfast["plusFive"] = []
c9_c10_breakfast["plusSix"] = []
c9_c10_breakfast["plusSeven"] = []
c9_c10_lunch["current"] = []
c9_c10_lunch["plusOne"] = []
c9_c10_lunch["plusTwo"] = []
c9_c10_lunch["plusThree"] = []
c9_c10_lunch["plusFour"] = []
c9_c10_lunch["plusFive"] = []
c9_c10_lunch["plusSix"] = []
c9_c10_lunch["plusSeven"] = []
c9_c10_dinner["current"] = []
c9_c10_dinner["plusOne"] = []
c9_c10_dinner["plusTwo"] = []
c9_c10_dinner["plusThree"] = []
c9_c10_dinner["plusFour"] = []
c9_c10_dinner["plusFive"] = []
c9_c10_dinner["plusSix"] = []
c9_c10_dinner["plusSeven"] = []

cow_stev_breakfast = {}
cow_stev_lunch = {}
cow_stev_dinner = {}
COW_STEV = [cow_stev_breakfast, cow_stev_lunch, cow_stev_dinner]
cow_stev_breakfast["current"] = []
cow_stev_breakfast["plusOne"] = []
cow_stev_breakfast["plusTwo"] = []
cow_stev_breakfast["plusThree"] = []
cow_stev_breakfast["plusFour"] = []
cow_stev_breakfast["plusFive"] = []
cow_stev_breakfast["plusSix"] = []
cow_stev_breakfast["plusSeven"] = []
cow_stev_lunch["current"] = []
cow_stev_lunch["plusOne"] = []
cow_stev_lunch["plusTwo"] = []
cow_stev_lunch["plusThree"] = []
cow_stev_lunch["plusFour"] = []
cow_stev_lunch["plusFive"] = []
cow_stev_lunch["plusSix"] = []
cow_stev_lunch["plusSeven"] = []
cow_stev_dinner["current"] = []
cow_stev_dinner["plusOne"] = []
cow_stev_dinner["plusTwo"] = []
cow_stev_dinner["plusThree"] = []
cow_stev_dinner["plusFour"] = []
cow_stev_dinner["plusFive"] = []
cow_stev_dinner["plusSix"] = []
cow_stev_dinner["plusSeven"] = []

crow_mer_breakfast = {}
crow_mer_lunch = {}
crow_mer_dinner = {}
CROW_MER = [crow_mer_breakfast, crow_mer_lunch, crow_mer_dinner]
crow_mer_breakfast["current"] = []
crow_mer_breakfast["plusOne"] = []
crow_mer_breakfast["plusTwo"] = []
crow_mer_breakfast["plusThree"] = []
crow_mer_breakfast["plusFour"] = []
crow_mer_breakfast["plusFive"] = []
crow_mer_breakfast["plusSix"] = []
crow_mer_breakfast["plusSeven"] = []
crow_mer_lunch["current"] = []
crow_mer_lunch["plusOne"] = []
crow_mer_lunch["plusTwo"] = []
crow_mer_lunch["plusThree"] = []
crow_mer_lunch["plusFour"] = []
crow_mer_lunch["plusFive"] = []
crow_mer_lunch["plusSix"] = []
crow_mer_lunch["plusSeven"] = []
crow_mer_dinner["current"] = []
crow_mer_dinner["plusOne"] = []
crow_mer_dinner["plusTwo"] = []
crow_mer_dinner["plusThree"] = []
crow_mer_dinner["plusFour"] = []
crow_mer_dinner["plusFive"] = []
crow_mer_dinner["plusSix"] = []
crow_mer_dinner["plusSeven"] = []

port_kres_breakfast = {}
port_kres_lunch = {}
port_kres_dinner = {}
PORT_KRES = [port_kres_breakfast, port_kres_lunch, port_kres_dinner]
port_kres_breakfast["current"] = []
port_kres_breakfast["plusOne"] = []
port_kres_breakfast["plusTwo"] = []
port_kres_breakfast["plusThree"] = []
port_kres_breakfast["plusFour"] = []
port_kres_breakfast["plusFive"] = []
port_kres_breakfast["plusSix"] = []
port_kres_breakfast["plusSeven"] = []
port_kres_lunch["current"] = []
port_kres_lunch["plusOne"] = []
port_kres_lunch["plusTwo"] = []
port_kres_lunch["plusThree"] = []
port_kres_lunch["plusFour"] = []
port_kres_lunch["plusFive"] = []
port_kres_lunch["plusSix"] = []
port_kres_lunch["plusSeven"] = []
port_kres_dinner["current"] = []
port_kres_dinner["plusOne"] = []
port_kres_dinner["plusTwo"] = []
port_kres_dinner["plusThree"] = []
port_kres_dinner["plusFour"] = []
port_kres_dinner["plusFive"] = []
port_kres_dinner["plusSix"] = []
port_kres_dinner["plusSeven"] = []

car_oak_breakfast = {}
car_oak_lunch = {}
car_oak_dinner = {}
CAR_OAK = [car_oak_breakfast, car_oak_lunch, car_oak_dinner]
car_oak_breakfast["current"] = []
car_oak_breakfast["plusOne"] = []
car_oak_breakfast["plusTwo"] = []
car_oak_breakfast["plusThree"] = []
car_oak_breakfast["plusFour"] = []
car_oak_breakfast["plusFive"] = []
car_oak_breakfast["plusSix"] = []
car_oak_breakfast["plusSeven"] = []
car_oak_lunch["current"] = []
car_oak_lunch["plusOne"] = []
car_oak_lunch["plusTwo"] = []
car_oak_lunch["plusThree"] = []
car_oak_lunch["plusFour"] = []
car_oak_lunch["plusFive"] = []
car_oak_lunch["plusSix"] = []
car_oak_lunch["plusSeven"] = []
car_oak_dinner["current"] = []
car_oak_dinner["plusOne"] = []
car_oak_dinner["plusTwo"] = []
car_oak_dinner["plusThree"] = []
car_oak_dinner["plusFour"] = []
car_oak_dinner["plusFive"] = []
car_oak_dinner["plusSix"] = []
car_oak_dinner["plusSeven"] = []
    
# list of all the individual dining hall lists
# lot of lists huh? gonna try to find a solution to them in the future. Dictionary data structure doesn't seem too promising
diningHalls = [C9_C10, COW_STEV, CROW_MER, PORT_KRES, CAR_OAK]

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

def getMeals(url, breakfast, lunch, dinner):
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
        # print("X: " + str(x))

# def autoCheck():
#     favoriteResults = []

#     #Open all dining hall urls and put the meal names in the breakfast, lunch, and dinner lists
    
#     for num, diningHall in enumerate(diningHalls):
#         if num == 0:
#             getMeals(URLS[0], c9_c10_breakfast, c9_c10_lunch, c9_c10_dinner)

#         elif num == 1:

def getAllMeals():
    getMeals(URLS[0], c9_c10_breakfast, c9_c10_lunch, c9_c10_dinner)
    getMeals(URLS[1], cow_stev_breakfast, cow_stev_lunch, cow_stev_dinner)
    getMeals(URLS[2], crow_mer_breakfast, crow_mer_lunch, crow_mer_dinner)
    getMeals(URLS[3], port_kres_breakfast, port_kres_lunch, port_kres_dinner)
    getMeals(URLS[4], car_oak_breakfast, car_oak_lunch, car_oak_dinner)

def manualCheck():
    favoriteResults = []
    choiceMade = False
    while choiceMade == False:
        print("Which dining hall would you like check to see if your favorite meals are on the menu?")
        print("1. College 9/10")
        print("2. Cowell and Stevenson")
        print("3. Crown and Merrill")
        print("4. Porter and Kresge")
        print("5. Racheal Carson and Oakes")

        choice = int(input())
        
        if choice == 1:
            url = C9_C10_URL
            choiceMade = True
            print("You chose C9/C10 dining hall.")
            break
        elif choice == 2:
            url = COW_STEV_URL
            choiceMade = True
            print("You chose Cowell and Stevenson dining hall.")
            break
        elif choice == 3:
            url = CROW_MER_URL
            choiceMade = True
            print("You chose Crown and Merrill dining hall.")
            break
        elif choice == 4:
            url = PORT_KRES_URL
            choiceMade = True
            print("You chose Porter and Kresge dining hall.")
            break
        elif choice == 5:
            url = CAR_OAK_URL
            choiceMade = True
            print("You chose Rachael Carson and Oakes dining hall.")
            break
        else:
            print("Please input a valid choice.")

    try:
        resp = urllib.request.urlopen(url).read()

        soup = BeautifulSoup(resp, 'html.parser')

        table = soup.find('table')
        myTables = soup.findAll("table", {"cellspacing": 1}) #get the breakfast, lunch, and dinner tables, all with cellspacing: 0
        x = 0
        breakfast = []
        lunch = []
        dinner = []
        for table in myTables:
            myDivs = table.findAll("div", {"class": "menusamprecipes"})
            
            for div in myDivs:
                if x == 0:
                    breakfast.append(div.text)
                elif x == 1:
                    lunch.append(div.text)
                elif x == 2:
                    dinner.append(div.text)
            
            print(x)
            x += 1
        
        if not breakfast:
            print("There are no breakfast items today.")
        else:
            print("\nThese are the breakfast items:")
            for meal in breakfast:
                print(meal)
        
        if not lunch:
            print("There are no lunch items today.")
        else:
            print("\nThese are the lunch items:")
            for meal in lunch:
                print(meal)
        
        if not dinner:
            print("There are no dinner items today.")
        else:
            print("\nThese are the dinner items:")
            for meal in dinner:
                print(meal)

        print("Your breakfast favorites on the menu today:")
        for meal in favorites:
            if meal in breakfast:
                favoriteResults.append(meal)
                print(meal)


        print("\nYour lunch favorites on the menu today:")
        for meal in favorites:
            if meal in lunch:
                favoriteResults.append(meal)
                print(meal)

        print("\nYour dinner favorites on the menu today:")
        for meal in favorites:
            if meal in dinner:
                favoriteResults.append(meal)
                print(meal)

        return favoriteResults

    except Exception as e:
        print(str(e))


def sendText(toNumber, message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body = message,
        from_ ='+18316071845',
        to = toNumber
    )

# getAllMeals()
getMeals(PORT_KRES_URLS[0], port_kres_breakfast["current"], port_kres_lunch["current"], port_kres_dinner["current"])

print(port_kres_breakfast["current"])
print(port_kres_lunch["current"])
print(port_kres_dinner["current"])
# print(plusTwo)

# foodResults = manualCheck()

# foodResultString = ''
# for num, meal in enumerate(foodResults):
#     if num == (len(foodResults) - 1):
#         foodResultString += meal
#     else:
#         foodResultString += meal + ', '

# print(foodResultString)
#sendText(14086211865, "Your favorites on the menu today are: " + foodResultString)

# Special thanks to Mom for the "Hub" part of the Slug Grub Hub name
# Also special thanks to some of my friends for helping beta test Slug Grub Hub