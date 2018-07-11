def translate_shorthand (dictionary):
    for key, value in sorted(dictionary.items()):
        print(key, value)


#Key = shorthand; value = written out
shorthand ={
"omg" : "oh my gawd",
"l8r" : "later",
"ttyl" : "talk to you later",
"gn" : "good night",
"gg" : "good game",
"wtf" : "what the fork",
"ily" : "i love you"
}

translate_shorthand(shorthand)
