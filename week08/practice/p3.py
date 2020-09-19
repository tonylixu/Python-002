class Vector(Point):
    def __init__(self, p1, p2, p3):
        super(Vector).__init__()
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def __sub__(self, other):
        tmp = (self.p1 - other.p1)**2 + (self.p2 - other.p2)**2 + (self.p3 - other.p3)**2
        return sqrt(tmp)