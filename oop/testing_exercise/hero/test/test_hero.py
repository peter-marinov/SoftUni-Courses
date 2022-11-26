import unittest

from project.hero import Hero


class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("Gosho", 60, 95.5, 20.5)
        self.enemy_hero = Hero("Ivan", 50, 85.5, 10.5)

    def test_correct_initializing(self):
        self.assertEqual(self.hero.username, "Gosho")
        self.assertEqual(self.hero.level, 60)
        self.assertEqual(self.hero.health, 95.5)
        self.assertEqual(self.hero.damage, 20.5)

    def test_battle_with_enemy_with_the_same_name_as_hero_raise_exception(self):
        self.enemy_hero.username = "Gosho"
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)

        self.assertEqual(str(ex.exception), "You cannot fight yourself")

    def test_battle_with_enemy_when_your_health_is_equal_to_zero_raise_exception(self):
        self.hero.health = 0
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)

        self.assertEqual(str(ex.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle_with_enemy_when_enemy_health_is_equal_to_zero_raise_exception(self):
        self.enemy_hero.health = 0
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)

        self.assertEqual(str(ex.exception), "You cannot fight Ivan. He needs to rest")

    def test_battle_when_both_heroes_health_is_lower_than_zero(self):
        self.hero.health = 1
        self.enemy_hero.health = 1
        expected_result = self.hero.battle(self.enemy_hero)

        self.assertEqual(expected_result, "Draw")

    def test_battle_when_enemy_hero_health_is_lower_than_zero(self):
        self.enemy_hero.level = 1
        expected_result = self.hero.battle(self.enemy_hero)

        self.assertEqual(expected_result, "You win")
        self.assertEqual(self.hero.level, 61)
        self.assertEqual(self.hero.health, 90)
        self.assertEqual(self.hero.damage, 25.5)

    def test_battle_when_your_hero_health_is_lower_than_zero(self):
        self.hero.level = 1
        expected_result = self.hero.battle(self.enemy_hero)

        self.assertEqual(expected_result, "You lose")
        self.assertEqual(self.enemy_hero.level, 51)
        self.assertEqual(self.enemy_hero.health, 70)
        self.assertEqual(self.enemy_hero.damage, 15.5)

    def test_str_from_hero(self):
        expected_result = "Hero Gosho: 60 lvl\n" \
               "Health: 95.5\n" \
               "Damage: 20.5\n"

        self.assertEqual(expected_result, str(self.hero))

if __name__ == '__main__':
    unittest.main()