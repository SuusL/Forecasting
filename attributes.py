

class Color():

    def __init__(self, name='Цвет'):
        self.name = name
        self.__rgb = None
        self.__hex = None

    @property
    def rgb(self):
        return self.__rgb

    @property
    def hex(self):
        return self.__hex

    @rgb.setter
    def rgb(self, rgb: tuple):
        self.__rgb = rgb
        self.__hex = "#{:02x}{:02x}{:02x}".format(rgb[0] ,rgb[1] ,rgb[2])

    @hex.setter
    def hex(self, hex: str):
        self.__hex = hex
        hex = self.__hex.lstrip('#')
        self.__rgb = tuple(int(hex[i: i +2], 16) for i in (0, 2, 4))




