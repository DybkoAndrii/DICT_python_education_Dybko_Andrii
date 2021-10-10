water = 200
milk = 50
coffee_beans = 15
cups = input('Write how many cups of coffee you will need: ')
x = water * int(cups)
y = milk * int(cups)
z = coffee_beans * int(cups)
print("for" + cups + "cups of coffee you will need:")
print(str(x) + "ml of water")
print(str(y) + "ml of milk")
print(str(z) + "g of coffee beans")
