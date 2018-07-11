#TODO: define function guess_the_number
import random
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

guess_the_number()
