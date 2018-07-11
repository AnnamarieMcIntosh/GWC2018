number = 9
tries = 0

guess = int(input("What number is it?"))
while guess != number:
    for tries in range(2):
        tries += 1
        if number > guess:
            guess = int(input("Guess higher:"))
        else:
            guess = int(input("Guess lower:"))
    print("The number is {}".format(number))
    print =("Try again.")
