#!/usr/bin/python3
matrix_mul = __import__('100-matrix_mul').matrix_mul

print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
print(matrix_mul([[1, 2], [3, 4], [3, 4]], [[5, 6, 1], [7, 8, 2]]))
print(matrix_mul([[5, 6], [7, 8]], [[5, 6], [7, "8"]]))
# print(matrix_mul())
# print(matrix_mul())
# print(matrix_mul())

