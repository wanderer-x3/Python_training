class Horse:
    x_distance = 0
    sound = 'Frrr'

    def run(self, dx, dy):
        self.dx = dx
        self.x_distance += self.dx
        super().fly(dy)


class Eagle:
    y_distance = 0
    sound = 'I thain, eat, sleep, and repeat'
    
    def fly(self, dy):
        self.dy = dy
        self.y_distance += self.dy


class Pegasus(Horse, Eagle):
    def move(self, dx, dy):
        super().run(dx, dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(f'{Eagle.sound}')


if __name__ == '__main__':

    p1 = Pegasus()

    print(p1.get_pos())
    p1.move(10, 15)
    print(p1.get_pos())
    p1.move(-5, 20)
    print(p1.get_pos())

    p1.voice()
