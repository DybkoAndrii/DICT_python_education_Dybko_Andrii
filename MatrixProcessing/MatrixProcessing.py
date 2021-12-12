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
        ans_wer = 0
        print("The result is: ")
        for i in range(len(matrix_1)):
            for j in range(len(matrix_2[0])):
                for k in range(len(matrix_2)):
                    ans_wer += float(matrix_1[i][k]) * float(matrix_2[k][j])
                print(ans_wer, end=" ")
                ans_wer = 0
            print("")
    else:
        print("ERROR")


def transpose_1():
    matrix = input_m("matrix")
    print("The result is: ")
    for j in range(len(matrix)):
        for i in range(len(matrix[0])):
            print(matrix[i][j], end=' ')
        print('')


def transpose_2():
    matrix = input_m("matrix")
    mat = [[y for y in reversed(matrix[x])] for x in range(len(matrix))]
    qwe = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
    print("The result is: ")
    for x in range(len(matrix)):
        for y in reversed(qwe[x]):
            print(y, end=' ')
        print('')


def transpose_3():
    matrix = input_m("matrix")
    print("The result is: ")
    for x in range(len(matrix)):
        for y in reversed(matrix[x]):
            print(y, end=' ')
        print('')


def transpose_4():
    matrix = input_m("matrix")
    mat = [y for y in reversed(matrix)]
    print("The result is: ")
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end=' ')
        print('')


def get_minor(mat, i, j):
    return [x[:j] + x[j+1:] for x in (mat[:i]+mat[i+1:])]


def minor_determinant(minor):
    if len(minor) == 2:
        return float(minor[0][0])*float(minor[1][1])-float(minor[0][1])*float(minor[1][0])


def determinant_mat(mat):
    if len(mat) == 2:
        return float(mat[0][0]) * float(mat[1][1]) - float(mat[0][1]) * float(mat[1][0])
    else:
        determinant = 0
        for y in range(len(mat)):
            determinant += ((-1) ** y) * float(mat[0][y]) * minor_determinant(get_minor(mat, 0, y))
        return determinant


def inverse_mat():
    matrix = input_m("matrix")
    determinant = determinant_mat(matrix)
    if determinant != 0:
        if len(matrix) == 2:
            ntr_1 = [float(matrix[1][1]) / determinant, -1 * float(matrix[0][1]) / determinant]
            ntr_2 = [-1 * float(matrix[1][0]) / determinant, float(matrix[0][0]) / determinant]
            return ntr_1, ntr_2
        else:
            cofactors = []
            for r in range(len(matrix)):
                cofactor_row = []
                for c in range(len(matrix[r])):
                    minor = get_minor(matrix, r, c)
                    cofactor_row.append(((-1) ** (r + c)) * determinant_mat(minor))
                cofactors.append(cofactor_row)
            cofactors = [[cofactors[j][i] for j in range(len(cofactors))] for i in range(len(cofactors[0]))]
            for r in range(len(cofactors)):
                for c in range(len(cofactors)):
                    cofactors[r][c] = cofactors[r][c] / determinant
            return cofactors
    else:
        print("This matrix doesn't have an inverse.")


while True:
    print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit""")
    action = input("Your choice: ")
    if action == "1":
        sum_mat()
    elif action == "2":
        multiply_const()
    elif action == "3":
        multiply()
    elif action == "4":
        print("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
        action_2 = input("Your choice: ")
        if action_2 == "1":
            transpose_1()
        elif action_2 == "2":
            transpose_2()
        elif action_2 == "3":
            transpose_3()
        elif action_2 == "4":
            transpose_4()
        else:
            print("ERROR")
    elif action == "5":
        lst = input_m("matrix")
        print("The result is: ")
        print(determinant_mat(lst))
    elif action == "6":
        answer = inverse_mat()
        if answer is not None:
            print("The result is: ")
            for st in range(len(answer)):
                for st_2 in answer[st]:
                    print(round(st_2, 2), end=' ')
                print('')
    elif action == "0":
        break
    else:
        print("ERROR")
