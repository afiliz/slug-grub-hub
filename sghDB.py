import mysql.connector

# create connection to db and create cursor object
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="MySQL0l09802",
  database="sgh"
)

mycursor = mydb.cursor()

# gets the food string of given user
def getUserFoodString(number):
    sql = "SELECT foods FROM users WHERE number = %s"
    mycursor.execute(sql, (number,))
    myresult = mycursor.fetchone()

    for result in myresult:
        return result

# gets the dining hall string of given user
def getUserDiningHallsString(number):
    sql = "SELECT diningHalls FROM users WHERE number = %s"
    mycursor.execute(sql, (number,))
    myresult = mycursor.fetchone()

    for result in myresult:
        return result

# updates the user's food string to inputted string
def updateUserFoods(foodString, number):
    sql = "UPDATE users SET foods = %s WHERE number = %s"
    mycursor.execute(sql, (foodString, number,))
    mydb.commit()

# updates the user's dining hall string to inputted string
def updateUserDiningHalls(dhString, number):
    sql = "UPDATE users SET diningHalls = %s WHERE number = %s"
    mycursor.execute(sql, (dhString, number,))
    mydb.commit()

# prints out the user table
def printUsersTable():
    sql = "SELECT * FROM users"
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for results in myresult:
        print(results)

# converts an entry string (separated by ',') into an array
def getEntryArray(entryString):
    entryArr = entryString.split(',')
    del entryArr[-1]
    return entryArr

# adds a new entry to a string separated by ','
def addEntryToUserString(entryString, entryToAdd):
    # create array out of input string and delete last element
    # last element is created since there is a ',' at end of string
    entryArr = entryString.split(',')
    del entryArr[-1]

    # re-add ',' to all elements in array, then create the entry to add to array
    for i, entry in enumerate(entryArr):
        newentry = entryArr[i] + ','
        entryArr[i] = newentry
    addition = entryToAdd + ','

    # add the new entry entry to array and return array as string
    entryArr.append(addition)
    return ''.join(entryArr)

# adds a food entry to a given user's food string
def addFoodToUser(entryToAdd, number):
    foodString = getUserFoodString(number)

    newFoodString = addEntryToUserString(foodString, entryToAdd)

    updateUserFoods(newFoodString, number)

# adds a dh entry to a given user's dh string
def addDHToUser(entryToAdd, number):
    dhString = getUserDiningHallsString(number)

    newDHString = addEntryToUserString(dhString, entryToAdd)

    updateUserDiningHalls(newDHString, number)

# initializes a new user given their name and number
def createNewUser(name, number):
    sqlFormula = "INSERT INTO users (name, number, diningHalls, foods) VALUES (%s, %s, %s, %s)"
    newUser = (name, number, "", "")
    mycursor.execute(sqlFormula, newUser)
    mydb.commit()


# create table

# mycursor.execute("CREATE TABLE users (name VARCHAR(255), number VARCHAR(255), diningHalls JSON, foods JSON)")


# tried to use JSON arrays
# JSON_ARRAY_APPEND(json_doc, path, val[, path, val] ...)

# mycursor.execute("SELECT * FROM sgh")
# mycursor.execute("UPDATE sgh SET diningHalls = JSON_ARRAY_APPEND")

# mycursor.execute("INSERT INTO sgh(name, number, diningHalls, foods) VALUES ('user', '+17777777777', '[9, 10]', '[11, 12]')")
