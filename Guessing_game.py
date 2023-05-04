import random
guess_number = random.randint(1, 100)
tries = 11
print(guess_number)
print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.""")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    for izi in range(11):
        tries -= 1
        print(f"You have {tries} attempts remaining to guess the number.")
        guess = int(input("Guess number: "))
        if guess < guess_number:
            print("computer's number is higher")
        elif guess > guess_number:
            print("computer's number is lower")
        else:
            print("You Won")
            break
        if tries == 1:
            print("You've run out of guesses, you lose.")
            break
        elif tries > 1:
            print("guess again")
else:
    for izi in range(6):
        tries -= 1
        print(tries)
        print(f"You have {tries - 5} attempts remaining to guess the number.")
        if tries == 5:
            print("You've run out of guesses, you lose.")
            break
        guess = int(input("Guess number: "))
        if guess < guess_number:
            print("computer's number is higher")
        elif guess > guess_number:
            print("computer's number is lower")
        else:
            print("You Won")
            break
        if tries > 6:
            print("guess again")
