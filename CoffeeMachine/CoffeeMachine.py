water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9
money = 550


def espresso():
    global water, coffee_beans, money, disposable_cups
    water -= 250
    coffee_beans -= 16
    disposable_cups -= 1
    money += 4
    return


def latte():
    global water, milk, coffee_beans, money, disposable_cups
    water -= 350
    milk -= 75
    coffee_beans -= 20
    disposable_cups -= 1
    money += 7
    return


def cappuccino():
    global water, milk, coffee_beans, money, disposable_cups
    water -= 200
    milk -= 100
    coffee_beans -= 12
    money += 6
    return


def vod():
    global water, milk, coffee_beans, money, disposable_cups
    print("The coffee machine has:\n" + str(water) + " of water\n" + str(milk) + " of milk")
    print(str(coffee_beans) + " of coffee beans\n" + str(disposable_cups) + " of disposable cups")
    print(str(money) + " of money")


def buy():
    x = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: "))
    if x == 1:
        espresso()
    elif x == 2:
        latte()
    elif x == 3:
        cappuccino()
    else:
        print("enter the correct number")
    vod()


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
    vod()
    print("")
    answer = input("Write action (buy, fill, take): ")
    if answer == "buy":
        buy()
        break
    elif answer == "fill":
        fill()
        break
    elif answer == "take":
        take()
        break
    else:
        print("Enter the action correctly")
