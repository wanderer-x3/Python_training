"""
Задача "История строительства":
Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов".

В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.

Правильней вписывать здание в историю сразу при создании объекта, тем более можно удобно обращаться к атрибутам класса используя ссылку на сам класс - cls.
Дополните метод __new__ так, чтобы:

    Название объекта добавлялось в список cls.houses_history.
    Название строения можно взять из args по индексу.

Также переопределите метод __del__(self) в котором будет выводиться строка:
"<название> снесён, но он останется в истории"

Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__, а также значение атрибута houses_history.
"""

class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        __instance = object().__new__(cls)
        cls.houses_history.append(args[0])
        return __instance


    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor <= self.number_of_floors and new_floor > 1:
            for floor in range(1, new_floor + 1):
                print(floor)
                if new_floor == floor:
                    print(f'"Ваш этаж."')
        else:
            print('"Такого этажа не существует."')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        # return f'{self.name}'
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other

    def __lt__(self, other):
        return self.number_of_floors < other

    def __le__(self, other):
        return self.number_of_floors <= other

    def __gt__(self, other):
        return self.number_of_floors > other

    def __ge__(self, other):
        return self.number_of_floors >= other

    def __ne__(self, other):
        return self.number_of_floors != other

    def __add__(self, other):
        if isinstance(other, House):
            self.number_of_floors = self.number_of_floors + other.number_of_floors
            return self
        elif isinstance(other, int):
            self.number_of_floors = self.number_of_floors + other
            return self

    def __iadd__(self, other):
        if isinstance(other, House):
            self.number_of_floors += other.number_of_floors
            return self
        elif isinstance(other, int):
            self.number_of_floors += other
            return self

    def __radd__(self, other):
        return self + other

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')
        # __instance = None
        # House.houses_history = House.houses_history + (self.name)


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
