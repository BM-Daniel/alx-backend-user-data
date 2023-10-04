#!/usr/bin/env python3

'''
Write a function called filter_datum that returns the log message obfuscated
The function should use a regex to replace occurrences of certain field values
'''

import logging
import re


def filter_datum(fields, redaction, message, separator):
  '''
  Write a function called filter_datum that returns the log message obfuscated
  The function should use a regex to replace occurrences of certain field values
  '''
  for value in fields:
    pattern = re.compile(f'({"|".join(fields)})=[^{separator}]+')
    return pattern.sub(fr'\1={redaction}', message)
