from string import ascii_letters, digits
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class CharactersValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Username must contain only letters, digits, and underscores!"
        else:
            self.__message = value

    def __call__(self, value: str, *args, **kwargs):
        allowed_characters = ascii_letters + digits + '_'


        for char in value:
            if char not in allowed_characters:
                raise ValidationError(self.message)


@deconstructible
class AgeValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Age requirement: 21 years and above."

    def __call__(self, value: int, *args, **kwargs):
        if value < 21:
            raise ValidationError(self.message)
