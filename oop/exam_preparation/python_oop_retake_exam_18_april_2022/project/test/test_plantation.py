from unittest import TestCase, main

from project.plantation import Plantation


class TestPlantation(TestCase):
    def setUp(self):
        self.plantation = Plantation(5)

    def test_correct_initializing(self):
        self.assertEqual(5, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_lower_than_zero_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            new_plantation = Plantation(-1)
        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_hire_worker_when_already_hired_expect_value_error(self):
        self.plantation.workers = ['worker1']
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker('worker1')
        self.assertEqual("Worker already hired!", str(ve.exception))

    def test_hire_worker_when_possible(self):
        self.plantation.workers = ['worker1']
        self.plantation.hire_worker('worker2')
        expected_result = self.plantation.hire_worker('worker3')

        self.assertEqual(['worker1', 'worker2', 'worker3'], self.plantation.workers)
        self.assertEqual("worker3 successfully hired.", expected_result)

    def test_planting_when_working_not_hired_expect_value_error(self):
        self.plantation.hire_worker('worker1')
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting('worker2', 'flower')

        self.assertEqual("Worker with name worker2 is not hired!", str(ve.exception))

    def test_planting_when_no_space_expect_value_error(self):
        self.plantation.hire_worker('worker1')
        self.plantation.hire_worker('worker2')
        self.plantation.planting('worker1', 'flower1')
        self.plantation.planting('worker1', 'flower2')
        self.plantation.planting('worker1', 'flower3')
        self.plantation.planting('worker1', 'flower4')
        self.plantation.planting('worker1', 'flower5')

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting('worker2', 'flower6')

        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_planting_when_first_flower_for_worker(self):
        self.plantation.hire_worker('worker1')
        self.plantation.hire_worker('worker2')
        self.plantation.plants = {'worker2': ['flower2']}
        expected_result = self.plantation.planting('worker1', 'flower1')

        self.assertEqual({'worker2': ['flower2'], 'worker1': ['flower1']}, self.plantation.plants)
        self.assertEqual("worker1 planted it's first flower1.", expected_result)

    def test_planting_when_not_the_fist_plant(self):
        self.plantation.hire_worker('worker1')
        self.plantation.hire_worker('worker2')
        self.plantation.planting('worker1', 'flower1')
        self.plantation.planting('worker2', 'flower2')
        expected_result = self.plantation.planting('worker1', 'flower3')

        self.assertEqual({'worker1': ['flower1', 'flower3'], 'worker2': ['flower2']}, self.plantation.plants)
        self.assertEqual("worker1 planted flower3.", expected_result)

    def test_len_when_no_plants(self):
        self.assertEqual(0, len(self.plantation))

    def test_len_number_of_plants(self):
        self.plantation.hire_worker('worker1')
        self.plantation.hire_worker('worker2')
        self.plantation.planting('worker1', 'flower1')
        self.plantation.planting('worker2', 'flower2')
        self.plantation.planting('worker1', 'flower3')

        self.assertEqual(3, len(self.plantation))

    def test_str_method_output(self):
        self.plantation.hire_worker('worker1')
        self.plantation.hire_worker('worker2')
        self.plantation.planting('worker1', 'flower1')
        self.plantation.planting('worker2', 'flower2')
        self.plantation.planting('worker1', 'flower3')

        actual_result = 'Plantation size: 5\n' \
                        'worker1, worker2\n' \
                        'worker1 planted: flower1, flower3\n' \
                        'worker2 planted: flower2'\

        self.assertEqual(actual_result, str(self.plantation))

    def test_str_method_output_when_no_workers_and_plants(self):
        actual_result = 'Plantation size: 5\n'
        self.assertEqual(actual_result, str(self.plantation))

    def test_repr_method_output(self):
        self.plantation.hire_worker('worker1')
        self.plantation.hire_worker('worker2')
        self.plantation.planting('worker1', 'flower1')
        self.plantation.planting('worker2', 'flower2')
        self.plantation.planting('worker1', 'flower3')

        actual_result = 'Size: 5\n' \
                        'Workers: worker1, worker2'

        self.assertEqual(actual_result, self.plantation.__repr__())

    def test_repr_method_output_when_no_workers(self):
        actual_result = 'Size: 5\n' \
                        'Workers: '
        self.assertEqual(actual_result, self.plantation.__repr__())

if __name__ == '__main__':
    main()