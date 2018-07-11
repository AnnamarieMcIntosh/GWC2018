import random
def even_or_odd():
    player = False
    while player == False:
        computer_value = random.randint(1,10)
        print("{}".format(computer_value))
        user_input = input("Is this number even or odd?")

        if computer_value%2 == 0 and user_input == "even":
            print("YOU DID IT! YOU USED YOUR SMARTS.")
        elif computer_value%2 == 0 and user_input == "odd":
            print("You are wrong.")
        elif computer_value%2 != 0 and user_input == "even":
            print("You are wrong.")
        elif computer_value%2 == 0 and user_input == "even":
            print("YOU DID IT! YOU USED YOUR SMARTS.")
        again = input("Play again? (Y/N)")
        if again == "y":
            player = False
            computer_value = random.randint(1,10)
        else:
            print("Goodbye!")
            exit()


even_or_odd()
