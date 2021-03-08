"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

"""

import random



def start_game():
    print("-" * 30)
    print("Welcome to the Number Guessing Game!")
    print("-" * 30)


    tries = 0
    highscore = 0
    answer = random.randint(1, 10)

    while True:
        try:
            guess = int(input("Pick a number between 1 and 10:\n"))
        except:
            print("That was an invalid guess.")
            guess = int(input("Pick a number between 1 and 10:\n"))
        if guess >= 1 and guess <= 10:

            if guess < answer:
                print("It is higher!")
                tries += 1
            elif guess > answer:
                print("It is lower!")
                tries += 1
            else:
                tries += 1
                if tries > 1:
                    print(f"You got it! It took you {tries} tries!")
                else:
                    print(f"You got it! It took you {tries} try!")
                play_again = input("Would you like to play again? [y]es/[n]o: ").lower()

                if play_again == 'y':
                    if tries > highscore:
                        highscore = tries
                    print(f"The highscore is {highscore}")
                else:
                    break


                tries = 0
                answer = random.randint(1, 10)
        else:
            print("That was not a valid guess.")



start_game()