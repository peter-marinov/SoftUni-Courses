import unittest

from project.student import Student


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student('Gosho', {'Math': [4], 'Music': [3]})

    def test_if_no_courses_are_set(self):
        self.new_student = Student('Ivan')
        self.assertEqual({}, self.new_student.courses)

    def test_correct_initializing(self):
        self.assertEqual("Gosho", self.student.name)
        self.assertEqual({'Math': [4], 'Music': [3]}, self.student.courses)

    def test_enroll_add_existing_course(self):
        expected_result = self.student.enroll('Math', [6, 5], "")

        self.assertEqual(expected_result, "Course already added. Notes have been updated.")
        self.assertEqual([4, 6, 5], self.student.courses['Math'])

    def test_enroll_when_course_notes_are_y_with_new_course(self):
        expected_result = self.student.enroll('Bio', [6, 5], "Y")

        self.assertEqual(expected_result, "Course and course notes have been added.")
        self.assertEqual([6, 5], self.student.courses['Bio'])

    def test_enroll_when_course_notes_are_empty_with_new_course(self):
        expected_result = self.student.enroll('Bio', [6, 5], "")

        self.assertEqual(expected_result, "Course and course notes have been added.")
        self.assertEqual([6, 5], self.student.courses['Bio'])

    def test_enroll_when_course_notes_are_not_y_or_empty_with_new_course(self):
        expected_result = self.student.enroll('Bio', [6, 5], "empty")

        self.assertEqual(expected_result, "Course has been added.")
        self.assertEqual([], self.student.courses['Bio'])

    def test_add_notes_in_existing_course(self):
        expected_result = self.student.add_notes('Math', 3)

        self.assertEqual([4, 3], self.student.courses['Math'])
        self.assertEqual(expected_result, "Notes have been updated")

    def test_add_notes_in_not_existing_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('Bio', 3)

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_with_existing_course(self):
        expected_result = self.student.leave_course('Math')

        self.assertEqual("Course has been removed", expected_result)
        self.assertNotIn('Math', self.student.courses)

    def test_leave_course_with_not_existing_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('Bio')

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))



if __name__ == '__main__':
    unittest.main()