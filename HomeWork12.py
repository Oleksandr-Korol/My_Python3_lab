class Vector2D(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x,
                        self.y + other.y)

    def __mul__(self, scalar):
        if type(scalar) is int or type(scalar) is float:
            return Vector2D(self.x * scalar,
                            self.y * scalar)
        if type(scalar) == type(self):
            return self.x * scalar.x + self.y * scalar.y

    def modul(self):
        return (self.x ** 2 + self, y ** 2) ** 0.5

    def __eq__(self, other):
        self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x},{self.y})"

    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
    def __setitem__(self, key, value):
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value

class Vector3d(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __add__(self, other):
        return Vector3d(self.x + other.x,
                        self.y + other.y,
                        self.z + other.z)

    def __mul__(self, scalar):
        if type(scalar) is int or type(scalar) is float:
            return Vector3d(self.x * scalar,
                            self.y * scalar,
                            self.z * scalar)
        if type(scalar) == type(self):
            return self.x * scalar.x + self.y * scalar.y + self.z * scalar

    def modul(self):
        return (self.x ** 2 + self.y ** 2 + self.z** 2) ** 0.5

    def __eq__(self, other):
        self.x == other.x and self.y == other.y and self.z == other.z

    def __str__(self):
        return f"({self.x},{self.y},{self.z})"

firs = Vector3d(2, 3, 2)

print(firs)










