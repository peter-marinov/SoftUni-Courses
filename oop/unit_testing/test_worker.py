class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'

# Create the following tests:
#     • Test if the worker is initialized with the correct name, salary, and energy
#     • Test if the worker's energy is incremented after the rest method is called
#     • Test if an error is raised if the worker tries to work with negative energy or equal to 0
#     • Test if the worker's money is increased by his salary correctly after the work method is called
#     • Test if the worker's energy is decreased after the work method is called
#     • Test if the get_info method returns the proper string with correct values

import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("TestGuy", 1000, 100)

    def test_correct_initializing(self):
        self.assertEqual("TestGuy", self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_increment_money_on_worker_when_working(self):
        self.worker.work()
        self.assertEqual(self.worker.salary, self.worker.money)

    def test_decrease_energy_on_worker_when_working(self):
        self.worker.work()
        self.assertEqual(99, self.worker.energy)

    def test_raise_exception_when_worker_is_working_with_zero_negative_energy(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_increment_energy_on_worker_when_rest(self):
        self.worker.rest()
        self.assertEqual(101, self.worker.energy)

    def test_correct_get_info(self):
        result = self.worker.get_info()
        self.assertEqual('TestGuy has saved 0 money.', result)


if __name__ == '__main__':
    unittest.main()