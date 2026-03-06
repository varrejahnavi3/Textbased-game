import random

def play_game():
    print("\n🎮 Welcome to the Guess the Number Game!")
    print("I am thinking of a number between 1 and 50.")
    print("You have 7 attempts to guess it.\n")

    secret_number = random.randint(1, 50)
    attempts = 7
    score = 0

    while attempts > 0:
        try:
            guess = int(input(f"Enter your guess (Attempts left: {attempts}): "))

            if guess < 1 or guess > 50:
                print("⚠ Please enter a number between 1 and 100.\n")
                continue

            if guess == secret_number:
                score = attempts * 10
                print(f"🎉 Congratulations! You guessed it right!")
                print(f"🏆 Your Score: {score}")
                break

            elif guess < secret_number:
                print("📉 Too low! Try a higher number.\n")

            else:
                print("📈 Too high! Try a lower number.\n")

            attempts -= 1

        except ValueError:
            print("❌ Invalid input! Please enter a valid number.\n")

    if attempts == 0:
        print(f"\n💀 Game Over! The correct number was {secret_number}.")

def main():
    while True:
        play_game()
        replay = input("\nDo you want to play again? (yes/no): ").lower()
        if replay != "yes":
            print("\n👋 Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()