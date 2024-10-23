from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class YearValidator(object):
    def __init__(self, message=None):
        self.message = message


    @property
    def message(self):
        return self.__message


    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Year must be between 1999 and 2030!"
        else:
            self.__message = value

    def __call__(self, value: int, *args, **kwargs):
        if value < 1999 or value > 2030:
            raise ValidationError(self.message)