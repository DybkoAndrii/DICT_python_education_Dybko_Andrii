import random

numb = int(input("Enter the number of friends joining (including you): "))
if numb > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    friends = [input() for i in range(numb)]
    amount = int(input("Enter the total amount: "))
    value_dict = {i: round(amount / numb, 2) for i in friends}
    action = input('Do you want to use the "Who is lucky?" feature? Write Yes/No: ')
    if action == "Yes" or action == "yes":
        lucky = random.choice(range(len(friends)))
        print("{} is the lucky one!".format(friends[lucky]))
        value_dict_1 = {i: round(amount / (numb - 1), 2) for i in friends}
        value_dict_l = list(value_dict_1.keys())
        value_dict_1[value_dict_l[lucky]] = 0
        print(value_dict_1)
    else:
        print("No one is going to be lucky")
        print(value_dict)
else:
    print("No one is joining for the party")
