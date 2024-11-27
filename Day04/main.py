import random
import sys
from helpers import handle_input, evaluate_guess

while True:  
    rand = random.randint(1, 20)
    print("I am thinking of a number between 1 and 20.")
    print("Type 'x' to exit, 'n' for a new game, or 's' to see the hidden number.")
    
    while True:  
        num = input("Guess a number (or use 'x', 'n', 's'): ")
        result = handle_input(num, rand)

        # Handle the result from handle_input
        if result == "exit":
            sys.exit()
        if result == "new_game":
            break  # Exit the inner loop to start a new game
        if result == "show_number" or result == "invalid" or result == "out_of_range":
            continue  # Prompt again for a valid input
        
        # Evaluate the guess if it's valid
        result = evaluate_guess(result, rand)
        if result == "correct":
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again != "y":
                print("Thanks for playing!")
                sys.exit()
            else:
                break  # Exit the inner loop to start a new game