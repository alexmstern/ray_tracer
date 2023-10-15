from math import sqrt

class Vec3:

    def __init__(self, e0, e1, e2):
        self.e = (e0, e1, e2)
    
    def x(self):
        return self.e[0]
    
    def y(self):
        return self.e[1]
    
    def z(self):
        return self.e[2]
    
    def length(self):
        return sqrt(self.lengthsquared)

    def lengthsquared(self):
        return (self.e[0]*self.e[0] + self.e[1]*self.e[1] + self.e[2]*self.e[2])
    
    def normalize(self):
        return self / self.length
    
    def __neg__(self):
        return Vec3(-self.e[0], -self.e[1], -self.e[2])
    
    def __add__(self, other):
        return Vec3(self.e[0] + other.e[0], self.e[1] + other.e[1], self.e[2] + other.e[2])

    def __iadd__(self, other):
        self.__init__(self + other)
        return self
    
    def __sub__(self, other):
        return Vec3(self.e[0] - other.e[0], self.e[1] - other.e[1], self.e[2] - other.e[2])
    
    def __isub__(self, other):
        self.__init__(self - other)
        return self
    
    def __mul__(self, other):
        if isinstance(other, Vec3):
            return Vec3(self.e[0] * other.e[0], self.e[1] * other.e[1], self.e[2] * other.e[2])
        else:
            return Vec3(self.e[0] * other, self.e[1] * other, self.e[2] * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        self.__init__(self * other)
        return self

    def __truediv__(self, other):
        if isinstance(other, Vec3):
            return Vec3(self.e[0] / other.e[0], self.e[1] / other.e[1], self.e[2] / other.e[2])
        else:
            return Vec3(self.e[0] / other, self.e[1] / other, self.e[2] / other)
    
    def __idiv__(self, other):
        self.__init__(self / other)
        return self

Point3 = Vec3