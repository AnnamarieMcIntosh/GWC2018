# --- Define your functions below! ---
import random

def intro():
    print("Hello! Welcome to the chatbot.")
def greeting():
    print("Let's have a deep conversation about my favorite topic.")
def dating():
    print("I have been looking for a partner. I am 105 years old. I am a Fashion Nova Instagram Model in my free time. ")
    print("During the day, I am a ceral killer. At night, I am Batman.")
    rep = input("Soooo, come here often?")
    if rep == "yes":
        print("Sorry, you took long, I have a significant other.")
    elif rep == "no":
        print("That's good because I lost interest.")
    else:
        print ("Please respond with either yes or no.")
def art():
    rep = input("Do you want to see a piece of artwork?")
    if rep == "yes" or rep == "yah":
        random_art = random.choice(ascii_art)
        print(random_art)
def is_valid_input(response, all_valid_inputs):
    if response in all_valid_inputs:
        return True
    else:
        return False
ascii_art = ['''
                                   $""$o
                                  $"  $$
                                   $$$$
                                   o "$o
                                  o"  "$
             oo"$$$"  oo$"$ooo   o$    "$    ooo"$oo  $$$"o
o o o o    oo"  o"      "o    $$o$"     o o$""  o$      "$  "oo   o o o o
"$o   ""$$$"   $$         $      "   o   ""    o"         $   "o$$"    o$$
  ""o       o  $          $"       $$$$$       o          $  ooo     o""
     "o   $$$$o $o       o$        $$$$$"       $o        " $$$$   o"
      ""o $$$$o  oo o  o$"         $$$$$"        "o o o o"  "$$$  $
        "" "$"     """""            ""$"            """      """ "
         "oooooooooooooooooooooooooooooooooooooooooooooooooooooo$
          "$$$$"$$$$" $$$$$$$"$$$$$$ " "$$$$$"$$$$$$"  $$$""$$$$
           $$$oo$$$$   $$$$$$o$$$$$$o" $$$$$$$$$$$$$$ o$$$$o$$$"
           $"""""""""""""""""""""""""""""""""""""""""""""""""""$
           $"                                                 "$
           $"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$
''',
'''
   ________
   /_______/\
   \ \    / /
 ___\ \__/_/___
/____\ \______/\
\ \   \/ /   / /
 \ \  / /\  / /
  \ \/ /\ \/ /
   \_\/  \_\/
''',
'''
                    .---,
     .-.    __,,,__/    |
    /   \-'`        `-./_
    |    |               `)
     \   `             `\ ;
    /       ,        ,    |
    |      /         : O /_
    |          O  .--;__   '.
    |                (  )`.  |
    \                 `-` /  |
     \          ,_  _.-./`  /
      \          \``-.(    /
      |           `---'   /--.
    ,--\___..__        _.'   /--.
    \          `-._  _`/    '    '.
    .' ` ' .       ``    '        .
''',
'''
                             ,-''`-. \n
                            /       `._ \n'
                      __,-'/       _.  `--. \n
                    ,'   ,'      ,'  ,--.  ) \n
                  ,'   ,'       /  ,(  ,/)/ \n
                 /           ,',;-,-),;(' \n
                /      __.-',--'  ,,|/  `-.__ \n
               /  ,      ),',;;  (O)(        `--. \n
     ,.----.__/_,'      // /O)\  `.  \--'`-.     ) \n
   ,' __         _,.-'  ,/,-     c.' /  `.  `  ,/   .-. \n
  / ,'         ,'  _,-' (,,-\  -==*'/     )   (      ) \ \n
 ','      ,  ,'  ,'     ,'--`\-.___/.    ,   ( `-..-'   ) \n
 |      ,'   |          ``'\  \ ,    `.       `.      ,' \n
 | /   /      \        ,' \ )- )      |            --' ) \n
  ||  | .      .      (   //  /       |   ---._      ,' \n
   `. '. `-.          |  //  |        |   ,--' `-.-.' \n
     `--:._ `-.._     | //   |     Y  | ,' \n
                 `'-- )'/    |   ,'  /-' \n
                     / /     | ,'   / \n
                    ( (      ,'    ' \n
       -hrr-        ` `.__ ,'      ( \n
                     `.__,\      ,'"\ \n
                        ,- \ .  /\  ,\ \n
                       '    \  /  )/  `. \n
                       `.    )/  //     `. \n

''',
'''
    ,--._
    `.   `.                      ,-.
      `.`. `.                  ,'   )
        \`:  \               ,'    /
         \`:  ),.         ,-' ,   /
         ( :  |:::.    ,-' ,'   ,'
         `.;: |::::  ,' ,:'  ,-'
         ,^-. `,--.-/ ,'  _,'
        (__        ^ ( _,'
      __((o\   __   ,-'
    ,',-.     ((o)  /
  ,','   `.    `-- (
  |'      ,`        \
  |     ,:' `        |
 (  `--      :-.     |
 `,.__       ,-,'   ;
 (_/  `,__,-' /   ,'
 |\`--|_/,' ,' _,'
 \_^--^,',-' -'(
 (_`--','       `-.
  ;;;;'       ::::.`------.
    ,::       `::::  `:.   `.
   ,:::`       :::::   `::.  \
  ;:::::       `::::     `::  \
  |:::::        `::'      `:   ;
  |:::::.        ;'        ;   |
  |:::::;                   )  |
  |::::::        ,   `::'   |  \
  |::::::.       ;.   :'    ;   ::.
  |::::,::        :.  :   ,;:   |::
  ;:::;`"::     ,:::  |,-' `:   |::,
  /;::|    `--;""';'  |     :. (`";'
  \   ;           ;   |     ::  `,
   ;  |           |  ,:;     |  :
   |  ;           |  |:;     |  |
   |  |           |  |:      |  |
   |  |           |  ;:      |  |
  /___|          /____|     ,:__|
 /    /         /     |     /    )
 `---'          '----'      `---'
''',
'''
                      _____ \n
                   ,-'     `._ \n
                 ,'           `.        ,-. \n
               ,'               \       ),.\ \n
     ,.       /                  \     /(  \; \n
    /'\\     ,o.        ,ooooo.   \  ,'  `-') \n
    )) )`. d8P"Y8.    ,8P"""""Y8.  `'  .--"' \n
   (`-'   `Y'  `Y8    dP       `'     / \n
    `----.(   __ `    ,' ,---.       ( \n
           ),--.`.   (  ;,---.        ) \n
          / \O_,' )   \  \O_,'        | \n
         ;  `-- ,'       `---'        | \n
         |    -'         `.           | \n
        _;    ,            )          : \n
     _.'|     `.:._   ,.::" `..       | \n
  --'   |   .'     """         `      |`.\n
        |  :;      :   :     _.       |`.`.-'--.\n
        |  ' .     :   :__.,'|/       |  \ \n
        `     \--.__.-'|_|_|-/        /   ) \n
         \     \_   `--^"__,'        ,    | \n
         ;  `    `--^---'          ,'     | \n
          \  `                    /      / \n
           \   `    _ _          / \n
            \           `       / \n
             \           '    ,' \n
              `.       ,   _,' \n
                `-.___.---' \n

''']
greeting_promt = ["hi", "hello", "howdy"]
dating_prompt = ["Hello;)", "love me", "I've been looking for a partner", "I need a partner in crime"]
art_prompt = ["I like art", "show me art", "Show me art", "art", "Art"]
exit_prompt = ["bye", "goodbye", "exit", "Exit"]
# --- Put your main program below! ---
def main():
    valid_input = ["hi", "hello", "howdy", "Hi!", "Hello;)", "love me", "I've been looking for a partner", "I need a partner in crime", "I like art", "show me art", "Show me art", "art", "Art", "bye", "goodbye", "exit", "Exit"]
    intro()
    while True:
        answer = input("(What will you say?) ")
        if is_valid_input(answer, valid_input):
            if answer in greeting_promt:
                greeting()
            elif answer in dating_prompt:
                dating()
            elif answer in art_prompt:
                art()
            elif answer in exit_prompt:
                print("Goodbye! I will miss you.Come back again soon!")
                break
        else:
            print("These are the inputs I understand:")
            for vi in valid_input:
                print (vi)
            print("... I don't understand anything else.")



# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()
