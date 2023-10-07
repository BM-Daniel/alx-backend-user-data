#!/usr/bin/env python3

'''
Module to encrypt user password
'''

import bcrypt


def hash_password(password: str) -> bytes:
    '''
    Implement a hash_password function that expects one string argument name
    password and returns a salted, hashed password, which is a byte string.
    '''
    byte_value = password.encode()
    hash_value = bcrypt.hashpw(byte_value, bcrypt.gensalt())

    return hash_value


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''
    Implement an is_valid function that expects 2 arguments and returns a
    boolean.
    '''
    return bcrypt.checkpw(password.encode(), hashed_password)
