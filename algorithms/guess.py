# Write a function that generates a random number between 1 and 100 and asks the user to guess it.
# Provide feedback to the user after each guess (e.g., "Too high!" or "Too low!").
# The game continues until the user guesses the correct number.
#
# RETURNS a boolean

import random
# TODO: Implement the game logic
def guess_the_number(user_guess):
    secret_number = random.randint(1, 100)
    print(secret_number)
    
    current_secret_number = secret_number
    current_guess = int(user_guess)
    
    while current_guess != current_secret_number: 
        current_guess = input('Guess another number: ')
        
        if int(current_guess) > current_secret_number:
            print('Too high, try again')   
            continue
        if int(current_guess) < current_secret_number:
            print('Too low!, try again')
            continue
        else: 
         print('You have guessed!')
        break
    
    

# Start the game
user_guess = input('Guess your number: ')
guess_the_number(user_guess)
