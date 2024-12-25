import random
import tkinter as tk
from tkinter import messagebox

def start_new_game():
    global hidden_number
    hidden_number = random.randint(1, 20)
    guess_entry.delete(0, tk.END)
    info_label.config(text="I am thinking of a number between 1 and 20.")

def check_guess():
    guess = guess_entry.get()
    if guess.lower() == 'x':
        root.destroy()
    elif guess.lower() == 's':
        messagebox.showinfo("Hidden Number", f"The hidden number is: {hidden_number}")
    elif not guess.isdigit():
        messagebox.showwarning("Invalid Input", "Please enter a valid number!")
    else:
        guess = int(guess)
        if guess < 1 or guess > 20:
            messagebox.showwarning("Out of Range", "Please guess a number between 1 and 20.")
        elif guess < hidden_number:
            info_label.config(text="Try a bigger number.")
        elif guess > hidden_number:
            info_label.config(text="Try a smaller number.")
        else:
            if messagebox.askyesno("Congratulations!", "Great Job, you won! Do you want to play again?"):
                start_new_game()
            else:
                root.destroy()

def reveal_hidden_number():
    messagebox.showinfo("Hidden Number", f"The hidden number is: {hidden_number}")

# Create the main window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x250")

# Initialize the hidden number
hidden_number = random.randint(1, 20)

# Create widgets
info_label = tk.Label(root, text="I am thinking of a number between 1 and 20.")
info_label.pack(pady=10)

guess_entry = tk.Entry(root, width=10)
guess_entry.pack(pady=5)

check_button = tk.Button(root, text="Check Guess", command=check_guess)
check_button.pack(pady=5)

reveal_button = tk.Button(root, text="Tell the Hidden Number", command=reveal_hidden_number)
reveal_button.pack(pady=5)

new_game_button = tk.Button(root, text="New Game", command=start_new_game)
new_game_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack(pady=5)

# Start the GUI event loop
root.mainloop()
