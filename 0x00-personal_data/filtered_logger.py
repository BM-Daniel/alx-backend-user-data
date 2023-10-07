#!/usr/bin/env python3

'''
Write a function called filter_datum that returns the log message obfuscated
The function should use a regex to replace occurrences of certain field values
'''

import logging
import re
from typing import List


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
