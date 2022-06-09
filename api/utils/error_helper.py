from __future__ import annotations

class ErrorHelper():
    __code: int
    __name: str
    __description: str
    __validation: dict

    def __init__(self, code: int, name: str, description: str, validation: dict = None):
        self.__code = code
        self.__name = name
        self.__description = description
        self.__validation = validation

    # Json
    def json(self):
        result = {
            'code': self.__code,
            'name': self.__name,
            'description': self.__description
        }
        if self.__validation is not None: result['validation'] = self.__validation
        return result

    # General
    @staticmethod
    def UNKNOWN_ERROR():
        return ErrorHelper(1, 'UNKNOWN_ERROR', 'Unknown error.')

    @staticmethod
    def VALIDATION_ERROR(validation: dict):
        return ErrorHelper(4, 'VALIDATION_ERROR', 'Validation errors.', validation)

    @staticmethod
    def NOT_FOUND():
        return ErrorHelper(5, 'NOT_FOUND', 'Not found.')
