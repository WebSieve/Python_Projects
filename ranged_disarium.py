# Prints list of disarium numbers between particular range.
from digit_separation import digit_separation as ds

lower_range = int(input("enter the lower range: "))
upper_range = int(input("enter the upper range: "))


def sum_of_digits(num1):
    temp = 0
    sep_digit = ds(num1)
    for i in sep_digit:
        temp = temp + i ** (sep_digit.index(i) + 1)
    return temp


for i in range(lower_range, upper_range):
    if i == sum_of_digits(i):
        print(i)

