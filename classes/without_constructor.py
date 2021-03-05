# -- coding: UTF-8 --

"""
Given an input dictionary in the form of a JSON how will you construct an
instance of a class without explicitly calling the class constructor.
"""

import logging.config


__author__ = 'saranya@gyandata.com'

LOGGER = logging.getLogger('root')
LOGGER_CONFIG_PATH = 'config/logging.json'


class JsonData:
    """ A class contains the co ordinates of a point"""
    def __init__(self, x, y):
        """
        Constructor
        :ivar x: The x coordinate of the point
        :ivar y: The y coordinate of the point
        """
        self.x = x
        self.y = y

    def __str__(self):
        return "Value of x: %d and Value of y: %d" % (self.x, self.y)
