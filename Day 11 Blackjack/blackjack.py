from replit import clear
from art import logo
from random import randint,choice

card = [11,2,3,4,5,6,7,8,9,10,10,10,10]


def calculate_score(l):
    if 11 in l and sum(l) > 21:
        l.remove(11)
        l.append(1)
        return sum(l)
    else:
        return sum(l)

while True:
    comp = []
    user = []
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if start == "y":
        clear()
        print(logo)
        user.append(choice(card))
        user.append(choice(card))
        comp.append(choice(card))
        comp.append(choice(card))
        print(f"Your cards: {user}, current score: {calculate_score(user)}")
        print(f"Computer's first card: {comp[0]}")
        while True:
            hit = input("Type 'y' to get another card, type 'n' to pass: ")
            if hit == "y":
                user.append(choice(card))
                print(f"Your cards: {user}, current score: {calculate_score(user)}")
                print(f"Computer's first card: {comp[0]}")
                if calculate_score(user) > 21 :
                    break
            else:
                break
        while calculate_score(comp)!=21 and calculate_score(comp) < 17:
            comp.append(choice(card))
        print(f"Your final hand: {user}, final score: {calculate_score(user)}")
        print(f"Computer's final hand: {comp}, final score: {calculate_score(comp)}")
        if calculate_score(user) > 21 :
            print("You lose 😤")
        elif calculate_score(comp) == 21:
            print("Lose, opponent has Blackjack 😱")
        elif calculate_score(comp) > 21:
            print("Opponent went over. You win 😁")
        elif calculate_score(comp) > 21:
            print("Opponent went over. You win 😁")
        elif calculate_score(user) == 21:
            print("Win with a Blackjack 😎")
        elif calculate_score(user) > calculate_score(comp):
            print("You win 😃")
        else:
            print("You lose 😤")
    else:
        break

