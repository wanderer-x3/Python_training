my_dict = {'Sasha': 2000, 'Danya':1986, 'Kiril':2011} # Присваиваем Словарь
print('Dict:', my_dict)
print('Existing value:', my_dict ['Sasha'])
print('Not existing value:', my_dict.get('Misha'))

my_dict.update({
    'Misha': 1999,
    'Max': 2005
    })
Kiril = my_dict.pop('Kiril')
print('Deleted value:', Kiril)
print('Modufied dictionary:', my_dict)

my_set = {1, 58, 5.4, 'Ok', 1, 6, 58}
my_set = set(my_set)
print('Set:', my_set)

my_set.update({5.4, 'Hello', 3, 3})
my_set.remove('Ok')
print('Modified set:', my_set)
