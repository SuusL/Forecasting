from math import sqrt
from objects import Line2D, BilinearLine2D, CubicLine2D
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
                self.scatter.linear_trend = self.__line
                break

    def target_func(self, a, b, c) -> float:
        error = 0
        for offset in self.scatter.offsets:
            error += (abs(a * self.scatter.get_day_of_offset_from_reference_date(offset) + b*offset.value + c) / sqrt(a**2 + b**2))**2
        return error

    @property
    def line(self):
        return self.__line


class ParabolaBilinear:

    def __init__(self, scatter, a=10, b=10, c=100, step=0.001, max_h_error=10**-7):
        self.scatter = scatter
        self.__bilinear_line = BilinearLine2D(a, b, c, self.scatter)
        self.step = step
        self.max_h_error = max_h_error

    def adjust(self):
        while True:

            f = [
                self.target_func(self.__bilinear_line.a - self.step, self.__bilinear_line.b, self.__bilinear_line.c),
                self.target_func(self.__bilinear_line.a, self.__bilinear_line.b, self.__bilinear_line.c),
                self.target_func(self.__bilinear_line.a + self.step, self.__bilinear_line.b, self.__bilinear_line.c)
            ]
            h = self.step * (f[0] - f[2]) / (2 * (f[0] - 2 * f[1] + f[2]))
            self.__bilinear_line.a += h

            f = [
                self.target_func(self.__bilinear_line.a, self.__bilinear_line.b - self.step, self.__bilinear_line.c),
                self.target_func(self.__bilinear_line.a, self.__bilinear_line.b, self.__bilinear_line.c),
                self.target_func(self.__bilinear_line.a, self.__bilinear_line.b + self.step, self.__bilinear_line.c)
            ]
            h = self.step * (f[0] - f[2]) / (2 * (f[0] - 2 * f[1] + f[2]))
            self.__bilinear_line.b += h

            f = [
                self.target_func(self.__bilinear_line.a, self.__bilinear_line.b, self.__bilinear_line.c - self.step),
                self.target_func(self.__bilinear_line.a, self.__bilinear_line.b, self.__bilinear_line.c),
                self.target_func(self.__bilinear_line.a, self.__bilinear_line.b, self.__bilinear_line.c + self.step)
            ]
            h = self.step * (f[0] - f[2]) / (2 * (f[0] - 2 * f[1] + f[2]))
            self.__bilinear_line.c += h

            if abs(h) < self.max_h_error:
                self.scatter.bilinear_trend = self.__bilinear_line
                break

    def target_func(self, a, b, c) -> float:
        error = 0
        for offset in self.scatter.offsets:
            x = self.scatter.get_day_of_offset_from_reference_date(offset)
            error += abs((a * x**2 + b * x + c) - offset.value)**2
        return error

    @property
    def bilinear_line(self):
        return self.__bilinear_line


class ParabolaCubic:

    def __init__(self, scatter, a=10, b=10, c=10, d=10, step=0.001, max_h_error=10**-7):
        self.scatter = scatter
        self.__cubic_line = CubicLine2D(a, b, c, d, self.scatter)
        self.step = step
        self.max_h_error = max_h_error

    def adjust(self):
        while True:

            f = [
                self.target_func(self.__cubic_line.a - self.step, self.__cubic_line.b, self.__cubic_line.c, self.__cubic_line.d),
                self.target_func(self.__cubic_line.a, self.__cubic_line.b, self.__cubic_line.c, self.__cubic_line.d),
                self.target_func(self.__cubic_line.a + self.step, self.__cubic_line.b, self.__cubic_line.c, self.__cubic_line.d)
            ]
            h = self.step * (f[0] - f[2]) / (2 * (f[0] - 2 * f[1] + f[2]))
            self.__cubic_line.a += h

            f = [
                self.target_func(self.__cubic_line.a, self.__cubic_line.b - self.step, self.__cubic_line.c, self.__cubic_line.d),
                self.target_func(self.__cubic_line.a, self.__cubic_line.b, self.__cubic_line.c, self.__cubic_line.d),
                self.target_func(self.__cubic_line.a, self.__cubic_line.b + self.step, self.__cubic_line.c, self.__cubic_line.d)
            ]
            h = self.step * (f[0] - f[2]) / (2 * (f[0] - 2 * f[1] + f[2]))
            self.__cubic_line.b += h

            f = [
                self.target_func(self.__cubic_line.a, self.__cubic_line.b, self.__cubic_line.c - self.step, self.__cubic_line.d),
                self.target_func(self.__cubic_line.a, self.__cubic_line.b, self.__cubic_line.c, self.__cubic_line.d),
                self.target_func(self.__cubic_line.a, self.__cubic_line.b, self.__cubic_line.c + self.step, self.__cubic_line.d)
            ]
            h = self.step * (f[0] - f[2]) / (2 * (f[0] - 2 * f[1] + f[2]))
            self.__cubic_line.c += h

            f = [
                self.target_func(self.__cubic_line.a, self.__cubic_line.b, self.__cubic_line.c, self.__cubic_line.d - self.step),
                self.target_func(self.__cubic_line.a, self.__cubic_line.b, self.__cubic_line.c, self.__cubic_line.d),
                self.target_func(self.__cubic_line.a, self.__cubic_line.b, self.__cubic_line.c, self.__cubic_line.d + self.step)
            ]
            h = self.step * (f[0] - f[2]) / (2 * (f[0] - 2 * f[1] + f[2]))
            self.__cubic_line.d += h

            if abs(h) < self.max_h_error:
                self.scatter.cubic_trend = self.__cubic_line
                break

    def target_func(self, a, b, c, d) -> float:
        error = 0
        for offset in self.scatter.offsets:
            x = self.scatter.get_day_of_offset_from_reference_date(offset)
            error += abs((a * x**3 + b * x**2 + c * x + d) - offset.value)**2
        return error

    @property
    def cubic_line(self):
        return self.__cubic_line
