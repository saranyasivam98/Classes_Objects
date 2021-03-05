# -- coding: UTF-8 --

""" Construct classes which will allow you to store units and perform direct unit
conversion
"""

import logging
import logging.config
import json

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
                return self.multiplier * value + self.offset

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


def main():
    """ Main Function"""

    with open("units.json") as file:
        units_data = json.load(file)

    with open("conv.json") as file:
        conversions = json.load(file)

    units = {}
    for data in units_data:
        units[data["name"]] = Unit(data["unit"], data["quantity"], data["lower_limit"])

    unit_1 = units['celsius']
    unit_2 = units['fahrenheit']

    multiplier = None
    offset = None

    for conversion in conversions:
        if conversion["from_unit"] == unit_1.unit and conversion["to_unit"] == unit_2.unit:
            multiplier = conversion['multiplier']
            offset = conversion['offset']
    if unit_1.quantity != unit_2.quantity:
        raise TypeError("The units must be of same quantity")

    if multiplier is None and offset is None:
        raise NameError("The conversion is not defined for the mentioned units")

    test_1 = UnitConversion(unit_1, unit_2, multiplier, offset)
    final_value = test_1.convert(0)
    print("The converted value is %f " % final_value)


if __name__ == "__main__":
    main()

