import random
import art

print(art.logo)

print("Welcome to the Number Guessing Game!")

while True:
    print("I'm thinking of a number between 1 and 100.")

    numb = list(range(1, 101))

    picked_numb = random.choice(numb)

    difficulty = input("\nChoose a difficulty. Type 'easy' or 'hard': ").strip().lower()

    if difficulty == "easy":
        lives = 10
    elif difficulty == "hard":
        lives = 5
    else:
        print("\nInvalid choice! Defaulting to hard mode.")
        lives = 5

    print(f"\nYou have {lives} attempts remaining to guess the number.")

    while lives > 0:
        try:
            guess = int(input("\nMake a guess: "))
        except ValueError:
            print("\nInvalid input! Please enter a number between 1 and 100.")
            continue

        if guess < 1 or guess > 100:
            print("\nYou chose a wrong number! Pick a number between 1 and 100.")
            continue

        if guess == picked_numb:
            print(f"\nYou got it! The answer was {picked_numb}.")
            break
        else:
            lives -= 1
            if guess < picked_numb:
                print("\nToo low! Try again.")
            else:
                print("\nToo high! Try again.")

            if lives > 0:
                print(f"\nYou have {lives} attempts remaining.")
            else:
                print(f"\nGame Over! The number was {picked_numb}.")

    choice = input("\nDo you want to play again? (y = yes, n = no): ").strip().lower()
    if choice == "n":
        print("\nThanks for playing!")
        break
    elif choice == "y":
        print("\n" * 100)
        pass
    elif choice != "q" or "n":
        print("\nYou typed a wrong keyword, the game will now end.aa \nThanks for playing!")
        break
