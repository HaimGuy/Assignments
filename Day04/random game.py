import random
import sys
while True: # to allow multiple games 
    rand = random.randint(1,20)
    print("I am thinking of a number between 1 and 20.")
    print("Type 'x' to exit, 'n' for a new game, or 's' to see the hidden number.")
    
    while True: 
        num = input("guess a number between 1-20")
        if num == "x":
            print ("Bye!")
            sys.exit()    
        if num == "n":
            print ("lets try again")
            break
        if num == "s":
            print (f"the hidden number is: {rand}")
            continue
        if not num.isdigit():
            print("Please enter a valid number!")
            continue
        num = int(num) # convert to digit

        if num > 20 or num < 0:
            print("out of range")
            continue
        if num < rand: 
            print("try a bigger number")
            continue
        if num > rand:
            print("try a smaller number")
            continue
        if num == rand:
            print ("Great Job, you won!")
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again != "y":
                print("Thanks for playing!")
                sys.exit()
            else:
                break