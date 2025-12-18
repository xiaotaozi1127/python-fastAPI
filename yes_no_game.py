def yes_no_game():
    """A simple yes/no guessing game."""
    print("Welcome to the Yes/No Guessing Game!")
    print("Player 1: Think of something (an object, a person, etc.) and keep it in your mind.")
    print("Player 2: Ask yes/no questions to guess what Player 1 is thinking.")

    secret = input("Player 1, what are you thinking of? (This will be hidden from Player 2): ")
    print("\n" * 50)  # Clear the screen to hide the secret
    print("Player 2, start asking yes/no questions!")

    while True:
        question = input("Player 2, ask your question: ")
        answer = input("Player 1, answer (yes/no): ").strip().lower()

        if answer not in ["yes", "no"]:
            print("Invalid answer. Please respond with 'yes' or 'no'.")
            continue

        guess = input("Player 2, do you want to guess the object? (yes/no): ").strip().lower()
        if guess == "yes":
            final_guess = input("What is your guess? ")
            if final_guess.lower() == secret.lower():
                print("Congratulations! You guessed it correctly!")
                break
            else:
                print("Wrong guess. Keep trying!")

if __name__ == "__main__":
    yes_no_game()