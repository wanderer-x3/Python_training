import unittest
from unittest import TestCase

from runner_and_tournament import Runner, Tournament

def if_frozen(test_func):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen'):
            print('Тесты в этом кейсе заморожены')
            raise unittest.SkipTest('Тесты в этом кейсе заморожены')
        return test_func(self, *args, **kwargs)

    return wrapper


class RunnerTest(TestCase):
    is_frozen = False

    @if_frozen
    def test_walk(self):
        w = Runner("test_walk")
        for _ in range(10):
            w.walk()
        self.assertEqual(w.distance, 50)

    @if_frozen
    def test_run(self):
        r = Runner('test_run')
        for _ in range(10):
            r.run()
        self.assertEqual(r.distance, 100)

    @if_frozen
    def test_challenge(self):
        r = Runner('test_run')
        w = Runner("test_walk")
        for _ in range(10):
            r.run()
            w.walk()
        self.assertNotEqual(r.distance, w.distance)


class TournamentTest(TestCase):
    all_results = {}
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.participant_1 = Runner('Усэйн', 10)
        self.participant_2 = Runner('Андрей', 9)
        self.participant_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
       for result in cls.all_results.values():
            print({place: str(participant) for place, participant in result.items()})

    @if_frozen
    def test_tournament_1(self):
        tournament = Tournament(90, self.participant_1, self.participant_3)
        results = tournament.start()
        self.all_results[1] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    @if_frozen
    def test_tournament_2(self):
        tournament = Tournament(90, self.participant_2, self.participant_3)
        results = tournament.start()
        self.all_results[2] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    @if_frozen
    def test_tournament_3(self):
        tournament = Tournament(90, self.participant_1, self.participant_2, self.participant_3)
        results = tournament.start()
        self.all_results[3] = results
        self.assertTrue(results[max(results.keys())] == "Ник")


if __name__ == '__main__':
    unittest.main()
