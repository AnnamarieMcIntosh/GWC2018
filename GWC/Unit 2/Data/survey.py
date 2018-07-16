import json
import os


questions = {"Name": "What is your name? ",
"birthday": "When is your birthday? (MM/DD/YYYY) ",
"socialMedia": "What Social Media do you use most often? ",
"freeTime": "What do you do in your free time? ",
"color": "What is your favorite color? "
}


allResponses = []
user = True
while user == True:
    response = {}
    for category, question in questions.items():
        response[category] = input(question)
    allResponses.append(response)
    enter_again = input("Do you want to enter another response? (Y/N) ")
    if enter_again == "Y" or enter_again == "y" :
        user = True
    else:
        print("I'm sad to see you go. Goodbye!")
        user = False
        if os.path.isfile("data.json"):
            file = open("data.json", "r+")
            old_data = json.load(file)
            old_data.extend(allResponses)
            file.write(json.dumps(old_data))
            file.close()
        else:
            f = open("data.json","w") #create a file called data.json and give it the write permission
            file.write(json.dumps(allResponses)) #turn data into a json object
            file.close() #close our file




#===========================================================================================================================================
# WHAT TO DO WHEN YOU HAVE NEW DATA BUT YOU ALREADY HAVE A DATA.JSON file
# data2 = [{"name": "sandy", "age": 20, "fave food": ["pizza", "boba", "chocolate"]}]
# f = open("data.json", "r+")
# old_data = json.load(f)
# old_data.extend(data2)
# f.write(json.dumps(old_data))
# f.close()
