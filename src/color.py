import sys
from vec3 import Vec3

class Color(Vec3):
    pass

def write_color(self, output=sys.stdout):
    ir = int(255.999 * self.e[0])
    ig = int(255.999 * self.e[1])
    ib = int(255.999 * self.e[2])
    print(f"{ir} {ig} {ib}", file=output)

Color.write_color = write_color
