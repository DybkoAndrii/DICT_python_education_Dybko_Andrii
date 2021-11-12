def input_m(qwe):
    dimension = input("Enter size of {}: ".format(qwe)).split()
    n, m = dimension
    mat = []
    print("Enter {}:".format(qwe))
    for y in range(int(n)):
        mat.append(input().split())
    return mat


def sum_mat():
    matrix = input_m("first matrix")
    matrix_2 = input_m("second matrix")
    if len(matrix) == len(matrix_2) and len(matrix[0]) == len(matrix_2[0]):
        print("The result is: ")
        for i in range(len(matrix)):
            for x in range(len(matrix[0])):
                print(float(matrix[i][x]) + float(matrix_2[i][x]), end=' ')
            print('')
    else:
        print("ERROR")


def multiply_const():
    matrix = input_m("matrix")
    const = input("Enter constant: ")
    print("The result is: ")
    for i in range(len(matrix)):
        for x in range(len(matrix[0])):
            print(float(matrix[i][x]) * float(const), end=' ')
        print('')


def multiply():
    matrix_1 = input_m("first matrix")
    matrix_2 = input_m("second matrix")
    if len(matrix_1) == len(matrix_2[0]):
        answer = 0
        print("The result is: ")
        for i in range(len(matrix_1)):
            for j in range(len(matrix_2[0])):
                for k in range(len(matrix_2)):
                    answer += float(matrix_1[i][k]) * float(matrix_2[k][j])
                print(answer, end=" ")
                answer = 0
            print("")
    else:
        print("ERROR")


while True:
    print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit""")
    action = input("Your choice: ")
    if action == "1":
        sum_mat()
    elif action == "2":
        multiply_const()
    elif action == "3":
        multiply()
    elif action == "0":
        break
    else:
        print("ERROR")
