from random import randint


print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100")
difficulty = input("Choose a Difficulty. Type 'easy' or 'hard': ")

number = randint(1,100)

if difficulty == 'easy':
    attempt = 10
else:
    attempt = 5
while attempt:
    print(f"You have {attempt} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it! The answer is {number}")
        break
    elif guess > number:
        print("Too High")
    else:
        print("Too Low")
    print("Guess Again")
    attempt-=1

if attempt == 0:
    print(f"You lose, the number was {number}")