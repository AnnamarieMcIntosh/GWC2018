#TODO: import your games library into this file
import games

#TODO: create a list of available games
available_games = ["Even or Odd", "Rock, Paper, Scissors", "Guess The Number"]
#TODO: create a function to display the list of available games
    #HINT: use a loop
def display_games():
    print("Hello! My name is PEPE and I like to play games. I can play multiple games.")
    for g in available_games:
        print(g)


#TODO: write a function to evaluate the player's choice of game
def evaluate_choice():
    #TODO: ask the player which game they wish to play
    player_choice = input("What game do you want to play?")
    #TODO: run that particular game by calling the respective game with the dot notation
    if player_choice == "even or odd" or player_choice == "Even or Odd":
        games.even_or_odd()
    elif player_choice == "rock, paper, scissors" or player_choice == "Rock, Paper, Scissors":
        games.rock_paper_scissors()
    elif player_choice == "Guess the Number" or player_choice == "guess the number":
        games.guess_the_number()
    else:
        print("Sorry, that is not a valid game. Try again!")
#TODO: define a main function to run the games
def main():
    player =True
    while player == True:
        #TODO: call the function that displays a list of available available_games
        display_games()
        #TODO: call the function that evaluates the player's choice of game
        evaluate_choice()
        #TODO: ask the player if they wish to keep playing
        play_again = input("Do you wish to play again? (Y/N) ")
        #TODO: use a loop to keep playing if the player answers yes
        if play_again == "Y" or play_again == "y" :
            player = True

        else:
            print("I'm sad to see you go. Goodbye!")
            player = False

#TODO: call the main function appropriately
if __name__ == "__main__":
    main()
