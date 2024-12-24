from unittest import TestCase
import logging

from rt_with_exceptions import Runner


class RunnerTest(TestCase):

    def test_walk(self):
        try:
            w = Runner("test_walk", -5)
            for _ in range(10):
                w.walk()
            self.assertEqual(w.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner: {e}")

    def test_run(self):
        try:
            r = Runner(123, 5)
            for _ in range(10):
                r.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner: {e}")

    def test_challenge(self):
        r = Runner('test_run', 5)
        w = Runner("test_walk", 5)
        for _ in range(10):
            r.run()
            w.walk()
        self.assertNotEqual(r.distance, w.distance)

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        filename='runner_tests.log',
        filemode='w',
        encoding='utf-8',
        format='%(asctime)s - %(levelname)s - %(message)s'
    )