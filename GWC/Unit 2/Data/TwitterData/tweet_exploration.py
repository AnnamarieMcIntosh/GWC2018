import json


file = open("tweets.json" , "r")
data = json.load(file)

for d in data: #data is a list,  d is a dicionary
    #loop through the dictionary (which correspondss to a single tweet)

#    for info_category, info in .items():
#        print (info_category, info)
#    print(user["favourites_count"])
    print(d["retweet_count"])

    #d is our dictionary about our tweet
    #for user_mention in d["user_mentions"]:
        #each user_mention is a dictionary
        #it corresponds
        #print(user_mention["screen_name"])
    break
