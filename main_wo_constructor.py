# -- coding: UTF-8 --

""" Main file for without_constructor.py"""

import logging
import logging.config
import json

from classes.without_constructor import JsonData

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
    """ Main function"""
    setup_logging()

    my_dict = {'x': 10, 'y': 20}

    my_dict = json.dumps(my_dict)

    obj_1 = json.loads(my_dict, object_hook=lambda val: JsonData(**val))
    LOGGER.info(obj_1)
    LOGGER.info(type(obj_1))


if __name__ == '__main__':
    main()
