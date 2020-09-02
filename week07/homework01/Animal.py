# -*- coding: utf-8 -*-
"""Animal Abstract class"""

from abc import ABC


class Animal(ABC):
    def __init__(self):
        self.type = None
        self.size = None
        self.character = None
        self.is_dangerous = None