def handle_input(num, rand):
    """
    Handle special inputs and validation.
    """
    if num == "x":
        print("Bye!")
        return "exit"
    if num == "n":
        print("Let's try again")
        return "new_game"
    if num == "s":
        print(f"The hidden number is: {rand}")
        return "show_number"
    if not num.isdigit():
        print("Please enter a valid number!")
        return "invalid"
    
    num = int(num)  
    if num < 1 or num > 20:
        print("Out of range! Please guess between 1 and 20.")
        return "out_of_range"
    
    return num  

def evaluate_guess(num, rand):
    """
    Evaluate whether the guess is too small, too big, or correct.
    """
    if num < rand:
        print("Try a bigger number.")
        return "too_small"
    elif num > rand:
        print("Try a smaller number.")
        return "too_big"
    else:
        print("Great Job! You won!")
        return "correct"