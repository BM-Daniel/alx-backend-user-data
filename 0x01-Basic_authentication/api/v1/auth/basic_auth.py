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
