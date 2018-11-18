import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="MySQL0l09802",
  database="sgh"
)



mycursor = mydb.cursor()

def getUserFoodString(number):
    sql = "SELECT foods FROM users WHERE number = %s"
    mycursor.execute(sql, (number,))
    myresult = mycursor.fetchone()

    for result in myresult:
        return result

def getUserDiningHallsString(number):
    sql = "SELECT diningHalls FROM users WHERE number = %s"
    mycursor.execute(sql, (number,))
    myresult = mycursor.fetchone()

    for result in myresult:
        return result

def updateUserFoods(foodString, number):
    sql = "UPDATE users SET foods = %s WHERE number = %s"
    mycursor.execute(sql, (foodString, number,))
    mydb.commit()

def updateUserDiningHalls(dhString, number):
    sql = "UPDATE users SET diningHalls = %s WHERE number = %s"
    mycursor.execute(sql, (dhString, number,))
    mydb.commit()

def printUsersTable():
    sql = "SELECT * FROM users"
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for results in myresult:
        print(results)

def addFoodToUser(foodString, foodToAdd):
    # create array out of input string and delete last element
    # last element is created since there is a ',' at end of string
    foodArr = foodString.split(',')
    del foodArr[-1]

    # re-add ',' to all elements in array, then create the entry to add to array
    for i, food in enumerate(foodArr):
        newFood = foodArr[i] + ','
        foodArr[i] = newFood
    addition = foodToAdd + ','

    # add the new food entry to array and return array as string
    foodArr.append(addition)
    return ''.join(foodArr)


# updateUserFoods("Allergen Free Chicken Thigh,Cheese Pizza", "+16666666666")

# updateUserDiningHalls("c9c10", "+16666666666")

# printUsersTable()

# print(getUserFoodString("+16666666666"))

foodString = "test,test2,"

print(addFoodToUser(foodString, "test3"))
# mycursor.execute("SELECT * FROM users LIMIT 2")

# myresult = mycursor.fetchall()

# for result in myresult:
#     print(myresult)


# insert user

# sqlFormula = "INSERT INTO users (name, number, diningHalls, foods) VALUES (%s, %s, %s, %s)"
# users = [("Adam", "+16666666666", "910,CowellStevenson", "BBQ Pork Ribs,Chicken Tenders"),
#         ("Test User", "+17777777777", "PorterKresge,CarsonOakes", "BBQ Pork Ribs,Cheese Pizza")]

# mycursor.executemany(sqlFormula, users)




# query for elements with particular values

# sql = "SELECT * FROM users WHERE name = %s"

# mycursor.execute(sql, ("Adam", ))

# myresult = mycursor.fetchall()

# for row in myresult:
#     print(row)


# create table

# mycursor.execute("CREATE TABLE users (name VARCHAR(255), number VARCHAR(255), diningHalls JSON, foods JSON)")



# tried to use JSON arrays
# JSON_ARRAY_APPEND(json_doc, path, val[, path, val] ...)

# mycursor.execute("SELECT * FROM sgh")
# mycursor.execute("UPDATE sgh SET diningHalls = JSON_ARRAY_APPEND")

# mycursor.execute("INSERT INTO sgh(name, number, diningHalls, foods) VALUES ('user', '+17777777777', '[9, 10]', '[11, 12]')")
