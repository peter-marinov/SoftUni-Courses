import unittest

from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle(1.25, 62.5)

    def test_correct_initializing(self):
        self.assertEqual(self.vehicle.fuel, 1.25)
        self.assertEqual(self.vehicle.horse_power, 62.5)
        self.assertEqual(self.vehicle.fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_with_not_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(10000)

        self.assertEqual(str(ex.exception), "Not enough fuel")

    def test_drive_with_enough_fuel(self):
        self.vehicle.drive(1)
        self.assertEqual(self.vehicle.fuel, 0)

    def test_refuel_with_more_than_max_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1000)

        self.assertEqual(str(ex.exception), "Too much fuel")

    def test_refuel_with_less_than_max_capacity(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(1)

        self.assertEqual(self.vehicle.fuel, 1)

    def test_str_method_output(self):
        expected_result = "The vehicle has 62.5 " \
               "horse power with 1.25 fuel left and " \
                          "1.25 fuel consumption"

        self.assertEqual(str(self.vehicle), expected_result)


if __name__ == '__main__':
    unittest.main()

