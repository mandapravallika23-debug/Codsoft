import random

# Initialize scores
user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

print("===================================")
print("      ROCK PAPER SCISSORS")
print("===================================")
print("Instructions:")
print("- Enter Rock, Paper, or Scissors")
print("- Type 'quit' anytime to exit")
print()

while True:
    # Get user choice
    user_choice = input("Choose Rock, Paper, or Scissors: ").lower()

    if user_choice == "quit":
        print("\nThanks for playing!")
        break

    if user_choice not in choices:
        print("❌ Invalid choice. Please try again.\n")
        continue

    # Computer choice
    computer_choice = random.choice(choices)

    print(f"\nYou chose: {user_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")

    # Determine winner
    if user_choice == computer_choice:
        print("🤝 It's a Tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("🎉 You Win!")
        user_score += 1
    else:
        print("💻 Computer Wins!")
        computer_score += 1

    # Display scores
    print("\nCurrent Scores:")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")

    # Play again
    play_again = input("\nPlay another round? (yes/no): ").lower()

    if play_again != "yes":
        print("\nFinal Scores:")
        print(f"You: {user_score}")
        print(f"Computer: {computer_score}")
        print("Thanks for playing!")
        break

    print("\n-----------------------------------\n")