from random import randint


def st_1():
    action_1 = randint(0, 2)
    num_1 = randint(2, 9)
    num_2 = randint(2, 9)
    action_st = ['+', '-', '*']
    if action_1 == 0:
        answer = num_1 + num_2
    elif action_1 == 1:
        answer = num_1 - num_2
    else:
        answer = num_1 * num_2
    print(f"{num_1} {action_st[action_1]} {num_2}")
    return answer


def st_2():
    num = randint(11, 29)
    print(num)
    return num ** 2


def st_3():
    action_1 = randint(0, 2)
    action_2 = randint(0, 2)
    num_1 = randint(2, 9)
    num_2 = randint(2, 9)
    num_3 = randint(2, 9)
    action_st = ['+', '-', '*']
    if action_1 == 0 and action_2 == 0:
        answer = num_1 + num_2 + num_3
    elif action_1 == 1 and action_2 == 0:
        answer = num_1 - num_2 + num_3
    elif action_1 == 2 and action_2 == 0:
        answer = num_1 * num_2 + num_3
    elif action_1 == 0 and action_2 == 1:
        answer = num_1 + num_2 - num_3
    elif action_1 == 1 and action_2 == 1:
        answer = num_1 - num_2 - num_3
    elif action_1 == 2 and action_2 == 1:
        answer = num_1 * num_2 - num_3
    elif action_1 == 0 and action_2 == 2:
        answer = num_1 + num_2 - num_3
    elif action_1 == 1 and action_2 == 2:
        answer = num_1 - num_2 - num_3
    else:
        answer = num_1 * num_2 * num_3
    print(f"{num_1} {action_st[action_1]} {num_2} {action_st[action_2]} {num_3}")
    return answer


def save(x, y, z):
    try:
        with open("results.txt", "a", encoding='utf-8') as f:
            f.write(f"{x}: {y}/5 in level {z}\n")
    except FileNotFoundError:
        with open("results.txt", "w", encoding='utf-8') as f:
            f.write(f"{x}: {y}/5 in level {z}\n")


if __name__ == "__main__":
    while True:
        action = input("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29
3 - operations on three numbers 2-9\n""")
        grade = 0
        if action == "1":
            lvl = "1 (simple operations with numbers 2-9)"
            for i in range(5):
                res = st_1()
                while True:
                    take = input()
                    try:
                        if int(take) == res:
                            print("Right!")
                            grade += 1
                        else:
                            print("Wrong!")
                    except ValueError:
                        print("Incorrect format")
                    else:
                        break
            print(f"Your mark is {grade}/5.")
            break
        elif action == "2":
            lvl = "2 (integral squares of 11-29)"
            for i in range(5):
                res = st_2()
                while True:
                    take = input()
                    try:
                        if int(take) == res:
                            print("Right!")
                            grade += 1
                        else:
                            print("Wrong!")
                    except ValueError:
                        print("Incorrect format")
                    else:
                        break
            print(f"Your mark is {grade}/5.")
            break
        elif action == "3":
            lvl = "3 (operations on three numbers 2-9)"
            for i in range(5):
                res = st_3()
                while True:
                    take = input()
                    try:
                        if int(take) == res:
                            print("Right!")
                            grade += 1
                        else:
                            print("Wrong!")
                    except ValueError:
                        print("Incorrect format")
                    else:
                        break
            print(f"Your mark is {grade}/5.")
            break
        else:
            print("Incorrect format")
    print("Would you like to save your result to the file? Enter yes or no.")
    while True:
        qwe = input()
        if qwe.lower() in ["yes", "y"]:
            name = input("What is your name?\n")
            save(name, grade, lvl)
            print('The results are saved in "results.txt"')
            break
        elif qwe.lower() in ["no", "n"]:
            break
        else:
            print("Incorrect format")
