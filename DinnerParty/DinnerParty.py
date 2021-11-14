numb = int(input("Enter the number of friends joining (including you): "))
if numb > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    friends = [input() for i in range(numb)]
    value_dict = {i: 0 for i in friends}
    print(value_dict)
