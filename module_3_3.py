def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


values_list = [6, 'Текст', True]
values_dict = {'a': 555, 'b': 'Ура', 'c': False}
values_list_2 = [54.32, 'Строка' ]

print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)