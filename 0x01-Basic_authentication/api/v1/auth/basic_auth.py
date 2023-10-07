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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        '''
        Method to decode base64 encoded value from authorization header
        '''
        if type(base64_authorization_header) == str:
            try:
                result = base64.b64decode(base64_authorization_header,
                                          validate=True)

                return result.decode('utf-8')
            except (binascii.Error, UnicodeDecodeError):
                return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        '''
        Method to extract the user credentials from the base64 decoded value
        '''
        if type(decoded_base64_authorization_header) == str:
            pattern = r'(?P<user>[^:]+):(?P<password>.+)'
            field_match = re.fullmatch(
                pattern, decoded_base64_authorization_header.strip())

            if field_match is not None:
                user = field_match.group('user')
                password = field_match.group('password')

                return user, password

        return None, None

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        '''
        Provides info about a user based on the credentials provided
        '''
        if type(user_email) == str and type(user_pwd) == str:
            try:
                users = User.search({'email': user_email})
            except Exception:
                return None

            if len(users) <= 0:
                return None
            if users[0].is_valid_password(user_pwd):
                return users[0]

        return None
