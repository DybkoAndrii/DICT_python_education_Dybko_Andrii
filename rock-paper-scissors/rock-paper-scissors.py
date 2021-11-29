options = {"scissors": "rock", "paper": "scissors", "rock": "paper"}
option = input()
if option in options:
    print("Sorry, but the computer chose {}".format(options[option]))
