from art import logo, vs
from gameData import data
from random import choice
from replit import clear
score = 0
a = choice(data)
b = choice(data)
print(logo)
while True:
    while a==b:
        b = choice(data)
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    print(vs)
    print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}.")
    vote = input("Who has more followers? Type 'A' or 'B': ")
    if a['follower_count'] > b['follower_count']:
        winner = 'A'
    else:
        winner = 'B'
    clear()
    print(logo)
    if vote == winner:
        score += 1
        a=b
        b = choice(data)
        print(f"You're right! Current score: {score}.")
        continue
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        break
