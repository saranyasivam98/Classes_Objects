# -- coding: UTF-8 --

""" Main file for Newton Raphson"""
import argparse
import logging
import logging.config
import json

from classes.nr_classes import NewtonRaphson

__author__ = 'saranya@gyandata.com'

LOGGER = logging.getLogger('root')
LOGGER_CONFIG_PATH = 'config/logging.json'


def arg_parse():
    """
    Function Description: To parse command line arguments

    :return: command line arguments passed
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', nargs="+", type=float)
    parser.add_argument('-x', help="Initial value of x", type=float)
    parser.add_argument("-v", "--verbose", help="print extra values", default=0,
                        action="store_true")
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
    """ Main Function"""
    setup_logging()
    args = arg_parse()
    polynomial = args.p
    x = args.x
    obj = NewtonRaphson(polynomial, x)
    root, flag_root = obj.find_root
    # obj.print()
    if root:
        LOGGER.info(root)
    else:
        LOGGER.error("No real roots for this equation")


if __name__ == '__main__':
    main()
