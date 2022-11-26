import unittest

from project.mammal import Mammal


class TestMammal(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal('Gosho', 'cat', 'maow')

    def test_correct_initializing(self):
        self.assertEqual(self.mammal.name, 'Gosho')
        self.assertEqual(self.mammal.type, 'cat')
        self.assertEqual(self.mammal.sound, 'maow')
        self.assertEqual(self.mammal._Mammal__kingdom, 'animals')

    def test_if_make_sound_returns_correct_message(self):
        self.assertEqual(self.mammal.make_sound(), "Gosho makes maow")

    def test_if_get_kingdom_returns_correct_message(self):
        self.assertEqual(self.mammal.get_kingdom(), 'animals')

    def test_if_info_returns_correct_message(self):
        self.assertEqual(self.mammal.info(), "Gosho is of type cat")

if __name__ == '__main__':
    unittest.main()