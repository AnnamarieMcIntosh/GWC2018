########### Starter code for Rock Paper Scissors ############
def rock_paper_scissors():
    # Import the module (aka library) random
    import random
    # Create a list of possible moves in rock paper scissors
    gestures = ["rock", "paper", "scissors"]

    # Allow the computer to make a random selection on the move
    computer = random.choice(gestures)

    player = False

    # TODO: Take in user input for rock, paper, or scissors
    # BE SURE TO PROCESS INPUT (valid inputs allowed ONLY)
    #set player to True
    while player == False:
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
        again = input("Play again? (Y/N)")
        if again == "y":
            player = False
            computer = random.choice(gestures)
        else:
            print("Goodbye!")
            exit()

rock_paper_scissors()
