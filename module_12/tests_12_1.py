from unittest import TestCase
import runner
from module_12.runner import Runner


class RunnerTest(TestCase):
    def test_walk(self):
        w = Runner("test_walk")
        for _ in range(10):
            w.walk()
        self.assertEquals(w.distance, 50)

    def test_run(self):
        r = Runner('test_run')
        for _ in range(10):
            r.run()
        self.assertEquals(r.distance, 100)

    def test_challenge(self):
        r = Runner('test_run')
        w = Runner("test_walk")
        for _ in range(10):
            r.run()
            w.walk()
        self.assertNotEquals(r.distance, w.distance)


if __name__ == '__main__':
    RunnerTest()