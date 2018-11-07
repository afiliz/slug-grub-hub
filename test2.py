from sghMeals import turnTupleIntoString
string1 = ""
string2 = ""
string3 = ""
string4 = ""

tup = ('BBQ Wings', 1, 'dinner')
turnTupleIntoString(tup, string1, string2, string3, string4)
print(string3)
# testString = "test\n"
# testString += "testerino"

# # def modifyString(testString):
# #   return testString + "testerino\n"

# print(testString)

# pickle test

# import pickle

# # wordList = ["cat", "hat", "jump", "house", "orange", "brick", "horse", "word"]

# # # do your thing here, like
# # wordList.append("monty")
# wordList = {}
# wordList2 = {}

# # wordList["test"] = "testerino"
# # wordList2["Test2"] = "TEEEEEST"

# wordLists = [wordList, wordList2]
# #open a pickle file
# newfile = 'mypickle2.pk'
# # newfile2 = 'mypickle3.pk'


# with open(newfile, 'wb') as fi:
#   # dump your data into the file
#   pickle.dump(wordLists, fi)

# # with open(newfile, 'wb') as di:
# #     pickle.dump(wordList2, di)

# # with open(newfile, 'rb') as fi:
# #   wordLists = pickle.load(fi)

# # with open(newfile, 'rb') as di:
# #   wordList2 = pickle.load(di)
# wordList = wordLists[0]
# wordList2 = wordLists[1]
# print (wordList["test"])
# print (wordList2["Test2"])

# end pickle test

# Deprecated code



    # getMeals(C9_C10_URLS[0], c9_c10_breakfast["current"], c9_c10_lunch["current"], c9_c10_dinner["current"], c9_c10_lateNight["current"])
    # getMeals(C9_C10_URLS[0], c9_c10_breakfast["plusOne"], c9_c10_lunch["plusOne"], c9_c10_dinner["plusOne"], c9_c10_lateNight["plusOne"])
    # getMeals(C9_C10_URLS[0], c9_c10_breakfast["plusTwo"], c9_c10_lunch["plusTwo"], c9_c10_dinner["plusTwo"], c9_c10_lateNight["plusTwo"])
    # getMeals(C9_C10_URLS[0], c9_c10_breakfast["current"], c9_c10_lunch["current"], c9_c10_dinner["current"], c9_c10_lateNight["current"])
    # getMeals(C9_C10_URLS[0], c9_c10_breakfast["current"], c9_c10_lunch["current"], c9_c10_dinner["current"], c9_c10_lateNight["current"])
    # getMeals(C9_C10_URLS[0], c9_c10_breakfast["current"], c9_c10_lunch["current"], c9_c10_dinner["current"], c9_c10_lateNight["current"])
    # getMeals(C9_C10_URLS[0], c9_c10_breakfast["current"], c9_c10_lunch["current"], c9_c10_dinner["current"], c9_c10_lateNight["current"])
    # getMeals(C9_C10_URLS[0], c9_c10_breakfast["current"], c9_c10_lunch["current"], c9_c10_dinner["current"], c9_c10_lateNight["current"])
    
# def updateAllMeals():
#     for i, hall in enumerate(diningHalls):
#         for j in range(1, 8):
#             if j == 1:





    # getMeals(C[0], c9_c10_breakfast, c9_c10_lunch, c9_c10_dinner, c9_c10_lateNight)

    # getMeals(URLS[0], c9_c10_breakfast, c9_c10_lunch, c9_c10_dinner, c9_c10_lateNight)
    # getMeals(URLS[1], cow_stev_breakfast, cow_stev_lunch, cow_stev_dinner, cow_stev_lateNight)
    # getMeals(URLS[2], crow_mer_breakfast, crow_mer_lunch, crow_mer_dinner, filler)
    # getMeals(URLS[3], port_kres_breakfast, port_kres_lunch, port_kres_dinner, filler)
    # getMeals(URLS[4], car_oak_breakfast, car_oak_lunch, car_oak_dinner, car_oak_lateNight)

# def autoCheck(): # old
#     favoriteResults = []

#     #Open all dining hall urls and put the meal names in the breakfast, lunch, and dinner lists
    
#     for num, diningHall in enumerate(diningHalls):
#         if num == 0:
#             getMeals(URLS[0], c9_c10_breakfast, c9_c10_lunch, c9_c10_dinner)

#         elif num == 1:


# Old function for manually checking dining hall foods via terminal
# def manualCheck():
#     favoriteResults = []
#     choiceMade = False
#     while choiceMade == False:
#         print("Which dining hall would you like check to see if your favorite meals are on the menu?")
#         print("1. College 9/10")
#         print("2. Cowell and Stevenson")
#         print("3. Crown and Merrill")
#         print("4. Porter and Kresge")
#         print("5. Racheal Carson and Oakes")

#         choice = int(input())
        
#         if choice == 1:
#             url = C9_C10_URL
#             choiceMade = True
#             print("You chose C9/C10 dining hall.")
#             break
#         elif choice == 2:
#             url = COW_STEV_URL
#             choiceMade = True
#             print("You chose Cowell and Stevenson dining hall.")
#             break
#         elif choice == 3:
#             url = CROW_MER_URL
#             choiceMade = True
#             print("You chose Crown and Merrill dining hall.")
#             break
#         elif choice == 4:
#             url = PORT_KRES_URL
#             choiceMade = True
#             print("You chose Porter and Kresge dining hall.")
#             break
#         elif choice == 5:
#             url = CAR_OAK_URL
#             choiceMade = True
#             print("You chose Rachael Carson and Oakes dining hall.")
#             break
#         else:
#             print("Please input a valid choice.")

#     try:
#         resp = urllib.request.urlopen(url).read()

#         soup = BeautifulSoup(resp, 'html.parser')

#         table = soup.find('table')
#         myTables = soup.findAll("table", {"cellspacing": 1}) #get the breakfast, lunch, and dinner tables, all with cellspacing: 0
#         x = 0
#         breakfast = []
#         lunch = []
#         dinner = []
#         for table in myTables:
#             myDivs = table.findAll("div", {"class": "menusamprecipes"})
            
#             for div in myDivs:
#                 if x == 0:
#                     breakfast.append(div.text)
#                 elif x == 1:
#                     lunch.append(div.text)
#                 elif x == 2:
#                     dinner.append(div.text)
            
#             print(x)
#             x += 1
        
#         if not breakfast:
#             print("There are no breakfast items today.")
#         else:
#             print("\nThese are the breakfast items:")
#             for meal in breakfast:
#                 print(meal)
        
#         if not lunch:
#             print("There are no lunch items today.")
#         else:
#             print("\nThese are the lunch items:")
#             for meal in lunch:
#                 print(meal)
        
#         if not dinner:
#             print("There are no dinner items today.")
#         else:
#             print("\nThese are the dinner items:")
#             for meal in dinner:
#                 print(meal)

#         print("Your breakfast favorites on the menu today:")
#         for meal in favorites:
#             if meal in breakfast:
#                 favoriteResults.append(meal)
#                 print(meal)


#         print("\nYour lunch favorites on the menu today:")
#         for meal in favorites:
#             if meal in lunch:
#                 favoriteResults.append(meal)
#                 print(meal)

#         print("\nYour dinner favorites on the menu today:")
#         for meal in favorites:
#             if meal in dinner:
#                 favoriteResults.append(meal)
#                 print(meal)

#         return favoriteResults

#     except Exception as e:
#         print(str(e))
