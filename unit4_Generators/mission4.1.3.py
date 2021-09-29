def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def first_prime_over(n):
    new_generator = (i for i in range(n + 1, n ** 2) if is_prime(i))
    return next(new_generator)


print(first_prime_over(1000000))