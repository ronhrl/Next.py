def double(char):
    return char * 2


def double_letter(my_str):
    return ''.join(list(map(double, my_str)))


print(double_letter("python"))
