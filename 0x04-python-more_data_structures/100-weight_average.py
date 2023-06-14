#!/usr/bin/python3
def weight_average(my_list=[]):
    sum_nums = 0
    mul_nums = 0
    average = 0
    if len(my_list):
        for k, v in dict(my_list).items():
            sum_nums += v
            mul_nums += k * v
        average = mul_nums / sum_nums
    return (average)
