#!/usr/bin/env python3

'''
Write a function called filter_datum that returns the log message obfuscated
The function should use a regex to replace occurrences of certain field values
'''

import logging
import re
from typing import List


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    '''
    Write a function called filter_datum that returns the log message
    obfuscated
    The function should use a regex to replace occurrences of certain
    field values
    '''
    for field in fields:
        message = re.sub(field + '=.*?' + separator,
                         field + '=' + redaction + separator, message)

    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        '''
        Implement the format method to filter values in incoming log records
        using filter_datum. Values for fields in fields should be filtered.
        '''
        meessage = super(RedactingFormatter, self).format(record)
        redacted = filter_datum(self.fields, self.REDACTION, meessage,
                                self.SEPARATOR)
        return redacted


def get_logger() -> logging.Logger:
    '''
    Implement a get_logger function that takes no arguments and returns a
    logging.Logger object.
    '''
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logging.propagate = False

    handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
