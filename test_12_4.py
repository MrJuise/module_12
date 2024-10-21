import logging
import unittest


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_walk(self):
        try:
            runn = Runner('Test_Runner_walk', speed=-5)
            for _ in range(10):
                runn.walk()
            self.assertEqual(runn.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as er:
            logging.warning(f"Неверная скорость для Runner. | {er}")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_run(self):
        try:
            runn = Runner(132)
            for _ in range(10):
                runn.run()
            self.assertEqual(runn.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as er:
            logging.warning(f"Неверный тип данных для объекта Runner | {er}")


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_challenge(self):
        runner_walk = Runner('Test_runner_walk')
        runner_run = Runner('Test_runner_run')
        for _ in range(10):
            runner_walk.walk()
            runner_run.run()
        self.assertNotEqual(runner_walk.distance, runner_run.distance, msg="fail")

logging.basicConfig(level=logging.INFO, filemode="w", filename='runner_tests.log', encoding='UTF-8',
                    format="%(name)s - %(funcName)s - %(asctime)s - %(levelname)s - %(message)s")

first = Runner('Вося', 10)
second = Runner('Илья', 5)
third = Runner('Арсен', 10)

t = Tournament(101, first, second)
print(t.start())