#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    matrix1 = len(matrix)

    if matrix1 > 0:
        for i in range(matrix1):
            matrix2 = len(matrix[i])
            if matrix2 > 0:
                for j in range(matrix2):
                    end_line = " " if j < (matrix2 - 1) else "\n"
                    print("{:d}".format(matrix[i][j]), end=end_line)
            else:
                print()
