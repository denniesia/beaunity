from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError

@deconstructible
class OnlyDigitsValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value or 'The phone number must consist of digits only.'

    def __call__(self, value):
        if not value.isdigit():
            raise ValidationError(self.message)

@deconstructible
class FourUniqueDigitsValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value or "Your secret key must have 4 unique digits!"

    def __call__(self, value):
        key = []
        for char in value:
            if char.isdigit() and char not in key:
                key.append(char)
            else:
                raise ValidationError(self.message)
        if len(key) != 4:
            raise ValidationError(self.message)