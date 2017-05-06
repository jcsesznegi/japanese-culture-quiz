import sys, os, datetime

class ValidateHelper(object):
    @classmethod
    def validate_int(cls, value):
        if isinstance(value, str):
            value = int(value)
        else:
            assert(isinstance(value, int))
        return value

    @classmethod
    def validate_string(cls, value):
        assert(isinstance(value, str))
        return value

    @classmethod
    def validate_datetime(cls, value):
        assert(isinstance(value, datetime.datetime))
        return value

    @classmethod
    def validate_email(cls, value):
        assert('@' in value)
        return value

    @classmethod
    def validate_test(cls, value):
        return value

