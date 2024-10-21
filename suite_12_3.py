import unittest
import test_12_3


tests = unittest.TestSuite()
tests.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.RunnerTest))
tests.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(tests)