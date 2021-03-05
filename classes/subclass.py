# -- coding: UTF-8 --

"""
Given classes A and B, B being a subclass of A, show how you will construct
an instance of A given an instance of B. Can you construct an instance of B
given an instance of A? If yes, show.
"""

import logging
import logging.config
import json

__author__ = 'saranya@gyandata.com'

LOGGER = logging.getLogger('root')
LOGGER_CONFIG_PATH = 'config/logging.json'


class SuperClass:
    """
    Class Description: This is going to be our superclass for which sub classes can be created
    """
    pass


class SubClass(SuperClass):
    """
    Class Description: This is going to be our subclass
    """
    pass
