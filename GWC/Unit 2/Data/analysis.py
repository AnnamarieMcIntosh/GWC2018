import json


with open("data.json", "r") as f:
    # Load our json data into our json object
    data = json.load(f)

    # Loop through and print
    for d in data:
        print(d)
    print()

    # Find the most common social media
    media_count = {} # hold the counts for each social media
    for d in data:
        # Add 1 count for each social media seen
        media_count[d["socialMedia"]] =  media_count.get(d["socialMedia"], 0) + 1
    print("Most used Social Media by percentage of participants")
    for media, count in media_count.items():
        print("{}: {}%".format(media, 100 * count/ len(data)))
    print()

    # Find the most common favorite color
    color_count = {} # hold the counts for each color
    for d in data:
        # Add 1 count for each color seen
        color_count[d["color"]] =  color_count.get(d["color"], 0) + 1
    print("Favorite colors by percentage of participants")
    for color, count in color_count.items():
        print("{}: {}%".format(color, 100 * count/ len(data)))
    print()

    # Find the youngest and oldest age of participants
    print("Youngest and oldest participants")
    age_sort = sorted(data, key=lambda k: int(k['age'])) # sort from young to old
    print("Youngest: {}, age {}".format(age_sort[0]["Name"], age_sort[0]["age"]))
    print("Oldest: {}, age {}".format(age_sort[-1]["Name"], age_sort[-1]["age"]))
