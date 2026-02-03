import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    best_score = None

    while True:
        print("\nChoose Difficulty Level:")
        print("1. Easy (1-20)")
        print("2. Medium (1-50)")
        print("3. Hard (1-100)")

        choice = input("Enter difficulty (1/2/3):")

        if choice == "1":
            max_num = 20
        elif choice == "2":
            max_num = 50
        elif choice == "3":
            max_num = 100
        else:
            print("Invalid choice! Defaulting to Medium (1-50).")
            max_num = 50

        secret_number = random.randint(1, max_num)
        attempts = 0

        print(f"\nI have chosen a number between 1 and {max_num}. Try to guess it!")

        while True:
            try:
                guess = int(input("Your guess: "))
                attempts += 1

                if guess < secret_number:
                    print(" Too low! Try a higher number.")
                elif guess > secret_number:
                    print(" Too high! Try a lower number.")
                else:
                    print(f" Correct! You guessed it in {attempts} attempts.")
                    break
            except ValueError:
                print("! Please enter a valid number!")

        # Tract best attempts
        if best_score is None or attempts < best_score:
            best_score = attempts
            print("New Best Score!")
        else:
            print(f"Best Score so far: {best_score} attempts")

        # Replay Option
        Play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if Play_again != "yes":
            print("\nThanks for playing! Goodbye")
            break

# Run th egame
number_guessing_game()


