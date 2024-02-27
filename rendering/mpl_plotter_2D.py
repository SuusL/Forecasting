import matplotlib.pyplot as plt
from utils import get_date_from_date_and_timedelta, convert_days_to_timedelta
from datetime import datetime


class Plot2D:

    def __init__(self, title='Название', equal_aspect=True, horizontal_axis='x', vertical_axis='y', figsize=(12, 6),
                 legend=False):
        self.title = title
        self.equal_aspect = equal_aspect
        self.horizontal_axis = horizontal_axis
        self.vertical_axis = vertical_axis
        self.figsize = figsize
        self.legend = legend

    def plot(self, *objects):
        fig, ax = plt.subplots()
        min_x, max_x = datetime(2030, 1, 1), datetime(1970, 1, 1)
        for object in objects:
            if type(object).__name__ == 'Scatter':
                x = [get_date_from_date_and_timedelta(object.reference_date, offset.date) for offset in object.offsets]
                y = [offset.value for offset in object.offsets]

                sorted_by_x = object.sort_offsets_by_x()
                if get_date_from_date_and_timedelta(object.reference_date, sorted_by_x[0].date) < min_x:
                    min_x = get_date_from_date_and_timedelta(object.reference_date, sorted_by_x[0].date)
                if get_date_from_date_and_timedelta(object.reference_date, sorted_by_x[-1].date) > max_x:
                    max_x = get_date_from_date_and_timedelta(object.reference_date, sorted_by_x[0].date)

                ax.scatter(x, y, label='Смещения', c=object.color.hex, marker=object.marker, s=object.size)

            if type(object).__name__ == 'Line2D':
                print(not min_x == datetime(2030, 1, 1))
                if not (min_x == datetime(2030, 1, 1) and max_x == datetime(1970, 1, 1)):
                    offsets = object.scatter.sort_offsets_by_x()
                    x = [x for x in range(offsets[0].date.days, offsets[-1].date.days+50, offsets[-1].date.days-1)]
                    y = [(-object.a * x - object.c) / object.b for x in x]
                    x = [get_date_from_date_and_timedelta(object.scatter.reference_date, convert_days_to_timedelta(x)) for
                         x in x]
                else:
                    x = [x for x in range(0, 11, 10)]
                    y = [(-object.a * x - object.c) / object.b for x in x]
                ax.plot(x, y, label=f'Прямая: {round(object.a,1)}x+{round(object.b,1)}y+{round(object.c,1)}=0',
                            c=object.color.hex, marker=object.marker,linestyle=object.linestyle,
                            linewidth=object.linewidth)
        if self.legend:
            ax.legend()
        if self.equal_aspect:
            ax.set_aspect(1)
        plt.xticks(rotation=25)
        ax.set_title(self.title)
        ax.set_xlabel(self.horizontal_axis)
        ax.set_ylabel(self.vertical_axis)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.show()
