from django.core.exceptions import ValidationError
from django.test import TestCase

from lost_and_found.objects_posts.validators import validate_phone, INVALID_PHONE_MESSAGE


class ValidatePhoneTests(TestCase):
    def test_validate_phone__when_starts_with_plus__expect_nothing(self):
        phone_number = '+123456'
        validate_phone(phone_number)

    def test_validate_phone__when_starts_with_zero__expect_nothing(self):
        phone_number = '0123456'
        validate_phone(phone_number)

    def test_validate_phone__when_not_starts_with_zero_or_plus__expect_raise(self):
        phone_number = '4123456'
        with self.assertRaises(ValidationError) as context:
            validate_phone(phone_number)

        self.assertIsNotNone(context.exception)
        self.assertEqual(INVALID_PHONE_MESSAGE, context.exception.message)
