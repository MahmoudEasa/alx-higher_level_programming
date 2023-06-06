#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_num = (-int(str(number)[-1]) if number < 0 else int(str(number)[-1]))
print(f"Last digit of {number} is {last_num} and is", end=" ")
if last_num > 5:
    print("greater than 5")
elif last_num < 6 and last_num != 0:
    print("less than 6 and not 0")
elif last_num == 0:
    print("0")
