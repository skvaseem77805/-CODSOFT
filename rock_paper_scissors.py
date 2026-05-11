# =========================================
#     ROCK PAPER SCISSORS GAME
# =========================================

import random

print("===================================")
print("    ROCK PAPER SCISSORS GAME")
print("===================================")

# Score counters
user_score = 0
computer_score = 0

# Game loop
while True:

    print("\nChoose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user_choice = input("Enter your choice: ").lower()

    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print("\nComputer chose:", computer_choice)

    # Game Logic
    if user_choice == computer_choice:
        print("Result: It's a Tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("Result: You Win!")
        user_score += 1

    elif user_choice in choices:
        print("Result: Computer Wins!")
        computer_score += 1

    else:
        print("Invalid Choice! Please choose rock, paper, or scissors.")
        continue

    # Display scores
    print("\nScore Board")
    print("You:", user_score)
    print("Computer:", computer_score)

    # Play again option
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\n===================================")
        print(" Final Scores")
        print(" You:", user_score)
        print(" Computer:", computer_score)
        print(" Thanks for playing!")
        print("===================================")
        break
