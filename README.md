# Syntecxhub_Number_Guessing_Game

🎯 Number Guessing Game

A simple and fun Python project that demonstrates the use of loops, conditionals, and the random module.
The game randomly selects a number, and the player tries to guess it with helpful hints provided along the way.

🚀 Features

🎲 Random number generation

⬆️ Higher / ⬇️ Lower hints

🔢 Difficulty levels (Easy, Medium, Hard)

🧠 Tracks attempts for each round

🏆 Displays best (lowest) attempt score

🔁 Replay option

💡 Beginner-friendly logic using loops & conditionals

🛠️ How It Works

Player selects a difficulty level

Easy → 1–20

Medium → 1–50

Hard → 1–100

Program generates a random secret number.

Player guesses the number:

If guess is low → prints “Too low!”

If guess is high → prints “Too high!”

If correct → displays number of attempts

The game keeps track of the best score.

Player can choose to play again.

📂 Project Structure
Number_Guessing_Game/
│
├── Number_Guessing_game.py   # Main program
└── README.md                 # Project documentation

▶️ How to Run the Project
1. Install Python

Make sure Python is installed (Python 3.x recommended).

2. Run this command in terminal:
python Number_Guessing_game.py

📸 Screenshots (Optional)

Add your gameplay screenshots here

![Game Screenshot](screenshots/gameplay.png)

📚 Concepts Used

Random number generation (random.randint)

While loops

If-else conditions

Try-except error handling

User input handling

🔮 Future Improvements

You can extend the project by adding:

GUI version (Tkinter or PyQt)

Sound effects

Timer-based challenge

Score saving in a file

Colorful terminal output (using colorama)
