from math import hypot


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # The repr special methid is called by the repr built-in to get the string representation of the object for inspection. If we do not implement __repr__, vector instances would be shown in the console like <Vector object at 0x10e100080
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    # returns the magnitude of the vector
    def __abs__(self):
        return hypot(self.x, self.y)

    # Python accepts any object in a boolean context. This implementation of bool returns False if the magnitude of the vector is zero. Another implementation would be:
    # def __bool_(self):
    #    return bool(self.x or self.y)
    def __bool__(self):
        return bool(abs(self))

    # implements the operator + i.e. using v1 + v2
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return(Vector(x, y))

    # implements the operator * i.e. using v1 * scalar
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


v1 = Vector(1, 4)
v2 = Vector(2, 5)
print(v1)  # Vector(1, 4)
print(v1 + v2)print(v1 * 4)   # Vector(4,16)
print(abs(v2))  # 5.38...
v3 = Vector()   # Vector(0,0)
print(bool(v3))  # False
print(bool(v2))  # True
