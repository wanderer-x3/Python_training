immutable_var = tuple([1, 5, 5.07, 'go'])
print('Immutable tuple:', immutable_var)

# immutable_var[0][0]= 9 # !Элементы кортежа нельзя изменять или удалять, так как они прописываюсться в виде констант
# immutable_var[0]= 9 # ! (таким методом тоже, таким методом можно изменять только список) Элементы кортежа нельзя изменять или удалять, так как они прописываюсться в виде констант

mutable_list = [1, 5, 8.4, 'module']
mutable_list [1] = 'run'
print ('Mutable list:', mutable_list)

motorcade = ([1, 'apple'], [2, 'banan']) # Только в такой форме записе можно изменять элементы списка в кортеже
motorcade [1][1] = 'pear'
print('Motorcade [list]:',motorcade)
