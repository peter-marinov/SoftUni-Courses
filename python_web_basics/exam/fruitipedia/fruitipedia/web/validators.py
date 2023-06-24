from django.core.exceptions import ValidationError


def check_if_string_starts_with_letter(value):
    if not value[0].isalpha():
        raise ValidationError('Your name must start with a letter!')


def check_if_string_only_letters(value):
    if not value.isalpha():
        raise ValidationError('Fruit name should contain only letters!')