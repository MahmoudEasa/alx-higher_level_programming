#!/usr/bin/python3
import sys

"""Module to solves the N queens problem
"""


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

num_s = sys.argv[1]

if not num_s.isdigit():
    print("N must be a number")
    exit(1)

n = int(num_s)

if n < 4:
    print("N must be at least 4")
    exit(1)

arr = [[0 for i in range(n)] for j in range(n)]


def is_col_safe(arr, col, n):
    for i in range(n):
        if arr[i][col] == 1:
            return (1)
    return (0)


def is_row_safe(arr, row, n):
    for i in range(n):
        if arr[row][i] == 1:
            return (1)
    return (0)


def is_dbr_safe(arr, row, col, n):
    while (row < n and col < n):
        if arr[row][col] == 1:
            return (1)
        row += 1
        col += 1
    return (0)


def is_dbl_safe(arr, row, col, n):
    while (row < n and col >= 0):
        if arr[row][col] == 1:
            return (1)
        row += 1
        col -= 1
    return (0)


def is_dtr_safe(arr, row, col, n):
    while (row >= 0 and col >= 0):
        if arr[row][col] == 1:
            return (1)
        row -= 1
        col -= 1
    return (0)


def is_dtl_safe(arr, row, col, n):
    while (row >= 0 and col < n):
        if arr[row][col] == 1:
            return (1)
        row -= 1
        col += 1
    return (0)


def solution(arr, n):
    c = 0
    r = 0
    n_len = 0
    track = 0
    index = []
    result = []

    while (c >= 0 and c < n):
        if is_col_safe(arr, c, n):
            if track:
                arr[c][index[-1]] = 0
                r = index[-1]
                index.pop()
                result.pop()
            else:
                c += 1
                continue
        while (r >= 0 and r < n):
            if is_row_safe(arr, r, n):
                r += 1
                continue
            if is_dbr_safe(arr, r, c, n):
                r += 1
                continue
            if is_dbl_safe(arr, r, c, n):
                r += 1
                continue
            if is_dtr_safe(arr, r, c, n):
                r += 1
                continue
            if is_dtl_safe(arr, r, c, n):
                r += 1
                continue

            arr[r][c] = 1
            result.append([c, r])
            index.append(r)
            r = 0
            break
        if r == n:
            c -= 1
            if len(index) > 0:
                arr[index[-1]][c] = 0
                r = index[-1] + 1
                index.pop()
                result.pop()
            continue
        c += 1
        if c == n and len(index) > 0:
            print(result)
            result = []
            r = index[0] + 1
            c = 0
            index = []
            track = 0
            arr = [[0 for i in range(n)] for j in range(n)]


solution(arr, n)
