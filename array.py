dealersNames = ["Ford", "Chrysler", "Dodge", "Ram", "Jeep", "Chevy", "GMC"]
print (dealersNames)

print (len(dealersNames))

dealersNames.append("Buick")
print (dealersNames)

print (dealersNames[3])

dealersNames.insert(2, "Toyota")
print (dealersNames)

dealersNames.pop(5)
print (dealersNames)

dealersNames.sort()
print (dealersNames)

dealersNames.sort(reverse = True)
print (dealersNames)

MyArrayLen = len(dealersNames)
print ("The length of my array is " + str(MyArrayLen))