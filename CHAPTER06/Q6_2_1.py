class cylinder:
    pi = 3.14

    def __init__(self, radius=1, height=1):
        self.radius = radius
        self.height = height

    def calc_base_area(self):
        pi = cylinder.pi
        r = self.radius
        return pi * r * r

    def calc_side_area(self):
        pi = cylinder.pi
        r = self.radius
        h = self.height
        return 2 * pi * r * h

    def calc_surface_area(self):
        c = self.calc_base_area()
        s = self.calc_side_area()
        return 2 * c + s

    def calc_volume(self):
        c = self.calc_base_area()
        h = self.height
        return c * h

    def show_results(self):
        r = self.radius
        h = self.height
        s = self.calc_surface_area()
        v = self.calc_volume()
        print(f"半径: {r}, 高さ: {h}, 表面積 {s}, 体積: {v}")


a = cylinder(15.0, 11.0)
print(a.show_results())
