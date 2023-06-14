#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_num = 0
    prev = 0
    if type(roman_string) == str:
        roman_items = {
                    "I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000,
                }
        for i in roman_string:
            if roman_items[i] > prev:
                roman_num -= prev
                roman_num += roman_items[i] - prev
            else:
                roman_num += roman_items[i]
            prev = roman_items[i]
    return (roman_num)
