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
    """

    def __init__(self, unit_1, unit_2, conversion_data):
        self.unit_1 = unit_1
        self.unit_2 = unit_2
        self.offset = None
        self.multiplier = None
        self.conversion_data = conversion_data
        self.find_params()

    def find_params(self):
        """
        The unit conversion is in the form of a linear equation y = m*x + c, where the multiplier is m and offset is c.
        The objective of the function is to find the multiplier and the constant for a particular conversion from
        unit_1 to unit_2
        :ivar self.multiplier: The multiplier in equation y=mx+c
        :vartype self.multiplier: float

        :ivar self.offset: The offset in equation y=mx+c
        :vartype self.offset: float

        :return: None
        """
        for conversion in self.conversion_data:
            if conversion["from_unit"] == self.unit_1.unit and conversion["to_unit"] == self.unit_2.unit:
                self.multiplier = conversion['multiplier']
                self.offset = conversion['offset']

        if self.unit_1.quantity != self.unit_2.quantity:
            raise TypeError("The units must be of same quantity")

        if self.multiplier is None and self.offset is None:
            raise NameError("The conversion is not defined for the mentioned units")

    def is_acceptable(self, value):
        """
        To find if the input value is greater then the lower limit assigned for each unit
        :ivar value: Input value from the user
        :vartype value: float
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


class Units(object):
    def __init__(self, d):
        self.kelvin = None
        self.millimeter = None
        self.centimeter = None
        self.kilometer = None
        self.meter = None
        self.fahrenheit = None
        self.celsius = None
        for a, b in d.items():
            if isinstance(b, (list, tuple)):

                setattr(self, a, [Units(x) if isinstance(x, dict) else x for x in b])
            else:
                setattr(self, a, Units(b) if isinstance(b, dict) else b)

    def __repr__(self):
        return str(self.__dict__)


def main():
    """ Main Function"""

    with open("units.json") as file:
        data = json.load(file)

    with open("conv.json") as file:
        conversions = json.load(file)

    units = Units(data)
    unit_1 = units.kelvin
    unit_2 = units.millimeter

    test_1 = UnitConversion(unit_1, unit_2, conversions)
    final_value = test_1.convert(32)
    print(final_value)


if __name__ == "__main__":
    main()
