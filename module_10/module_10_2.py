import threading
from time import sleep

class  Knight(threading.Thread):
    def __init__(self, name: str, power: int, enemies: int = 100):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies = enemies

    def battle(self, name, power, enemies):
        self.day = 0
        while enemies > 0:
            self.day += 1
            enemies -= power
            print(f'{name} сражается {self.day} день(дня)..., осталось {enemies} воинов.')
            sleep(1)
        return self.day

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.battle(self.name, self.power, self.enemies)
        print(f'{self.name} одержал победу спустя {self.day} дней(дня)!')


if __name__ == '__main__':
    # Создание класса
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)
    first_knight.start()
    second_knight.start()
    first_knight.join()
    second_knight.join()
    print('Все битвы закончились!')
    # Запуск потоков и остановка текущего
    # Вывод строки об окончании сражения