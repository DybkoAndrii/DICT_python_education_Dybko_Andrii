def input_m():
    dimension = input().split()
    n, m = dimension
    mat = []
    for y in range(int(n)):
        mat.append(input().split())
    return mat


def sum_mat():
    matrix = input_m()
    matrix_2 = input_m()
    if len(matrix) == len(matrix_2) and len(matrix[0]) == len(matrix_2[0]):
        for i in range(len(matrix)):
            for x in range(len(matrix[0])):
                print(int(matrix[i][x]) + int(matrix_2[i][x]), end=' ')
            print('')
    else:
        print("ERROR")


sum_mat()
