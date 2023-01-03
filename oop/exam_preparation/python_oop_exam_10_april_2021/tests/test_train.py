from unittest import TestCase, main

#from project.project.train.train import Train
from project.train.train import Train


class TestTrain(TestCase):
    def setUp(self):
        self.train = Train('train1', 3)

    def test_correct_initializing(self):
        self.assertEqual('train1', self.train.name)
        self.assertEqual(3, self.train.capacity)
        self.assertEqual([], self.train.passengers)
        self.assertEqual("Train is full", self.train.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", self.train.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", self.train.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", self.train.PASSENGER_ADD)
        self.assertEqual("Removed {}", self.train.PASSENGER_REMOVED)
        self.assertEqual(0, self.train.ZERO_CAPACITY)

    def test_add_passenger_when_no_capacity_raise_value(self):
        self.train.passengers = ['Ivan', 'Gosho', 'Stamat']
        with self.assertRaises(ValueError) as ve:
            self.train.add('Peter')

        self.assertEqual("Train is full", str(ve.exception))

    def test_add_passenger_when_passenger_exists_raise_valuer_error(self):
        self.train.passengers = ['Ivan', 'Gosho']
        with self.assertRaises(ValueError) as ve:
            self.train.add('Gosho')

        self.assertEqual("Passenger Gosho Exists", str(ve.exception))
        self.assertEqual(['Ivan', 'Gosho'], self.train.passengers)

    def test_add_passenger_correct(self):
        self.train.passengers = ['Ivan', 'Gosho']
        expected_result = self.train.add('Peter')
        self.assertEqual("Added passenger Peter", expected_result)
        self.assertEqual(['Ivan', 'Gosho', 'Peter'], self.train.passengers)

    def test_remove_passenger_when_not_exists_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.train.remove('Peter')
        self.assertEqual("Passenger Not Found", str(ve.exception))

    def test_remove_existing_passenger(self):
        self.train.passengers = ['Ivan', 'Gosho']

        expected_result = self.train.remove('Ivan')
        self.assertEqual("Removed Ivan", expected_result)
        self.assertEqual(['Gosho'], self.train.passengers)

if __name__ == '__main__':
    main()