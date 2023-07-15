def add_new_bidder(bidder_name, bid_price):
    bidder_price[bidder_name] = bid_price


def find_winner(bidder_record):
    winner = ""
    highest = 0
    for bidder in bidder_record:
        bid_number = bidder_record[bidder]
        if bid_number > highest:
            highest = bid_number
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest}.")


bidder_price = {}
should_end = False

while not should_end:
    name = input("What is your name?:").lower()
    bid = int(input("What's your bid?: $"))
    add_new_bidder(bidder_name=name, bid_price=bid)
    print(bidder_price)
    restart = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if restart == "no":
        should_end = True
        find_winner(bidder_price)




