# -- coding: UTF-8 --

""" Main file for subclasses """

import logging
import logging.config
import json

from classes.subclass import SuperClass, SubClass

__author__ = 'saranya@gyandata.com'

LOGGER = logging.getLogger('root')
LOGGER_CONFIG_PATH = 'config/logging.json'


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
    """ Main Function """
    setup_logging()
    # Creating instance of subclass using superclass instance
    a_1 = SuperClass()
    b_1 = a_1.__class__.__subclasses__()[0]()
    LOGGER.info("Type of b1 is: %s", type(b_1))

    b_2 = SubClass()
    # b_2.__class__ = SuperClass
    # b_2.meth_a()
    a_2 = b_2.__class__.__base__()
    LOGGER.info("Type of a2 is: %s", type(a_2))


if __name__ == '__main__':
    main()
