from attributes import Color


class Offset:

    def __init__(self, date, value):
        self.date = date
        self.value = value

    def __str__(self):
        return f'Offset:\ndate={self.date}\nvalue={self.value}'


class Scatter:

    def __init__(self, lon, lat, avg_velocity, offsets, name='Scatter', color=Color(), size=None, marker=None):
        self.lon = lon
        self.lat = lat
        self.avg_velocity = avg_velocity
        self.offsets = offsets
        self.__reference_date = None
        self.linear_trend = None
        self.bilinear_trend = None
        self.cubic_trend = None
        self.name = name
        self.color = color
        self.size = size
        self.marker = marker

    def __str__(self):
        return f'Scatter:\nlon={self.lon}\nlat={self.lat}\navg_valocity={self.avg_velocity}\noffsets={[[offset.date, offset.value] for offset in self.offsets]}'

    def set_new_date_reference_system(self) -> None:
        if not self.__reference_date:
            self.__reference_date = self.offsets[0].date

    def sort_offsets_by_x(self):
        offsets = sorted(self.offsets, key=lambda x: x.date)
        return offsets

    def get_day_of_offset_from_reference_date(self, offset):
        if self.__reference_date:
            return (offset.date - self.__reference_date).days

    @property
    def reference_date(self):
        return self.__reference_date


class Line2D:

    def __init__(self, a, b, c, scatter, name='Line', color=Color(), marker=None,
                 linestyle=None,
                 linewidth=None):
        self.a = a
        self.b = b
        self.c = c
        self.scatter = scatter
        self.name = name
        self.color = color
        self.marker = marker
        self.linestyle = linestyle
        self.linewidth = linewidth


class BilinearLine2D:

    def __init__(self, a, b, c, scatter, name='Line', color=Color(), marker=None,
                 linestyle=None,
                 linewidth=None):
        self.a = a
        self.b = b
        self.c = c
        self.scatter = scatter
        self.name = name
        self.color = color
        self.marker = marker
        self.linestyle = linestyle
        self.linewidth = linewidth


class CubicLine2D:

    def __init__(self, a, b, c, d, scatter, name='Line', color=Color(), marker=None,
                 linestyle=None,
                 linewidth=None):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.scatter = scatter
        self.name = name
        self.color = color
        self.marker = marker
        self.linestyle = linestyle
        self.linewidth = linewidth
