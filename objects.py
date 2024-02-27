

class Offset:

    def __init__(self, date, value):
        self.date = date
        self.value = value

    def __str__(self):
        return f'Offset:\ndate={self.date}\nvalue={self.value}'


class Scatter:

    def __init__(self, lon, lat, avg_velocity, offsets):
        self.lon = lon
        self.lat = lat
        self.avg_velocity = avg_velocity
        self.offsets = offsets

    def __str__(self):
        return f'Scatter:\nlon={self.lat}\nlon={self.lon}\navg_valocity={self.avg_velocity}\noffsets={[[offset.date, offset.value] for offset in self.offsets]}'
