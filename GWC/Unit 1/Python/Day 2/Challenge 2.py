#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
Appetizer = ["Stuffed Artichoke", "Deviled Eggs", "Roasted Cashews", "Cheese and Crackers"]
MainCourse = ["Shrimp", "Pizza", "Salad", "Chili", "Chicken"]
Desert = ["Ice Cream", "Cake", "Pie", "Brownies", "Cookies"]

#Generates a random integer.
response = input("Would you like an appetizer? (Y/N)")
while response != "N":
    if response == "Y":
        aRandomIndex = randint(0, len(Appetizer)-1)
        print(Appetizer[aRandomIndex])
    else:
        print("{} is an invalid input.".format(response)
response = input("Would you like the Main Course? (Y/N)")
while response != "N":
    if response == "Y":
        aRandomIndex = randint(0, len(MainCourse)-1)
        print(MainCourse[aRandomIndex])
    else:
        print("{} is an invalid input.".format(response)
