testArray = []

bacon = ["bacon1", "bacon2"]

print(testArray)

newBacon = bacon.copy()

testArray.append(newBacon)

print(testArray)

bacon.clear()

print(bacon)

print(testArray)
print("yay")

mainArray = [list(firstArray), list(secondArray), list(thirdArray)]
