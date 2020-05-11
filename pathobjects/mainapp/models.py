from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


# /new/file.pem

def path_validator(value):
    if not value.startswith('/'):
        raise ValidationError("a Путь должен начинаться со /")


class PathValidator(RegexValidator):

    def __init__(self):
        super().__init__(regex=r'.pem$')

    def __call__(self, value):
        path_validator(value)
        super().__call__(value)


class PathField(models.CharField):
    default_validators = [PathValidator()]


class FilePath(models.Model):
    path = PathField(max_length=64, unique=True)
