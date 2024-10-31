from math import pi

class Figure:
    sides_count = 0

    def __init__(self, color, sides):
        self.filled = True
        self.__sides = list(sides)
        self.__color = list(color)

    def set_color(self, r, g, b):               # Принимаем RGB
        if self._is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def _is_valid_color(self, r, g, b):         # Делаем проверку RGB
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                return True

    def get_color(self):
        return self.__color

    def set_sides(self, *new_sides):            # Принимаем длины сторон
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)

    def __is_valid_sides(self, new_sides):      # Делаем проверку
        if self.sides_count != len(new_sides):
            return False
        for side in new_sides:
            if not(isinstance(side, int) and side > 0):
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, sides)
        self.__radius = len(self) / (2 * pi)

    def get_square(self):                   # Считаем площадь круга
        return pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, sides * self.sides_count)

    def get_square(self):
        s = 1
        p = len(self) / 2
        for side in self.get_sides():
            s *= (p - side)
        return (p * s) ** (1 / 2)


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, sides * self.sides_count)

    def get_volume(self):
        for i in self.get_sides():
            return i * i * i


if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())
