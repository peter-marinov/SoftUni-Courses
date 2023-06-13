from django.core.validators import ValidationError


def image_size_validator_5mb(image_obj):
    max_size = 5 * 1024 * 1024
    if image_obj.size > max_size:
        return ValidationError('Image size can not be larger than 5MB')