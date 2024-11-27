import time
import threading
import random

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for oper in range(10):
            if self.balance <= 500 and self.lock.locked():
                self.lock.release()
            else:
                number = random.randint(50, 500)
                self.balance += number
                print(f'Пополнение: {number}. Баланс: {self.balance}')
                time.sleep(0.001)

    def take(self):
        for oper in range(10):
            number = random.randint(50, 500)
            print(f'Запрос на {number}')
            if number <= self.balance:
                self.balance -= number
                print(f'Снятие: {number}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()


if __name__ == '__main__':
    bk = Bank()
    # Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
    th1 = threading.Thread(target=Bank.deposit, args=(bk,))
    th2 = threading.Thread(target=Bank.take, args=(bk,))

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    print(f'Итоговый баланс: {bk.balance}')



