#!/usr/bin/env python3

'''
Module for authenticating and authorizing users
'''

import re
import base64
import binascii
from typing import Tuple, TypeVar

from .auth import Auth
# from models.use import User


class BasicAuth(Auth):
    '''
    Class for basic authentication
    '''
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        '''
        Method to extract base64 from authorization header
        '''
        if type(authorization_header) == str:
            pattern = r'Basic (?P<token>.+)'
            field_match = re.fullmatch(pattern, authorization_header.strip())

            if field_match is not None:
                return field_match.group('token')

        return None
