from art import logo
import os


def compare_bids(biddings):
    highest_bid = 0
    for bidder in biddings:
        bid_amount = biddings[bidder]
        # or max(biddings, key= biddings.get()) : gives maximum value in dictionary
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with the highest bid of {highest_bid}$")


bids = {}

continue_bidding = True

print(logo)
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("what is your bid? : $"))
    bids[name] = price
    should_continue = input("are there any new bidders? Type 'Yes or 'No. \n").lower()

    if should_continue == "no":
        continue_bidding = False
        compare_bids(bids)
    else:
        os.system('cls||clear')
