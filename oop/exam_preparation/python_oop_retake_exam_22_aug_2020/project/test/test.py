from unittest import TestCase, main

#from exam_preparation.python_oop_retake_exam_22_aug_2020.project.student_report_card import StudentReportCard
from project.student_report_card import StudentReportCard


class TestStudentReportCard(TestCase):
    def setUp(self):
        self.card = StudentReportCard('Peter', 3)

    def test_correct_initializing(self):
        self.assertEqual('Peter', self.card.student_name)
        self.assertEqual(3, self.card.school_year)
        self.assertEqual({}, self.card.grades_by_subject)

    def test_student_name_empty_string_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            new_card = StudentReportCard('', 3)

        self.assertEqual("Student Name cannot be an empty string!", str(ve.exception))

    def test_school_year_equal_to_zero_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            new_card = StudentReportCard('Peter', 0)

        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

    def test_school_year_equal_to_13_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            new_card = StudentReportCard('Peter', 13)

        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

    def test_init_edge_case_year_1(self):
        new_student = StudentReportCard('student1', 1)
        self.assertEqual('student1', new_student.student_name)
        self.assertEqual(1, new_student.school_year)
        self.assertEqual({}, new_student.grades_by_subject)

    def test_init_edge_case_year_12(self):
        new_student = StudentReportCard('student2', 12)
        self.assertEqual('student2', new_student.student_name)
        self.assertEqual(12, new_student.school_year)
        self.assertEqual({}, new_student.grades_by_subject)
   ####

    def test_add_grade_when_not_exists(self):
        self.card.add_grade('math', 4.50)
        self.assertEqual({'math': [4.50]}, self.card.grades_by_subject)


    def test_add_grade_when_exists(self):
        self.card.add_grade('math', 4.50)
        self.card.add_grade('bio', 5.50)
        self.card.add_grade('math', 3.50)
        self.assertEqual({'math': [4.50, 3.50], 'bio': [5.50]}, self.card.grades_by_subject)
    #####

    def test_average_grade_by_subject(self):
        self.card.add_grade('math', 4.50)
        self.card.add_grade('bio', 5.50)
        self.card.add_grade('math', 3.50)

        expected_result = self.card.average_grade_by_subject()
        self.assertEqual(f"math: 4.00\n"
                         f"bio: 5.50", expected_result)

    def test_average_grade_for_all_subjects(self):
        self.card.add_grade('math', 4.50)
        self.card.add_grade('bio', 5.00)
        self.card.add_grade('math', 3.50)

        expected_result = self.card.average_grade_for_all_subjects()
        self.assertEqual("Average Grade: 4.33", expected_result)

    def test__repr__with_data(self):
        self.card.add_grade('math', 4.50)
        self.card.add_grade('bio', 5.00)
        self.card.add_grade('math', 3.50)

        expected_result = repr(self.card)
        self.assertEqual("Name: Peter\n"
                         "Year: 3\n"
                         "----------\n"
                         "math: 4.00\n"
                         "bio: 5.00\n"
                         "----------\n"
                         "Average Grade: 4.33", expected_result)



if __name__ == '__main__':
    main()