import random

def generate_code(colors, length=4):
    """Generate a random secret code."""
    return [random.choice(colors) for _ in range(length)]

def get_feedback(secret, guess):
    """Provide feedback in terms of black and white pegs."""
    black_pegs = sum(s == g for s, g in zip(secret, guess))
    white_pegs = sum(min(secret.count(color), guess.count(color)) for color in set(guess)) - black_pegs
    return black_pegs, white_pegs

def mastermind():
    """Main function to play the Mastermind game."""
    colors = ["red", "blue", "green", "yellow", "white", "black"]
    secret_code = generate_code(colors)
    attempts = 10

    print("Welcome to Mastermind!")
    print(f"Available colors: {', '.join(colors)}")
    print("Try to guess the secret code. You have 10 attempts.")

    for attempt in range(1, attempts + 1):
        guess = input(f"Attempt {attempt}/{attempts}: Enter your guess (e.g., red blue green yellow): ").split()

        if len(guess) != len(secret_code):
            print(f"Your guess must have {len(secret_code)} colors.")
            continue

        if any(color not in colors for color in guess):
            print("Invalid colors in your guess. Please use only the available colors.")
            continue

        black_pegs, white_pegs = get_feedback(secret_code, guess)
        print(f"Feedback: {black_pegs} black peg(s), {white_pegs} white peg(s)")

        if black_pegs == len(secret_code):
            print("Congratulations! You've cracked the code!")
            break
    else:
        print("Sorry, you've run out of attempts. The secret code was:", " ".join(secret_code))

if __name__ == "__main__":
    mastermind()