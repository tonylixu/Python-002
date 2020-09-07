# -*- coding: utf-8 -*-
"""Dog class"""
from Animal import Animal


class Dog(Animal):
    sound = 'wang'

    def __init__(self, name, category, size,  character):
        super().__init__(category, size, character)
        self.name = name

    @property
    def is_dangerous(self):
        if Dog.ANIMAL_SIZE[self.size] >= 2 \
                and Dog.ANIMAL_FEEDING[self.category] == 1 \
                and self.character == 'dangerous':
            return True
        return False

    @property
    def is_pet(self):
        if self.is_dangerous:
            return False
        return True

    @staticmethod
    def make_sounds():
        print(f'{Dog.sound}, {Dog.sound}, {Dog.sound},...')


if __name__ == '__main__':
    dog1 = Dog('dog1', 'meat', 'medium', 'dangerous')
    dog1.make_sounds()
