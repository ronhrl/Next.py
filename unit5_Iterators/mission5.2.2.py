numbers = iter(list(range(1, 102)))
next(numbers)
next(numbers)
for i in numbers:
    print(i)
    next(numbers)
    next(numbers)
