import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
try:
    url = 'https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=40&locationName=Colleges+Nine+%26+Ten+Dining+Hall&sName=&naFlag='
    
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
    print("These are the breakfast items:")
    print(breakfast)
    print("These are the lunch items:")
    print(lunch)
    print("These are the dinner items:")
    print(dinner)
    #print(table.prettify())
    #table_rows = soup.find_all('tr')

    #for tr in table_rows:
except Exception as e:
    print(str(e))