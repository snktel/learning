string = ("Apple")
print(string)

print("{} is best fruit ever!".format(string))

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