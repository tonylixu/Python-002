class Kls1(object):
    bar = 1
    def foo(self):
        print('In foo')
    @classmethod
    def class_foo(cls):
        print(cls.bar)
        print(cls.__name__)
        cls().foo()

#Kls1.class_foo()

class Story():
    snake = 'Python'
    def __init__(self, name):
        self.name = name

    @classmethod
    def get_apple_to_eva(cls):
        return cls.snake

s = Story('anyone')
print(s.__init__)
print(s.get_apple_to_eva)
print(s.get_apple_to_eva())
print(Story.get_apple_to_eva())