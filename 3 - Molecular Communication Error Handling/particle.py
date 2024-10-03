class Particle:
    x: float
    y: float
    z: float
    type: bool
    is_absorbed: bool = False

    def __init__(self, x, y, z, type):
        self.x = x
        self.y = y
        self.z = z
        self.type = type

    def move(self, dx, dy, dz):
        self.x += dx
        self.y += dy
        self.z += dz

    def absorb(self):
        self.is_absorbed = True
