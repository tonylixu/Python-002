class Human(object):
    live = True

    def __init__(self, name):
        self.name = name

    def test(self):
        print('Test')


class MyfirstClass():
    pass


class NewList(list):
    __fly = False

if __name__ == '__main__':
    import inspect
    man = Human('Adam')
    woman = Human('Eva')
    Human.newattr = 1
    #print(Human.__dict__)
    print(Human.__dict__)
    man.test()
    print(man.__dict__)
    #print(man.__class__.__bases__[0].__subclasses__())
    man.live = False

    # l = NewList([1, 2, 3, 4])
    # setattr(NewList, 'newattr', 'test')
    # print(l.newattr)
    # l.newattr = 2
    # print(l.__dict__)
    # print(NewList.__dict__)
