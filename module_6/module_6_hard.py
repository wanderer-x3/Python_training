
class Figure:
    sides_count = 0

    def __init__(self, filled=True):
        self.filled = filled
        self._sides = []
        self._color = []

    def is_valid(self, *args):
        i = 0
        for number in args:
            if isinstance(number, int):
                if 0 <= number <= 255:
                    i += 1
        return i

    def set_color(self, *rgb):
        if self._is_valid_color(*rgb):
            for i in rgb:
                self._color.append(i)
                print(self._color)

    def _is_valid_color(self, *rgb):
        i = self.is_valid(*rgb)
        # i = 0
        # for number in rgb:
        #     if isinstance(number, int):
        #         if 0 <= number <=255:
        #             i += 1
        if i == 3:
            return True

    def get_color(self):
        return self._color

    def set_sides(self, *new_sides):
        if self._is_valid_sides(*new_sides):
            for i in new_sides:
                self._sides.append(i)

    def _is_valid_sides(self, *new_sides):
        i = self.is_valid(*new_sides)
        # i = 0
        # for side in new_sides:
        #     if isinstance(side, int):
        #         i += 1
        if len(self.sides_count) == i:
            return True
        return False

    def get_sides(self):
        return self._sides

    def __len__(self):
        return self.get_perimeter

class Circle(Figure):
    sides_count = [0]

    def __init__(self, color, sides):
        super().__init__()
        self.color = color
        self.sides = sides
        self.cast()


    def cast(self):
        self.set_color(self.color)
        # self.set_sides(self.sides)

    def radius(self):
        self.__radius = self.sides_count / (2 * 3.14)

    def get_perimeter(self):
        perimeter_ = 2 * 3.14 * self.__radius
        return perimeter_

    # def get_color(self):
    #     return super().get_color()




if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)
    print(circle1.get_color())
    # circle1.set_color(55, 66, 77)  # Изменится
    # print(circle1.get_color())

    # circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    # cube1 = Cube((222, 35, 130), 6)
    #
    # # Проверка на изменение цветов:
    # circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    # cube1.set_color(300, 70, 15)  # Не изменится
    # print(cube1.get_color())
    #
    # # Проверка на изменение сторон:
    # cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    # print(cube1.get_sides())
    # circle1.set_sides(15)  # Изменится
    # print(circle1.get_sides())
    #
    # # Проверка периметра (круга), это и есть длина:
    # print(len(circle1))
    #
    # # Проверка объёма (куба):
    # print(cube1.get_volume())



