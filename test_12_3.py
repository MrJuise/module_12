import runner
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @classmethod
    def setUpClass(cls):
        if cls.is_frozen:
            raise unittest.SkipTest("тесты в этом кейсе заморожены")

    def test_walk(self):
        runn = runner.Runner('Test_Runner_walk')
        for _ in range(10):
            runn.walk()
        self.assertEqual(runn.distance, 50)
    def test_run(self):
        runn = runner.Runner('Test_Runner_run')
        for _ in range(10):
            runn.run()
        self.assertEqual(runn.distance, 100)
    def test_challenge(self):
        runner_walk = runner.Runner('Test_runner_walk')
        runner_run = runner.Runner('Test_runner_run')
        for _ in range(10):
            runner_walk.walk()
            runner_run.run()
        self.assertNotEqual(runner_walk.distance, runner_run.distance, msg="fail")

class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        if cls.is_frozen:
            raise unittest.SkipTest("тесты в этом кейсе заморожены")
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