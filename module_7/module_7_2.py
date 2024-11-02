from pprint import pprint

def custom_write(file_name, strings):
    name = file_name
    file = open(name, 'w', encoding='utf-8')
    i = 1
    byte = 0
    strings_positions = {}
    for string in strings:
        file.write(string)
        file.write('\n')
        strings_positions [(i, byte)] = string
        byte += file.tell()
        i += 1
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)