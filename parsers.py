from objects import Offset, Scatter


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
                        date = float(self.data[0][i].replace('D', '').replace('\n', ''))
                        value = float(split_row[i])
                        offset = Offset(date, value)
                        offsets.append(offset)
                    scatter = Scatter(lon, lat, avg_velocity, offsets)
                    self.data.append(scatter)
                row_number += 1
