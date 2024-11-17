from random import choice
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda first, second: True if first == second else False, first, second)))


def get_advanced_writer(file_name):

    def write_everything(*data_set):
        nonlocal file_name
        try:
            with open(file_name, 'w') as file:
                for data in data_set:
                    data = str(data)
                    file.writelines(data + '\n')
        except FileNotFoundError:
            print('Ошибка файла')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())