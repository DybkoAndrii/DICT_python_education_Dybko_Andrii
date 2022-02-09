from random import randint


def st_1():
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
    print(f"{num_1} {action_st[action]} {num_2}")
    return answer


if __name__ == "__main__":
    grade = 0
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
