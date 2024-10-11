def divide(first, second):
    if second != 0:
        result = first / second
        return result
    else:
        return 'Ошибка'


if __name__ == '__main__':
    print(divide(3, 0))
