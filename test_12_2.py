import unittest
import runner


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = runner.Runner("Useyn", 10)
        self.runner_2 = runner.Runner("Andy", 9)
        self.runner_3 = runner.Runner("Nikc", 3)

    @classmethod
    def tearDownClass(cls):
        for results in cls.all_results.values():
            f_res = {place:str(runner.name) for place, runner in results.items()}
            print(f_res)


    def test_tournament_useyn_nikc(self):
        tournament = runner.Tournament(90, self.runner_1, self.runner_3)
        self.all_results[1] = tournament.start()
        self.assertTrue("Nikc", self.all_results[1])

    def test_tournament_andy_nikc(self):
        tournament = runner.Tournament(90, self.runner_2, self.runner_3)
        self.all_results[2] = tournament.start()
        self.assertTrue("Nikc", self.all_results[2])

    def test_tournament_useyn_nikc_andy(self):
        tournament = runner.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_results[3] = tournament.start()
        self.assertTrue("Nikc", self.all_results[3])

if __name__ == "__main__":
    unittest.main()