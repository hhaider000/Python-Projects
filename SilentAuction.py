import os
cls = lambda: print('\n'*100)
# Interface
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the silent auction program.")

record_dict = {}
more_bidders = True
while more_bidders is True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    record_dict[name] = bid
    more = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if more == "no":
        highest_bid = 0
        for name in record_dict:
            bid_amount = record_dict[name]
            if bid_amount > highest_bid:
                highest_bid = bid_amount
                winner = name
        print(f"The winner is {winner} with a bid of ${highest_bid}.")
        # more_bidders = False
        break
    elif more == "yes":
        cls()
        continue
    print("Wrong input.")
# List of ideas for furthur improvements:
'''
Incorrect input needs to be rectified!
What if inputs are wrong?
What if multiple bidders have the same highest bid?
'''
