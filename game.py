import tkinter as tk
import random
from PIL import Image, ImageTk

# Function to play the game
def play_game(user_choice):
    # Mapping user choice to image file
    user_image_file = {
        "rock": "rock.png",
        "paper": "paper.png",
        "scissors": "scissors.png"
    }[user_choice]

    # Load and display user's choice
    user_img = Image.open(user_image_file)
    user_img = user_img.resize((150, 150), Image.ANTIALIAS)
    user_photo = ImageTk.PhotoImage(user_img)
    user_label.config(image=user_photo)
    user_label.image = user_photo

    # Randomly choose computer's choice
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Load and display computer's choice
    computer_image_file = f"{computer_choice}.png"
    computer_img = Image.open(computer_image_file)
    computer_img = computer_img.resize((150, 150), Image.ANTIALIAS)
    computer_photo = ImageTk.PhotoImage(computer_img)
    computer_label.config(image=computer_photo)
    computer_label.image = computer_photo

    # Determine the winner and display the result
    if user_choice == computer_choice:
        result_label.config(text="It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        result_label.config(text="You win!")
    else:
        result_label.config(text="Computer wins!")

# Create a GUI window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

# Load and display default images
default_img = Image.open("default.png")
default_img = default_img.resize((150, 150), Image.ANTIALIAS)
default_photo = ImageTk.PhotoImage(default_img)

user_label = tk.Label(root, image=default_photo)
user_label.pack()

computer_label = tk.Label(root, image=default_photo)
computer_label.pack()

# Create buttons
rock_button = tk.Button(root, text="Rock", command=lambda: play_game("rock"))
rock_button.pack()

paper_button = tk.Button(root, text="Paper", command=lambda: play_game("paper"))
paper_button.pack()

scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game("scissors"))
scissors_button.pack()

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

# Start the GUI main loop
root.mainloop()
