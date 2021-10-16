def coli():
    water = int(input('Write how many ml of water the coffee machine has: '))
    milk = int(input('Write how many ml of milk the coffee machine has: '))
    coffee_beans = int(input('Write how many grams of coffee beans the coffee machine has: '))
    cups = int(input('Write how many cups of coffee you will need: '))
    x = water // 200
    y = milk // 50
    z = coffee_beans // 15
    cups1 = [x, y, z]
    cups2 = min(cups1)
    if cups2 == cups:
        print("Yes, I can make that amount of coffee")
    elif cups2 > cups:
        qwe = cups2 - cups
        print("Yes, I can make that amount of coffee (and even " + str(qwe) + " more than that)")
    else:
        print("No, I can make only " + str(cups2) + " cups of coffee")


coli()
