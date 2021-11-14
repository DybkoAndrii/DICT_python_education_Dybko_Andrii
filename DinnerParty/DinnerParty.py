numb = int(input("Enter the number of friends joining (including you): "))
if numb > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    friends = [input() for i in range(numb)]
    amount = int(input("Enter the total amount: "))
    value_dict = {i: round(amount / numb, 2) for i in friends}
    print(value_dict)
else:
    print("No one is joining for the party")
