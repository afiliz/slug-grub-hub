import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
try:
    url = 'https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=40&locationName=Colleges+Nine+%26+Ten+Dining+Hall&sName=&naFlag='
    
    resp = urllib.request.urlopen(url).read()

    soup = BeautifulSoup(resp, 'html.parser')

    table = soup.find('table')
    mydivs = soup.findAll("div", {"class": "menusamprecipes"})
    for div in mydivs:
        print(div.text)
    #print(table.prettify())

    #table_rows = soup.find_all('tr')

    #for tr in table_rows:
    


except Exception as e:
    print(str(e))