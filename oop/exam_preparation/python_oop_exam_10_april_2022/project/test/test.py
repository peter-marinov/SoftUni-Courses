from unittest import TestCase, main

from project.movie import Movie


class TestMovie(TestCase):
    def setUp(self):
        self.movie = Movie('some_movie', 2000, 4.25)

    def test_correct_initializing(self):
        self.assertEqual('some_movie', self.movie.name)
        self.assertEqual(2000, self.movie.year)
        self.assertEqual(4.25, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_with_empty_str_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            new_movie = Movie('', 2000, 4.25)
        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_year_before_1887_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            new_movie = Movie('name', 1886, 4.25)
        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_add_actor_with_different_name(self):
        self.movie.add_actor('some_name1')
        self.movie.add_actor('some_name2')
        self.assertEqual(['some_name1', 'some_name2'], self.movie.actors)

    def test_add_actor_when_name_already_exists(self):
        self.movie.add_actor('some_name1')
        expected_result = self.movie.add_actor('some_name1')

        self.assertEqual(['some_name1'], self.movie.actors)
        self.assertEqual("some_name1 is already added in the list of actors!", expected_result)

    def test_gt_when_first_rating_is_bigger(self):
        other_movie = Movie('other_movie', 2005, 2.75)

        expected_result = self.movie > other_movie
        self.assertEqual('"some_movie" is better than "other_movie"', expected_result)

    def test_gt_when_second_rating_is_bigger(self):
        other_movie = Movie('other_movie', 2005, 8.75)

        expected_result = self.movie > other_movie
        self.assertEqual('"other_movie" is better than "some_movie"', expected_result)

    def test_repr_with_cast(self):
        self.movie.add_actor('some_name1')
        self.movie.add_actor('some_name2')

        actual_result = "Name: some_movie\n" \
                        "Year of Release: 2000\n" \
                        "Rating: 4.25\n" \
                        "Cast: some_name1, some_name2"

        self.assertEqual(actual_result, self.movie.__repr__())

    def test_repr_with_no_cast(self):
        actual_result = "Name: some_movie\n" \
                        "Year of Release: 2000\n" \
                        "Rating: 4.25\n" \
                        "Cast: "

        self.assertEqual(actual_result, self.movie.__repr__())


if __name__ == '__main__':
    main()
