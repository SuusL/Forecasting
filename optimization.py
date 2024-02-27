from math import sqrt
from objects import Line2D
from attributes import Color

class ParabolaLine:

    def __init__(self, scatter, a=1, b=1, c=1, step=0.001, max_h_error=10**-5):
        self.scatter = scatter
        self.__line = Line2D(a, b, c, self.scatter)
        self.step = step
        self.max_h_error = max_h_error

    def adjust(self):
        while True:

            f = [
                self.target_func(self.__line.a - self.step, self.__line.b, self.__line.c),
                self.target_func(self.__line.a, self.__line.b, self.__line.c),
                self.target_func(self.__line.a + self.step, self.__line.b, self.__line.c)
            ]
            h = self.step * (f[0] - f[2]) / (2 * (f[0] - 2 * f[1] + f[2]))
            self.__line.a += h

            f = [
                self.target_func(self.__line.a, self.__line.b - self.step, self.__line.c),
                self.target_func(self.__line.a, self.__line.b, self.__line.c),
                self.target_func(self.__line.a, self.__line.b + self.step, self.__line.c)
            ]
            h = self.step * (f[0] - f[2]) / (2 * (f[0] - 2 * f[1] + f[2]))
            self.__line.b += h

            f = [
                self.target_func(self.__line.a, self.__line.b, self.__line.c - self.step),
                self.target_func(self.__line.a, self.__line.b, self.__line.c),
                self.target_func(self.__line.a, self.__line.b, self.__line.c + self.step)
            ]
            h = self.step * (f[0] - f[2]) / (2 * (f[0] - 2 * f[1] + f[2]))
            self.__line.c += h

            if abs(h) < self.max_h_error:
                break

    def target_func(self, a, b, c) -> float:
        error = 0
        for offset in self.scatter.offsets:
            error += (abs(a * offset.date.days + b*offset.value + c) / sqrt(a**2 + b**2))**2
        return error

    @property
    def line(self):
        color = Color()
        color.rgb = (138, 43, 226)
        self.__line.color = color
        return self.__line




