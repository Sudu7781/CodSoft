import random
import tkinter as tk
from tkinter import messagebox

choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0

def play_game(user_choice):
    global user_score, computer_score
    
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    score_label.config(text=f"Your Score: {user_score}  |  Computer Score: {computer_score}")

def determine_winner(user, computer):
    global user_score, computer_score

    if user == computer:
        return "It's a tie!"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Scissors" and computer == "Paper") or \
         (user == "Paper" and computer == "Rock"):
        user_score += 1
        return "You win!"
    else:
        computer_score += 1
        return "You lose!"

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text="Your Score: 0  |  Computer Score: 0")
    result_label.config(text="Make your choice!")

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")
root.config(bg="#F0F0F0")

title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 16, "bold"), bg="#F0F0F0")
title_label.pack(pady=10)

result_label = tk.Label(root, text="Make your choice!", font=("Arial", 12), bg="#F0F0F0")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Your Score: 0  |  Computer Score: 0", font=("Arial", 12, "bold"), bg="#F0F0F0")
score_label.pack(pady=10)

button_frame = tk.Frame(root, bg="#F0F0F0")
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="Rock", font=("Arial", 12), width=10, command=lambda: play_game("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(button_frame, text="Paper", font=("Arial", 12), width=10, command=lambda: play_game("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(button_frame, text="Scissors", font=("Arial", 12), width=10, command=lambda: play_game("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

reset_btn = tk.Button(root, text="Reset Game", font=("Arial", 12), width=15, command=reset_game)
reset_btn.pack(pady=10)

exit_btn = tk.Button(root, text="Exit", font=("Arial", 12), width=10, command=root.quit)
exit_btn.pack(pady=10)

root.mainloop()