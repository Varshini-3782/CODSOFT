import tkinter as tk
from tkinter import messagebox
import random

# Game window setup
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("500x400")
root.configure(bg="lightblue")

# Score variables
user_score = 0
computer_score = 0

# Game logic
def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = ""

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    # Update result display
    result_label.config(
        text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\nResult: {result}\n\nYour Score: {user_score} | Computer Score: {computer_score}"
    )

    # Ask to play again
    if messagebox.askyesno("Play Again", "Do you want to play another round?") == False:
        root.destroy()

# Heading
title = tk.Label(root, text="Rock, Paper, Scissors Game", font=("Helvetica", 16, "bold"), bg="lightblue")
title.pack(pady=10)

# Instructions
instructions = tk.Label(
    root,
    text="Select Rock, Paper, or Scissors to play.\nThe computer will also make a choice.\nRock beats Scissors, Scissors beats Paper, and Paper beats Rock.\nBest of luck!",
    font=("Helvetica", 10),
    bg="lightblue",
    justify="center"
)
instructions.pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", width=12, height=2, command=lambda: play("Rock"))
paper_button = tk.Button(button_frame, text="Paper", width=12, height=2, command=lambda: play("Paper"))
scissors_button = tk.Button(button_frame, text="Scissors", width=12, height=2, command=lambda: play("Scissors"))

rock_button.grid(row=0, column=0, padx=10)
paper_button.grid(row=0, column=1, padx=10)
scissors_button.grid(row=0, column=2, padx=10)

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="lightblue")
result_label.pack(pady=20)

# Start the GUI loop
root.mainloop()