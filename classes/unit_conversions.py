# -- coding: UTF-8 --

""" Construct classes which will allow you to store units and perform direct unit
conversion
"""

import logging
import logging.config

__author__ = 'saranya@gyandata.com'

LOGGER = logging.getLogger('root')
LOGGER_CONFIG_PATH = 'config/logging.json'


class UnitConversion:
    """
    To store the parameters and perform unit conversion
    :ivar unit_1: The first unit in unit conversion
    :vartype unit_1: Unit

    :ivar unit_2: The second unit in unit conversion
    :vartype unit_2: Unit

    :ivar multiplier: The value of 'm' in the unit conversion equation y = m*x + c
    :vartype multiplier: float

    :ivar offset: The value of 'c' in the unit conversion equation y = m*x + c
    :vartype offset: float
    """

    def __init__(self, unit_1, unit_2, multiplier, offset):
        self.unit_1 = unit_1
        self.unit_2 = unit_2
        self.offset = offset
        self.multiplier = multiplier

    def is_acceptable(self, value):
        """
        To find if the input value is greater then the lower limit assigned for each unit
        :param value: Input value from the user
        :type value: float
        :return: If the input value is greater than the lower limit
        :rtype: bool
        """
        if self.unit_1.lower_limit < value:
            return True

    def convert(self, value):
        """
        To perform unit conversion on an input value and return the conversion.
        :param value: Input from the user
        :return: The converted final value
        :rtype: float
        """
        flag = self.is_acceptable(value)
        if flag:

            if self.unit_2 == self.unit_1:
                return value
            else:
                final_value = self.multiplier * value + self.offset
                return final_value

        else:
            raise ValueError("The entered value is lesser the lower limit: %d allowed for the "
                             "unit" % self.unit_1.lower_limit)


class Unit:
    """
    A class to store units

    :ivar unit: Short name of the units that is widely used
    :vartype unit: str

    :ivar quantity: The physical quantity to which the unit belongs
    :vartype quantity: str

    :ivar lower_limit: The least value the unit can take
    :vartype lower_limit: float
    """

    def __init__(self, unit, quantity, lower_limit):
        self.unit = unit
        self.quantity = quantity
        self.lower_limit = lower_limit
