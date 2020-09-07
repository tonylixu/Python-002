# -*- coding: utf-8 -*-
"""Cat class"""
from Animal import Animal


class Cat(Animal):
    sound = 'miao'

    def __init__(self, name, category, size,  character):
        super().__init__(category, size, character)
        self.name = name

    @property
    def is_dangerous(self):
        if Cat.ANIMAL_SIZE[self.size] >= 2 \
                and Cat.ANIMAL_FEEDING[self.category] == 1 \
                and self.character == 'dangerous':
            return True
        return False

    @property
    def is_pet(self):
        if self.is_dangerous:
            return False
        return True


if __name__ == '__main__':
    cat1 = Cat('cat1', 'meat', 'medium', 'dangerous')
    print(f'Is cat1 dangerous? {cat1.is_dangerous}')
    cat2 = Cat('cat2', 'meat', 'small', 'dangerous')
    print(f'Is cat2 dangerous? {cat2.is_dangerous}')