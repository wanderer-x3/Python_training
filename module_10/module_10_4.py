from threading import Thread
from time import sleep
from random import randint
from queue import Queue

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        # Ожидание от 3 до 10 секунд
        sleep(randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()        # Очередь для гостей
        self.tables = tables        # Список столов в кафе

    def guest_arrival(self, *guests):
        for guest in guests:
            # Проверяем наличие свободного стола
            free_table = next((table for table in self.tables if table.guest is None), None)
            if free_table:
                free_table.guest = guest        # Сажаем гостя за стол
                print(f'{guest.name} сел(-а) за стол номер {free_table.number}')
                guest.start()       # Запускаем поток
            else:
                # Если нет свободных столов, помещаем в очередь
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty():
            for table in self.tables:
                if not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None  # Освобождаем стол

                if table.guest is None and not self.queue.empty():
                    table.guest = self.queue.get()  # Берем следующего из очереди и сажаем
                    print(f"{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                    table.guest.start()  # Запускаем поток нового гостя


if __name__ == "__main__":
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
        ]
    # # Создание гостей
    guests = [Guest(name) for name in guests_names]
    # Заполнение кафе столами
    cafe = Cafe(*tables)
    # # Приём гостей
    cafe.guest_arrival(*guests)
    # # Обслуживание гостей
    cafe.discuss_guests()
