import random

with open("rating.txt", "r", encoding='utf-8') as f:
    text = f.read()
    file = text.split()
if __name__ == "__main__":
    options = {"rock": "paper", "scissors": "rock", "paper": "scissors"}
    player = input("Enter your name: ")
    if player in file:
        rating = int(file[file.index(player) + 1])
    else:
        rating = 0
    while True:
        comp = random.choice(list(options.values()))
        option = input()
        if option in options:
            if option == options[comp]:
                print("Well done. The computer chose {} and failed".format(comp))
                rating += 100
            elif comp == options[option]:
                print("Sorry, but the computer chose {}".format(comp))
            else:
                print("There is a draw {}".format(option))
                rating += 50
        elif option == "!exit":
            print("Bye!")
            break
        elif option == "!rating":
            print("Your rating: {}".format(rating))
        else:
            print("Invalid input")
