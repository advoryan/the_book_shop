import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def p_def(self):
        return self.x, self.y

p1 = Point(1, 2)
p2 = Point(4, 5)

class Line:
    def __init__(self, name, obj1, obj2):
        self.name, self.x1, self.y1, self.x2, self.y2 = name, obj1.x, obj1.y, obj2.x, obj2.y
    def length(self):
        l = (((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2)) ** (1/2)
        self.l = l
        return l
    def angle(self):
        a = math.degrees(math.asin((self.y2 - self.y1) / self.l))
        return a
    def shift(self, x_sh, y_sh):
        self.x_sh = x_sh
        self.y_sh = y_sh
        self.x1 += x_sh
        self.x2 += x_sh
        self.y1 += y_sh
        self.y2 += y_sh
        return self.name, self.x1, self.y1, self.x2, self.y2
    def __repr__(self):
        return "{}- Координаты 1й точки: ({}, {}). Координаты 2й точки: ({}, {})".format(self.name,self.x1, self.y1, self.x2, self.y2)
    def __str__(self):
        return "{}- Координаты 1й точки: ({}, {}). Координаты 2й точки: ({}, {})".format(self.name,self.x1, self.y1, self.x2, self.y2)

mod = Line("Первая линия", p1, p2)

print("Длинна {} {} см, его наклон по оси х = {} градусов".format(mod.name, round(mod.length(),2), round(mod.angle(),1)))
print(mod)

a_shifted = mod.shift(5, 5)
print(a_shifted)

aaa = a_shifted.length()