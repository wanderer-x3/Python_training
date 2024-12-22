import unittest

from tests_12_3 import RunnerTest, TournamentTest

runnerST= unittest.TestSuite()
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

start_tests = unittest.TextTestRunner(verbosity=2)
start_tests.run(runnerST)
