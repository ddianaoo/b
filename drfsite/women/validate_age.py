from django.core.exceptions import ValidationError


def validate_age(age):
    if age < 1:
        raise ValidationError("Age must be a positive value")