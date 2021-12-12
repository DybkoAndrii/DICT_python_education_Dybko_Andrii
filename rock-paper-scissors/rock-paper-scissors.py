import random


def take_options():
    while True:
        fun_pl_options = input().split(",")
        fun_loses_opt = []
        if len(fun_pl_options) == 1 and '' in fun_pl_options:
            return {"rock": ["paper"], "scissors": ["rock"], "paper": ["scissors"]}
        elif len(fun_pl_options) < 3:
            print("you can enter at least 3 items")
            continue
        elif len(fun_pl_options) % 2 == 0:
            print("Please enter an odd number of items")
            continue
        else:
            for i in range(len(fun_pl_options)):
                qwe = []
                for j in range(int(len(fun_pl_options) / 2)):
                    qwe.append(fun_pl_options[i - 1 - j])
                fun_loses_opt.append(qwe)
            return {fun_pl_options[i]: fun_loses_opt[i] for i in range(len(fun_pl_options))}


while True:
    try:
        with open("rating.txt", "r", encoding='utf-8') as f:
            text = f.read()
            file = text.split()
    except FileNotFoundError:
        with open("rating.txt", "w", encoding='utf-8') as f:
            f.write("Ivan 350\nAnna 200\nAlexey 400")
    else:
        break

if __name__ == "__main__":
    player = input("Enter your name: ")
    print("Hello, {}".format(player))
    options = take_options()
    print("Okay, let's start")
    if player in file:
        rating = int(file[file.index(player) + 1])
    else:
        rating = 0
    while True:
        comp = random.choice(list(options.keys()))
        option = input()
        if option in options:
            if option in options[comp]:
                print("Well done. The computer chose {} and failed".format(comp))
                rating += 100
            elif comp in options[option]:
                print("Sorry, but the computer chose {}".format(comp))
            else:
                print("There is a draw {}".format(option))
                rating += 50
        elif option == "!exit":
            if player in file:
                file[file.index(player) + 1] = str(rating)
            else:
                file.append(player)
                file.append(str(rating))
            with open("rating.txt", "w", encoding='utf-8') as h:
                for i1 in file:
                    if file.index(i1) % 2 == 0:
                        h.write(f"{i1} ")
                    else:
                        h.write(f"{i1}\n")
            print("Bye!")
            break
        elif option == "!rating":
            print("Your rating: {}".format(rating))
        elif option == "!help":
            for hlp in list(options.keys()):
                print(f"{options[hlp]} ----> {hlp}")
        else:
            print("Invalid input")
