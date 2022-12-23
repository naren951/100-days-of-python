from replit import clear
from art import logo

end = False

print(logo)
print("Welcome to Secret Auction Program")

bids = {}

while not end:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n$"))
    bids[name] = bid
    cont = input("Are there any other bidders? Type \"Yes\" or \"No\"\n").lower()
    if cont == "no":
        end = True
    else:
        clear()

highest_bid = 0
hightest_bidder = ""
for key in bids:
    if bids[key] > highest_bid:
        highest_bid = bids[key]
        hightest_bidder = key
    

print(f"The winner is {hightest_bidder} with a bid of {highest_bid}")
