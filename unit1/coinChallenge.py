def combine_coins(coin, numbers):
    return [coin + str(num) for num in numbers]


print(combine_coins('$', range(5)))
