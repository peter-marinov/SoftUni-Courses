from unittest import TestCase, main

#from python_oop_exam_11_december_2021.project.team import Team
from project.team import Team


class TestTeam(TestCase):
    def setUp(self):
        self.team = Team('TeamName')

    def test_correct_initializing(self):
        self.assertEqual('TeamName', self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name_not_letter_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            new_team = Team('1233ad sd')

        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

    def test_add_member_when_no_members_exists(self):
        expected_result = self.team.add_member(Ivan=10, George=15, Stamat=15)

        self.assertEqual({'Ivan': 10, 'George': 15, 'Stamat': 15}, self.team.members)
        self.assertEqual("Successfully added: Ivan, George, Stamat", expected_result)

    def test_add_member_when_some_members_exist(self):
        self.team.add_member(George=15)
        expected_result = self.team.add_member(Ivan=10, George=17, Stamat=15)
        self.assertEqual({'George': 15, 'Ivan': 10, 'Stamat': 15}, self.team.members)
        self.assertEqual("Successfully added: Ivan, Stamat", expected_result)

    def test_add_member_when_all_exists(self):
        self.team.add_member(Ivan=10, George=15, Stamat=15)
        expected_result = self.team.add_member(Ivan=10, George=15, Stamat=15)
        self.assertEqual({'Ivan': 10, 'George': 15, 'Stamat': 15}, self.team.members)
        self.assertEqual("Successfully added: ", expected_result)

    def test_remove_member_the_one_member_which_exists(self):
        self.team.add_member(George=15)
        expected_result = self.team.remove_member('George')
        self.assertEqual({}, self.team.members)
        self.assertEqual("Member George removed", expected_result)

    def test_remove_member_when_members_left(self):
        self.team.add_member(Ivan=10, George=15, Stamat=15)
        expected_result = self.team.remove_member('George')
        self.assertEqual({'Ivan': 10, 'Stamat': 15}, self.team.members)
        self.assertEqual("Member George removed", expected_result)

    def test_remove_not_existing_member(self):
        self.team.add_member(George=15)
        expected_result = self.team.remove_member('Peter')
        self.assertEqual({'George': 15}, self.team.members)
        self.assertEqual("Member with name Peter does not exist", expected_result)

    def test_gt_when_first_team_have_more_members(self):
        self.team.add_member(Ivan=10, George=15, Stamat=15)
        second_team = Team('SecondTeam')
        second_team.add_member(Ivan=10)
        expected_result_true = self.team > second_team
        expected_result_false = self.team < second_team
        self.assertEqual(True, expected_result_true)
        self.assertEqual(False, expected_result_false)

    def test_len_of_team(self):
        self.team.add_member(Ivan=10, George=15, Stamat=15)
        self.assertEqual(3, len(self.team))

    def test_add_two_teams_method(self):
        self.team.add_member(Ivan=10, George=15)
        second_team = Team('SecondTeam')
        self.team.add_member(Ivan=12, Stamat=15)
        new_team = self.team + second_team
        self.assertEqual('TeamNameSecondTeam', new_team.name)
        self.assertEqual(3, len(new_team))
        self.assertTrue(isinstance(new_team, Team))

    def test_add_when_have_members(self):
        second_team = Team('SecondName')
        self.team.add_member(Gosho=22, Stamat=16)
        second_team.add_member(Ivan=20, Gosho=22, Stamat=16)
        new_team = self.team + second_team

        self.assertEqual('TeamNameSecondName', new_team.name)
        self.assertEqual({
            'Gosho': 22,
            'Stamat': 16,
            'Ivan': 20
        }, new_team.members)
        self.assertTrue(isinstance(new_team, Team))

    def test__str_when_no_members(self):
        actual_result = "Team name: TeamName"

        self.assertEqual(actual_result, str(self.team))

    def test_str_when_members_same_age(self):
        self.team.add_member(Ivan=22, Gosho=22, Stamat=16)

        actual_result = "Team name: TeamName\n" \
                        "Member: Gosho - 22-years old\n" \
                        "Member: Ivan - 22-years old\n" \
                        "Member: Stamat - 16-years old"

        self.assertEqual(actual_result, str(self.team))


if __name__ == '__main__':
    main()