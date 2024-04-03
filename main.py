# import os

auction_bidders = {}
keep_going = True

# print(logo)
print("Welcome to the secret auction!")

while keep_going:
    name = input("What is your name? ")
    bid = input("What is your bid? $")
    bid = int(bid)
    auction_bidders[name] = bid
    other_participants = input(
        "Are there any other participants willing to place their bids?\nType 'y' for yes or 'n' for no.\n")
    if other_participants.lower() != "y":
        keep_going = False
    # os.system('cls' if os.name == 'nt' else 'clear')

winner = name
for bidder in auction_bidders:
    if auction_bidders[bidder] > auction_bidders[winner]:
        winner = bidder
print(f"{winner} is the winner with ${auction_bidders[winner]} bid! Congratulations!")