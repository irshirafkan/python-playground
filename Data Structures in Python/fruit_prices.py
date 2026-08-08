# Fruit Dictionary Exercise
#
# Create a dictionary named fruit_prices that contains the prices of fruits.
# The prices are as follows:
#
# apple: 1500
# banana: 1000
# orange: 1200
#
# Then write code that changes the price of banana to 1100
# and completely removes apple.
# Finally, print the dictionary.

fruit = {
    "apple" : 1500,
    "banana" : 1000,
    "orange" : 1200,
}

fruit.update({"banana" : 1100 })
fruit.pop("apple")
print(fruit)