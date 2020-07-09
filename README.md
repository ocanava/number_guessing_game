# number_guessing_game

Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

import random

def start_game():
    print("Welcome to the Number Guessing Game!!")
    input("Press ENTER to continue...")
    number_of_guesses = 0
    number = random.randint(1, 10)   
                
    while True:  
        number = int(input("Pick a number between 1 and 10:  "))
        number_of_guesses +=1 
        if number < 3:
            print("It's Higher! ")
        if number > 3:
            print("It's Lower! ") 
        if number == 3:
            break
            
    if number == 3:
        number_of_guesses = str(number_of_guesses)
        print("Well done! You guessed it in " + number_of_guesses + " tries. Game has ended! See you next time! ")
        
          
start_game()
