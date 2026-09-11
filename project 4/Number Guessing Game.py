
import random

print("🎯 WELCOME TO NUMBER GUESSING GAME 🎯")

score = 0

while True:

    # Difficulty selection
    print("\nChoose Difficulty:")
    print("1. Easy   → 1 to 50, 10 attempts")
    print("2. Medium → 1 to 100, 7 attempts")
    print("3. Hard   → 1 to 200, 5 attempts")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        max_number = 50
        max_attempts = 10
        level = "Easy"

    elif choice == "2":
        max_number = 100
        max_attempts = 7
        level = "Medium"

    elif choice == "3":
        max_number = 200
        max_attempts = 5
        level = "Hard"

    else:
        print("❌ Invalid choice!")
        continue

    # Generate secret number
    secret_number = random.randint(1, max_number)

    print(f"\n🎮 Difficulty: {level}")
    print(f"Guess a number between 1 and {max_number}")
    print(f"You have {max_attempts} attempts.")

    # Guessing loop
    for attempt in range(1, max_attempts + 1):

        guess = int(input(f"\nAttempt {attempt}: Enter your guess: "))

        # Correct guess
        if guess == secret_number:
            points = (max_attempts - attempt + 1) * 10
            score += points

            print("\n🎉 CONGRATULATIONS!")
            print(f"Correct number: {secret_number}")
            print(f"Attempts used: {attempt}")
            print(f"⭐ Points earned: {points}")
            print(f"🏆 Total Score: {score}")
            break

        # Guess is too low
        elif guess < secret_number:
            print("📉 Too low! Try a higher number.")

        # Guess is too high
        else:
            print("📈 Too high! Try a lower number.")

        # Hint after 3 attempts
        if attempt == 3:
            if secret_number % 2 == 0:
                print("💡 Hint: The number is EVEN.")
            else:
                print("💡 Hint: The number is ODD.")

        # Hint after 5 attempts
        if attempt == 5 and max_number >= 10:
            if secret_number > max_number // 2:
                print(f"💡 Hint: The number is greater than {max_number // 2}.")
            else:
                print(f"💡 Hint: The number is less than or equal to {max_number // 2}.")

    else:
        print("\n😢 GAME OVER!")
        print(f"The correct number was: {secret_number}")
        print(f"🏆 Your total score: {score}")

    # Play again
    play_again = input("\n🔄 Do you want to play again? (yes/no): ")

    if play_again.lower() != "yes":
        print("\n👋 Thanks for playing!")
        print(f"🏆 Final Score: {score}")
        break

