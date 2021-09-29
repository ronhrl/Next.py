def get_fibo():
    x = 0
    yield x
    y = 1
    yield y
    fib_num = x + y
    while True:
        yield fib_num
        x = y
        y = fib_num
        fib_num = x + y


fibo_gen = get_fibo()
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
