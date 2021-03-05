# -- coding: UTF-8 --

""" Implement a tree and store its information in the class """

import logging.config

__author__ = 'saranya@gyandata.com'

LOGGER = logging.getLogger('root')
LOGGER_CONFIG_PATH = 'config/logging.json'


class Tree:
    """Class Description: To implement tree data structure using classes"""
    def __init__(self, name):
        self.parent = None
        self.child = []
        self.name = name

    def add_children(self, c_obj):
        """
        Method Description: To assign the parent to the class instance
        :param c_obj: Child object
        :type c_obj: list
        """
        for child in c_obj:
            self.child.append(child)
            child.parent = self.name

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.name) + "\n"
        for child in self.child:
            ret += child.__str__(level + 1)
        return ret
