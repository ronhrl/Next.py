def is_valid(num):
    return num % 4 == 0


def four_dividers(number):
    return list(filter(is_valid, range(1, number)))


print(four_dividers(3))
