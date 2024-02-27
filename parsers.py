from objects import Offset, Scatter
from datetime import datetime as dt
from attributes import Color


class ParserTXT:

    def __init__(self, path, sep):
        self.path = path
        self.sep = sep
        self.data = None

    def parse(self):
        self.data = []
        row_number = 0
        with open(f'{self.path}', 'r') as file:
            for row in file:

                if row_number == 0:
                    self.data.append(row.split(','))

                else:
                    split_row = row.split(',')
                    lon = float(split_row[0].replace('Point (', '').split(' ')[0])
                    lat = float(split_row[0].replace(')', '').split(' ')[2])
                    avg_velocity = float(split_row[4])
                    offsets = []
                    for i in range(8, len(split_row)):
                        date = self.data[0][i].replace('D', '').replace('\n', '')
                        date = dt.strptime(f'{date[0:4]}-{date[4:6]}-{date[6:8]}', '%Y-%m-%d')
                        value = float(split_row[i])
                        offset = Offset(date, value)
                        offsets.append(offset)
                    color = Color()
                    color.rgb = (255, 0, 0)
                    scatter = Scatter(lon, lat, avg_velocity, offsets, color=color, marker='X')
                    self.data.append(scatter)
                row_number += 1
