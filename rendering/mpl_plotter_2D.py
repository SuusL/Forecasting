import matplotlib.pyplot as plt
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

    def plot(self, plot_linear_trend=False, plot_bilinear_trend=False, plot_cubic_trend=False, *objects):

        fig, ax = plt.subplots()
        for object in objects:
            if type(object).__name__ == 'Scatter':
                x = [offset.date for offset in object.offsets]
                y = [offset.value for offset in object.offsets]
                ax.scatter(x, y, label='Смещения', c=object.color.hex, marker=object.marker, s=object.size)
                if plot_linear_trend:
                    x = [object.get_day_of_offset_from_reference_date(offset) for offset in object.offsets]
                    y = [(-object.linear_trend.a * x - object.linear_trend.c) / object.linear_trend.b for x in x]
                    x = [offset.date for offset in object.offsets]
                    ax.plot(x, y, label=f'Прямая: {round(object.linear_trend.a, 1)}x+{round(object.linear_trend.b, 1)}y+{round(object.linear_trend.c, 1)}=0',
                            c=object.linear_trend.color.hex, marker=object.linear_trend.marker, linestyle=object.linear_trend.linestyle,
                            linewidth=object.linear_trend.linewidth)
                if plot_bilinear_trend:
                    x = [object.get_day_of_offset_from_reference_date(offset) for offset in object.offsets]
                    y = [(object.bilinear_trend.a * x**2 + object.bilinear_trend.b * x + object.bilinear_trend.c) for x in x]
                    x = [offset.date for offset in object.offsets]
                    ax.plot(x, y, label=f'Полином 2-ого порядка: y={round(object.bilinear_trend.a, 1)}x^2+{round(object.bilinear_trend.b, 1)}x+{round(object.bilinear_trend.c, 1)}',
                            c=object.bilinear_trend.color.hex, marker=object.bilinear_trend.marker, linestyle=object.bilinear_trend.linestyle,
                            linewidth=object.bilinear_trend.linewidth)
                if plot_cubic_trend:
                    x = [object.get_day_of_offset_from_reference_date(offset) for offset in object.offsets]
                    y = [(object.cubic_trend.a * x**3 + object.cubic_trend.b * x**2 + object.cubic_trend.c * x + object.cubic_trend.d) for x in x]
                    x = [offset.date for offset in object.offsets]
                    ax.plot(x, y, label=f'Полином 3-ого порядка: y={round(object.cubic_trend.a, 4)}x^3+{round(object.cubic_trend.b, 4)}x^2+{round(object.cubic_trend.c, 4)}x + {round(object.cubic_trend.d, 4)}',
                            c=object.cubic_trend.color.hex, marker=object.cubic_trend.marker, linestyle=object.cubic_trend.linestyle,
                            linewidth=object.cubic_trend.linewidth)

            if type(object).__name__ == 'Line2D':
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
