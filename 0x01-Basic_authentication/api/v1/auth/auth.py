#!/usr/bin/env python3

'''
Module for authenticating and authorizing users
'''

from flask import request
from typing import List, TypeVar
import re


class Auth:
    '''
    Class for authentication
    '''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''
        Method to check if path requires authentication
        '''
        if path is not None and excluded_paths is not None:
            for excluded_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''

                if excluded_path[-1] == '*':
                    pattern = '{}.*'.format(excluded_path[0:-1])
                elif excluded_path[-1] == '/':
                    pattern = '{}/*'.format(excluded_path[0:-1])
                else:
                    pattern = '{}/*'.format(excluded_path)

                if re.match(pattern, path):
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        '''
        Request for the authorization header field 
        '''
        if request is not None:
            return request.headers.get('Authorization', None)
        
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        '''
        Identify current user from request
        '''
        return None
