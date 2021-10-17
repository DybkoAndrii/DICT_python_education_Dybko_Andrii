water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9
money = 550


def espresso():
    global water, coffee_beans, money, disposable_cups
    if water > 249 and coffee_beans > 15 and disposable_cups > 0:
        print("I have enough resources, making you a coffee!")
        water -= 250
        coffee_beans -= 16
        disposable_cups -= 1
        money += 4
        return
    if water < 250:
        print("Sorry, not enough water!")
    if coffee_beans < 16:
        print("Sorry, not enough coffee beans!")
    if disposable_cups < 1:
        print("Sorry, not enough disposable cups!")


def latte():
    global water, milk, coffee_beans, money, disposable_cups
    if water > 349 and coffee_beans > 20 and disposable_cups > 0 and milk > 74:
        print("I have enough resources, making you a coffee!")
        water -= 350
        milk -= 75
        coffee_beans -= 20
        disposable_cups -= 1
        money += 7
        return
    if water < 350:
        print("Sorry, not enough water!")
    if coffee_beans < 20:
        print("Sorry, not enough coffee beans!")
    if disposable_cups < 1:
        print("Sorry, not enough disposable cups!")
    if milk < 75:
        print("Sorry, not enough milk!")


def cappuccino():
    global water, milk, coffee_beans, money, disposable_cups
    if water > 199 and coffee_beans > 11 and disposable_cups > 0 and milk > 99:
        print("I have enough resources, making you a coffee!")
        water -= 200
        milk -= 100
        coffee_beans -= 12
        money += 6
        return
    if water < 200:
        print("Sorry, not enough water!")
    if coffee_beans < 12:
        print("Sorry, not enough coffee beans!")
    if disposable_cups < 1:
        print("Sorry, not enough disposable cups!")
    if milk < 100:
        print("Sorry, not enough milk!")


def vod():
    global water, milk, coffee_beans, money, disposable_cups
    print("")
    print("The coffee machine has:\n" + str(water) + " of water\n" + str(milk) + " of milk")
    print(str(coffee_beans) + " of coffee beans\n" + str(disposable_cups) + " of disposable cups")
    print(str(money) + " of money")


def buy():
    while True:
        x = int(input("What do you want to buy?\n1 - espresso, 2 - latte, 3 - cappuccino, 4 - back to main menu: "))
        if x == 1:
            espresso()
        elif x == 2:
            latte()
        elif x == 3:
            cappuccino()
        elif x == 4:
            break
        else:
            print("enter the correct number")
        break


def fill():
    global water, milk, coffee_beans, money, disposable_cups
    water += int(input("Write how many ml of water you want to add: "))
    milk += int(input("Write how many ml of milk you want to add: "))
    coffee_beans += int(input("Write how many grams of coffee beans you want to add: "))
    disposable_cups += int(input("Write how many disposable coffee cups you want to add: "))
    vod()


def take():
    global money
    print("I gave you " + str(money))
    money -= money
    vod()


while True:
    print("")
    answer = input("Write action (buy, fill, take, remaining, exit): ")
    if answer == "buy":
        buy()
    elif answer == "fill":
        fill()
    elif answer == "take":
        take()
    elif answer == "remaining":
        vod()
    elif answer == "exit":
        break
    else:
        print("Enter the action correctly")
