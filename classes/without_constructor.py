# -- coding: UTF-8 --

"""
Given an input dictionary in the form of a JSON how will you construct an
instance of a class without explicitly calling the class constructor.
"""

import argparse
import logging
import logging.config
import json

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
    """ Main function"""
    setup_logging()

    my_dict = {'x': 10, 'y': 20}

    my_dict = json.dumps(my_dict)

    obj_1 = json.loads(my_dict, object_hook=lambda val: JsonData(**val))
    print(obj_1)
    print(type(obj_1))


if __name__ == '__main__':
    main()
