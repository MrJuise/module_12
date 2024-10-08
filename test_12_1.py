from runner import Runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner('Test_Runner_walk')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)
    def test_run(self):
        runner = Runner('Test_Runner_run')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)
    def test_challenge(self):
        runner_walk = Runner('Test_runner_walk')
        runner_run = Runner('Test_runner_run')
        for _ in range(10):
            runner_walk.walk()
            runner_run.run()
        self.assertNotEqual(runner_walk.distance, runner_run.distance, msg="fail")

