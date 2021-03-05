# -- coding: UTF-8 --

""" Main file for unit conversion"""
import argparse
import logging
import logging.config
import json

from classes.unit_conversions import Unit, UnitConversion

__author__ = 'saranya@gyandata.com'

LOGGER = logging.getLogger('root')
LOGGER_CONFIG_PATH = 'config/logging.json'


def arg_parse():
    """
    Function Description: To parse command line arguments

    :return: command line arguments passed
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', help="Enter the first unit for unit conversion", type=str)
    parser.add_argument('-b', help="Enter the second unit for unit conversion", type=str)
    parser.add_argument("-val", help="The value for which unit conversion should happen", type=float)
    return parser.parse_args()


def setup_logging(default_path=LOGGER_CONFIG_PATH):
    """
    Function Description: To setup logging using the json file
    :param default_path: Path of the configuration file
    :type default_path: str
    """
    with open(default_path, 'rt') as file:
        config = json.load(file)
    logging.config.dictConfig(config)


def main():
    """Main Function"""
    setup_logging()
    args = arg_parse()
    with open("units.json") as file:
        units_data = json.load(file)

    with open("conv.json") as file:
        conversions = json.load(file)

    units = {}
    for data in units_data:
        units[data["name"]] = Unit(data["unit"], data["quantity"], data["lower_limit"])

    unit_1 = None
    unit_2 = None
    multiplier = None
    offset = None

    try:
        unit_1 = units[args.a]
    except KeyError:
        LOGGER.error("%s is not defined", args.a)

    try:
        unit_2 = units[args.b]
    except KeyError:
        LOGGER.error("%s is not defined", args.b)

    try:
        for conversion in conversions:
            if conversion["from_unit"] == unit_1.unit and conversion["to_unit"] == unit_2.unit:
                multiplier = conversion['multiplier']
                offset = conversion['offset']
        if unit_1.quantity != unit_2.quantity:
            raise TypeError("The units must be of same quantity")

        if multiplier is None and offset is None:
            raise NameError("The conversion is not defined for the mentioned units")

        test_1 = UnitConversion(unit_1, unit_2, multiplier, offset)
        final_value = test_1.convert(args.val)
        print("The converted value is %f " % final_value)

    except AttributeError:
        LOGGER.error("")


if __name__ == "__main__":
    main()
