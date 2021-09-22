def is_prime(num):
    return [set(False if num % i == 0 else True for i in range(2, num))]


print(is_prime(42))
