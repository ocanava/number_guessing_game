"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

import random

number = random.randint(1, 10)

def start_game():
 
    print("Welcome to the Number Guessing Game!!")
    input("Press ENTER to continue...")    
    Tries = 1
    
    while True:
            try:        
                number = int(input("Pick a number between 1 and 10:  "))
                number = int(number)
                guess_value = 3 
                
            except ValueError:                
                print("Oops! Please enter a valid number.")                                                    
                Tries = Tries + 1
                                  
            else:              
                if guess_value > number:                
                    print("It's Higher! ")
                    Tries = Tries + 1  
                    continue
                          
                elif guess_value < number:               
                    print("It's Lower! ") 
                    Tries = Tries + 1  
                    continue
                
                elif guess_value == number:               
                    Tries = str(Tries)                
                    print("Well done! You guessed it in",  Tries + " tries. Game has ended! See you next time! ")
                    break  


start_game()
