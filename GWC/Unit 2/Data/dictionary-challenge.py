friends_ages = {
    'Annamarie':16,
    'Kendra':16,
    'Sophia':17,
    'Grant':18,
}

#for k, v in friends_ages.items():
#    print("{0} is {1} years old.".format(k, v))

total_age = 0

for key, value in friends_ages.items():
    total_age += value
    
print("{0} is the average age.".format((total_age/len(friends_ages)))
