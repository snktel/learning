#_____________________________________ Lists

"""
favoriteFruits = ["Apple", "Mango", "Strawberry"]
print(favoriteFruits)
print(favoriteFruits[0])
print(favoriteFruits[2])

favoriteFruits[1] = "Orange"
print(favoriteFruits[1])

favoriteFruits.append("Kiwi")

print(favoriteFruits)

favoriteFruits.insert(1, "Mango")
print(favoriteFruits[1])

favoriteFruits.remove("Strawberry")
print(favoriteFruits)

favoriteFruits.sort()
print(favoriteFruits)

favoriteFruits.reverse()
print(favoriteFruits)

favoriteFruits.pop()
favoriteFruits.pop()

print(favoriteFruits)
"""
#________________________________________Tuple
"""
historicWarDates=(1914,1939)
print(historicWarDates[1])

del(historicWarDates)
print(historicWarDates)
"""
#________________________________________Dictionary

""""
priceOfCameras={"sony":500,"nikon":600,"canon":700}
print(priceOfCameras["sony"])

priceOfCameras["nikon"]=800
print(priceOfCameras["nikon"])

print(priceOfCameras.keys())
print(priceOfCameras.values())

copypriceOfCameras=priceOfCameras.copy()
print(copypriceOfCameras)

del priceOfCameras["sony"]
print(priceOfCameras)

priceOfCameras.clear()
print(priceOfCameras)
"""

#_________________________________________Conditional Statements
"""
totalMarks=80
if totalMarks >= 90:
    print("Congratulation! You have secures an 'A' grade")
else:
    print("You have cleared the examination")

totalMarks=100
if totalMarks >= 90:
    print("Congratulation! You have secures an 'A' grade")
elif totalMarks>=40:
    print("You have cleared the examination")
elif totalMarks>=20:
    print("You have barely cleared the examination")
else:
    print("You have failed the examination")

totalMarks=95
if totalMarks>=90:
    print("Congratulation! You have secures an 'A' grade")
    if totalMarks==100:
        print("You have also secured full marks!")

totalMarks=88
percentageOfAttendabce=93
if totalMarks>=90 and percentageOfAttendabce>=90:
    print("You are very disciplined student")

fruit="Apple"
if fruit is "Mango" or fruit is "Apple":
    print("I love that fruit")
"""

# Check if number is a multiple of 3. If it is, also check if it is a multiple of 7
# 6 % 3 = 0; 10 % 3 = 2;
"""
print("Enter a number:")
number = int(input())
if number % 3 is 0:
    print("Number is a multiple of 3")
    if number % 7 is 0:
        print("Number is also a multiple of 7")
    else:
        print("Number is a multiple of 3, but not a multiple of 7")
"""

fruits=["Apple", "Mango", "Orange", "Strawberry"]
for fruit in fruits:
    print(fruit)

#print(fruits[0])

for number in range(1,10):
    print(number)













