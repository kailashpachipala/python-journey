import random

CHOICES = ["rock", "paper", "scissors"]


def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(CHOICES)


def determine_winner(player, computer):
    """Determine the winner of a round."""
    if player == computer:
        return "draw"

    if (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        return "player"

    return "computer"


def display_result(player, computer, result):
    """Display the result of the current round."""
    print(f"\nYou chose     : {player.title()}")
    print(f"Computer chose: {computer.title()}")

    if result == "player":
        print("🎉 You win!")
    elif result == "computer":
        print("💻 Computer wins!")
    else:
        print("🤝 It's a draw!")


def play_game():
    """Run the Rock Paper Scissors game."""
    player_score = 0
    computer_score = 0
    draws = 0

    print("=" * 40)
    print("       ROCK PAPER SCISSORS")
    print("=" * 40)

    while True:
        print("\nChoose an option:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "4":
            break

        choice_map = {
            "1": "rock",
            "2": "paper",
            "3": "scissors"
        }

        if choice not in choice_map:
            print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")
            continue

        player_choice = choice_map[choice]
        computer_choice = get_computer_choice()

        result = determine_winner(player_choice, computer_choice)

        display_result(player_choice, computer_choice, result)

        if result == "player":
            player_score += 1
        elif result == "computer":
            computer_score += 1
        else:
            draws += 1

        print("\nScore:")
        print(f"You      : {player_score}")
        print(f"Computer : {computer_score}")
        print(f"Draws    : {draws}")

    print("\n" + "=" * 40)
    print("             FINAL SCORE")
    print("=" * 40)
    print(f"You      : {player_score}")
    print(f"Computer : {computer_score}")
    print(f"Draws    : {draws}")

    if player_score > computer_score:
        print("\n🏆 Congratulations! You won the game!")
    elif computer_score > player_score:
        print("\n💻 Computer won the game!")
    else:
        print("\n🤝 The game ended in a draw!")

    print("\nThanks for playing! 👋")


if __name__ == "__main__":
    play_game()