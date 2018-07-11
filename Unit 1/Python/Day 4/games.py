# TODO: import the random module since you  will need it in your game functions
import random
# TODO: define function guess_the_num
def guess_the_number():
    tries = 0
    #TODO: use random.randint to get a number between 1 and 20
    number = random.randint(1,20)
    #TODO: ask user to input their guess
    guess = int(input("What number is it?"))
    #TODO: loop to keep giving the player three guesses until they've guessed correctly
    while guess != number:
        for tries in range(2):
            tries += 1
        #TODO: give the player cues if the guess is not correct
        if number > guess:
            guess = int(input("Guess higher:"))
        elif number < guess:
            guess = int(input("Guess lower:"))
        elif number == guess:
            print("Congrats! You guessed the number!")
    #TODO: let the player know if the guess is correct
    if guess == number:
        print("Congrats! You guessed the number!")
    print("The number is {}".format(number))

# TODO: define function rock_paper_scissors

def rock_paper_scissors():
    # Create a list of possible moves in rock paper scissors
    gestures = ["rock", "paper", "scissors"]

    # Allow the computer to make a random selection on the move
    computer = random.choice(gestures)


    # TODO: Take in user input for rock, paper, or scissors
    # BE SURE TO PROCESS INPUT (valid inputs allowed ONLY)
    print("Hello! Welcome to Rock, Paper, Scissors!")
    player = input("rock, paper, or scissors?")
    # Show the human player what the computer decided on
    print("Computer chooses {}".format(computer.upper()))
    print("You chose {}".format(player.upper()))
        # Determine who wins
    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "Paper":
            print("You lose!")
        else:
            print("You win!")
    elif player == "paper":
        if computer == "Scissors":
            print("You lose!")
        else:
            print("You win!")
    elif player == "scissors":
        if computer == "Rock":
            print("You lose...")
        else:
            print("You win!")
    else:
            print("That's not a valid play. Check your spelling!")
        #player was set to True, but we want it to be False so the loop continues

# TODO: define function madlibs

# TODO: define function riddle

# TODO: define function even_or_odd
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
            
