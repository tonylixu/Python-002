# -*- coding: utf-8 -*-
"""Animal Abstract class"""

from abc import ABC, abstractmethod


class Animal(ABC):
    # Class property
    ANIMAL_SIZE = {'small': 1, 'medium': 2, 'large': 3}
    ANIMAL_FEEDING = {'meat': 1, 'grass': 2}

    def __init__(self, category, size, character):
        self.category = category
        self.size = size
        self.character = character

    @property
    @abstractmethod
    def is_dangerous(self):
        pass
