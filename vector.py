import math

class Vector():
    x = 0
    y = 0
    normal_x = 0
    normal_y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self) -> float:
        """Сосчитать длину вектора по теореме пифагора"""
        return math.hypot(self.x, self.y)

    def normalise(self):
        """Запусти перед началом рассчета с косинусами"""
        k = 1 / self.length()

        self.normal_x = k * self.x
        self.normal_y = k * self.y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __sub__(self, other):
        self + (-other)

    def __mul__(self, other: float):
        return Vector(self.x * other, self.y * other)

    def __truediv__(self, other: float):
        return self * (1 / other)

    def __str__(self) -> str:
        return f"[{self.x}, {self.y}]"

    def from_angle(angle: float):
        """Создаем вектор из угла в радианах"""
        return Vector(math.cos(angle), math.sin(angle))
