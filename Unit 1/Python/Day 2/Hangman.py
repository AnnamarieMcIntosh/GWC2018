def display(word, already_guessed_letters):
    new_str = ""
    for letter in word:
        if letter in already_guessed_letters:
            new_str += letter
        elif letter == " ":
            new_str += "  "
            # the letter in our phrase has not been guessed yet
        else:
            new_str += "_ "
    #print(new_str)
    return(new_str)

def main():
    # Have a word phrase
    phrase = "girls who code"
    # Keep track of users guesses
    guessed_letters = []
    game_over = False
    # Keep track of bad letters
    bad = []
    #Keep track of good letetrs
    good = []

    # Tell user how many spaces and letters
    begining = display(phrase, guessed_letters)
    print (begining)
    while game_over != True:
        # Allow user to give input to computer
        guess = input("Enter a letter:")

        # Tell the user if they get the right letter
        if guess in phrase:
            print("You got a letter: {}".format(guess))
        # Tell the user if they get the wrong letter
        else:
            print ("{} is not in the phrase".format(guess))
        # Add the guess letter to our list of guessed guessed_letters
        guessed_letters.append(guess)

        # Tell user how many spaces and letters
        hey = display(phrase, guessed_letters)
        print(hey)

        #End the game if the user gets all of the right letters in our phrase
        if "_" in hey:
            game_over = False
        else:
            game_over = True
    print("Congrats! END OF GAME")

    # End the game if the user gets all the right letters in the word phrase


if __name__ == "__main__":
    main()
