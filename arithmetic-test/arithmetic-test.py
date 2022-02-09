from random import randint

if __name__ == "__main__":
    action = randint(0, 2)
    num_1 = randint(2, 9)
    num_2 = randint(2, 9)
    action_st = ['+', '-', '*']
    if action == 0:
        answer = num_1 + num_2
    elif action == 1:
        answer = num_1 - num_2
    else:
        answer = num_1 * num_2
    take = input(f"{num_1} {action_st[action]} {num_2}\n")
    try:
        print(answer)
        if int(take) == answer:
            print("Right!")
        else:
            print("Wrong!")
    except ValueError:
        print("Incorrect format")

