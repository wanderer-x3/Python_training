import unittest
from unittest import TestCase
from runner_and_tournament import Runner, Tournament

class TournamentTest(TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.participant_1 = Runner('Усэйн', 10)
        self.participant_2 = Runner('Андрей', 9)
        self.participant_3 = Runner('Ник', 3)

    # @classmethod
    # def tearDownClass(cls):
    #     for res in cls.all_results.values():
    #         print(res)
    @classmethod
    def tearDownClass(cls):
       for result in cls.all_results.values():
            print({place: str(participant) for place, participant in result.items()})

    def test_tournament_1(self):
        tournament = Tournament(90, self.participant_1, self.participant_3)
        results = tournament.start()
        self.all_results[1] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_tournament_2(self):
        tournament = Tournament(90, self.participant_2, self.participant_3)
        results = tournament.start()
        self.all_results[2] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_tournament_3(self):
        tournament = Tournament(90, self.participant_1, self.participant_2, self.participant_3)
        results = tournament.start()
        self.all_results[3] = results
        self.assertTrue(results[max(results.keys())] == "Ник")


if __name__ == '__main__':
    unittest.main()
