import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
from twilio.rest import Client

# TODO:
# - Add documentation
# - Add scheduling - day and College
# - add mysql database for phone users
# - add start and stop subscription for users
# - add favorite per user


account_sid = 'account_sid'
auth_token = 'auth_token'


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

# lists of meals for each dining hall
# each breakfast, lunch, and dinner list is in one main college dh list

c9_c10_breakfast = []
c9_c10_lunch = []
c9_c10_dinner = []
C9_C10 = [c9_c10_breakfast, c9_c10_lunch, c9_c10_dinner]

cow_stev_breakfast = []
cow_stev_lunch = []
cow_stev_dinner = []
COW_STEV = [cow_stev_breakfast, cow_stev_lunch, cow_stev_dinner]

crow_mer_breakfast = []
crow_mer_lunch = []
crow_mer_dinner = []
CROW_MER = [crow_mer_breakfast, crow_mer_lunch, crow_mer_dinner]

port_kres_breakfast = []
port_kres_lunch = []
port_kres_dinner = []
PORT_KRES = [port_kres_breakfast, port_kres_lunch, port_kres_dinner]

car_oak_breakfast = []
car_oak_lunch = []
car_oak_dinner = []
CAR_OAK = [car_oak_breakfast, car_oak_lunch, car_oak_dinner]

# list of all the individual dining hall lists
# lot of lists huh? gonna try to find a solution to them in the future. Dictionary data structure doesn't seem too promising
diningHalls = [C9_C10, COW_STEV, CROW_MER, PORT_KRES, CAR_OAK]

def getMeals(url, breakfast, lunch, dinner):
    url = URLS[0]
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
        print("X: " + str(x))

# def autoCheck():
#     favoriteResults = []

#     #Open all dining hall urls and put the meal names in the breakfast, lunch, and dinner lists
    
#     for num, diningHall in enumerate(diningHalls):
#         if num == 0:
#             getMeals(URLS[0], c9_c10_breakfast, c9_c10_lunch, c9_c10_dinner)

#         elif num == 1:

def autoCheck():
    favoriteResults = []

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
                #print(div.text)

        
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

        
        # print("These are the lunch items:")
        # print(lunch)
        # print("These are the dinner items:")
        # print(dinner)
        #print(table.prettify())
        #table_rows = soup.find_all('tr')

        #for tr in table_rows:
    except Exception as e:
        print(str(e))


def sendText(toNumber, message):


    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body = message,
        from_ ='+18316071845',
        to = toNumber
    )

foodResults = manualCheck()

foodResultString = ''
for num, meal in enumerate(foodResults):
    if num == (len(foodResults) - 1):
        foodResultString += meal
    else:
        foodResultString += meal + ', '
    

print(foodResultString)
#sendText(14086211865, "Your favorites on the menu today are: " + foodResultString)
