import tkinter as tk
from tkinter import messagebox
import random


# Function to check if the guess is correct
def check_guess():
    user_guess = int(entry.get())
    if user_guess == secret_number:
        messagebox.showinfo("Congratulations!", "You guessed the number!")
        window.destroy()
    elif user_guess < secret_number:
        messagebox.showinfo("Wrong Guess", "Too low! Try again.")
    else:
        messagebox.showinfo("Wrong Guess", "Too high! Try again.")


# Generate a random number
secret_number = random.randint(1, 100)

# Create main window
window = tk.Tk()
window.title("Guess the Number Game")

# Add label and entry for user input
label = tk.Label(window, text="Guess the Number (1-100):")
label.pack(pady=10)
entry = tk.Entry(window)
entry.pack(pady=10)

# Add guess button
guess_button = tk.Button(window, text="Guess", command=check_guess)
guess_button.pack(pady=10)

# Run the game
window.mainloop()
