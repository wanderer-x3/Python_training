def calculate_structure_sum(data_structure):
    variable = 0
    for mean in data_structure:
        #print(mean, type(mean))
        #print()
        if  isinstance(mean, list):
            variable += calculate_structure_sum(mean)
            # print(mean, 'list')
        elif isinstance(mean, dict):
            variable += calculate_structure_sum(mean.items())
            #print(mean, 'dict')
        elif isinstance(mean, tuple):
            variable += calculate_structure_sum(mean)
            #print(mean, 'tuple')
        elif isinstance(mean, set):
            variable += calculate_structure_sum(mean)
            #print(mean, 'set')
        elif isinstance(mean, str):
            variable += len(mean)
            #print(mean, 'str')
        elif isinstance(mean, int):
            variable += mean
            #print(mean, 'int')
        else:
            print(mean, '?')
    return variable


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
