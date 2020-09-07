# -*- coding: utf-8 -*-
import Cat
import Dog


class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = {}

    def add_new_animal_by_id(self, animal):
        animal_id = id(animal)
        if animal_id in self.animals:
            raise ValueError(f"Animal {animal.__dict__['name']} already in the zoo!") from BaseException
        self.animals[animal_id] = animal

    def get_all_animals(self):
        for v in self.animals.values():
            print(v.__dict__)

    def has_animal(self, animal_name):
        for v in self.animals.values():
            if v.__dict__['name'] == animal_name:
                print(f'{animal_name} is in the zoo')


if __name__ == '__main__':
    cat1 = Cat.Cat('cat1', 'meat', 'medium', 'dangerous')
    cat2 = Cat.Cat('cat2', 'meat', 'small', 'dangerous')
    dog1 = Dog.Dog('dog1', 'meat', 'medium', 'dangerous')
    zoo1 = Zoo('Zoo1')
    zoo1.add_new_animal_by_id(cat1)
    zoo1.add_new_animal_by_id(cat2)
    zoo1.add_new_animal_by_id(cat1)
    zoo1.has_animal('cat1')
