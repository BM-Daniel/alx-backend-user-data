#!/usr/bin/env python3

'''
Write a function called filter_datum that returns the log message obfuscated
The function should use a regex to replace occurrences of certain field values
'''

import logging
import re
from typing import List
import os
import mysql.connector


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


def get_db() -> mysql.connector.connection.MySQLConnection:
    '''
    Database credentials should NEVER be stored in code or checked into version
    control. One secure option is to store them as environment variable on the
    application server.
    '''
    db_host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME", "")
    db_user = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    db_pwd = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    connection = mysql.connector.connect(host=db_host, port=3306, user=db_user,
                                         password=db_pwd, database=db_name)

    return connection


def main():
    '''
    Main function for the module
    '''
    db = get_db()
    logger = get_logger()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM users;')
    fields = cursor.column_names

    for row in cursor:
        message = ''.join('{}={}'.format(key, value)
                          for key, value in zip(fields, row))
        logger.info(message.strip())

    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
