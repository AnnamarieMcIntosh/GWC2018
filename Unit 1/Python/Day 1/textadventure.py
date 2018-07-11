# Update this text to match your story.
start = '''
You, the main character of this story, have friends that have been kidnapped and
held hostage by a wizard in a forest. You must save your friends or else they
will perish. You come to a fork in the forest. Which way do you choose to go?
'''
while True:
    print(start)
    print("Type 'left' to go left or 'right' to go right.") # Update to match your story.
    user_input = input()
    if user_input == "left":
        print("You decide to go left and come across a lake. You can either swim across or walk around the long way.") # Update to match your story.
        print("Type 'swim' to swim across or 'walk' to walk around.")
        user_input = input()
        if user_input == "swim":
            print("You start swimming, but then you hear myserious noises. You look around to see what it is, but you get eaten before you know what it is.")
            print("GAME OVER. Try again.")
        if user_input == "walk":
            print("You walk around the edge of the lake. You see the wizard and confront him. He says 'If you can solve my riddle, you can save your friends'")
            print("What goes up when the rain comes down? ")
            answer = "umbrella"
            tries = 0
            guess = input("What is the answer?")
            for tries in range(2):
                tries += 1
                if guess != answer:
                    guess= input("Try again! Hint: What do you use when it rains?")
            print("The answer is an {}".format(answer))
            print("The wizard accepted your answer. He lets you and your friends go.")
            print("Congrats! You've reached the end.")

    elif user_input == "right":
        print("You choose to go right and get chased by a hungry bear. Finally, you lose him, but you realize you're on the left path.") # Update to match your story.
        print("You come across a lake. You can either swim across or walk around the long way.")
        print("Type 'swim' to swim across or 'walk' to walk around.")
        user_input = input()
        if user_input == "swim":
            print("You start swimming, but then you hear myserious noises. You look around to see what it is, but you get eaten before you know what it is.")
            print("GAME OVER. Try again.")
        if user_input == "walk":
            print("You walk around the edge of the lake. You see the wizard and confront him. He says 'If you can solve my riddle, you can save your friends'")
            print("What goes up when the rain comes down?")
            answer = "umbrella"
            tries = 0
            guess = input("What is the answer?")
            for tries in range(2):
                tries += 1
                if guess != answer:
                    guess= input("Try again! Hint: What do you use when it rains?")
            print("The answer is an {}".format(answer))
            print("The wizard accepted your answer. He lets you and your friends go.")
            print("Congrats! You've reached the end.")
    # Continue code to finish story.
