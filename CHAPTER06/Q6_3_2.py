class Rectangle:
    angle = 90

    def __init__(self, width, height):
        self.name = "rectangle"
        self.width = width
        self.height = height
        self.perimater = self.calc_perimater()
        self.area = self.calc_area()

    def calc_perimater(self):
        w = self.width
        h = self.height
        return (w * h) * 2

    def calc_area(self):
        w = self.width
        h = self.height
        return w * h

    def show_attributes(self):
        ang = self.angle
        n = self.name
        w = self.width
        h = self.height
        p = self.perimater
        a = self.area
        print(f"name: {n}, width: {w}, height: {h}, angle: {ang}")
        print(f"perimater: {p}, area: {a}")


class Square(Rectangle):
    def __init__(self, width):
        super().__init__(width, width)
        self.name = "square"


a = Square(5)
print(a.show_attributes())
