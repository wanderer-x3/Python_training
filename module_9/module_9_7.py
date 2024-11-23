def is_prime(func):
    def wrapper(*args, **kwargs):
        number = func(*args, **kwargs)
        d = number - 1
        while d > 1:
            if number % d == 0:
                return f'Составное\n{number}'
            d -= 1
        return f'Простое\n{number}'

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)

