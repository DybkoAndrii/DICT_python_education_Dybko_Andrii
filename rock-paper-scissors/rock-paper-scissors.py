import random

options = {"rock": "paper", "scissors": "rock", "paper": "scissors"}
while True:
    comp = random.choice(list(options.values()))
    option = input()
    if option in options:
        if option == options[comp]:
            print("Well done. The computer chose {} and failed".format(comp))
        elif comp == options[option]:
            print("Sorry, but the computer chose {}".format(comp))
        else:
            print("There is a draw {}".format(option))
    elif option == "!exit":
        print("Bye!")
        break
    else:
        print("Invalid input")
