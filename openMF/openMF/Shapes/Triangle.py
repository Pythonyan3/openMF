from openMF.openMF.Shapes.Point import Point


class Triangle:
    def __init__(self, a: Point, b: Point, c: Point):
        self.a = a
        self.b = b
        self.c = c

    def __mul__(self, other):
        a = self.a * other
        b = self.b * other
        c = self.c * other
        return Triangle(a, b, c)

    def __rmul__(self, other):
        a = self.a * other
        b = self.b * other
        c = self.c * other
        return Triangle(a, b, c)

    def sort(self):
        a, b, c = self.a.copy(), self.b.copy(), self.c.copy()
        if a.y > b.y:
            a, b = b, a
        if a.y > c.y:
            a, c = c, a
        if b.y > c.y:
            b, c = c, b
        return Triangle(a, b, c)

    def copy(self):
        return Triangle(self.a.copy(), self.b.copy(), self.c.copy())
