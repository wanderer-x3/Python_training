from pprint import pprint


def add_everything_up(a, b):
    try:
        res = a + b
    except TypeError:
        return str(a) + str(b)
    return res

def read_file(name):
    try:
        with open(name) as file:
            list_file = file.readlines()
            pprint(list_file)
    except FileNotFoundError:
        print(f'Файл не найден')


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
read_file('test1.txt')