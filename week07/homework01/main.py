# -*- coding: utf-8 -*-
import Cat
import Dog
import Zoo

if __name__ == '__main__':
    cat1 = Cat.Cat('cat1', 'meat', 'medium', 'dangerous')
    cat2 = Cat.Cat('cat2', 'meat', 'small', 'dangerous')
    dog1 = Dog.Dog('dog1', 'meat', 'medium', 'dangerous')
    zoo1 = Zoo.Zoo('Zoo1')
    try:
       zoo1.add_new_animal_by_id(cat1)
    except ValueError as e:
       print(f'[Error]: {e}')
    try:
        zoo1.add_new_animal_by_id(cat2)
    except ValueError as e:
        print(f'[Error]: {e}')
    try:
        zoo1.add_new_animal_by_id(cat1)
    except ValueError as e:
        print(f'[Error]: {e}')
    zoo1.has_animal('cat1')
