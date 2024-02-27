from parsers import ParserTXT
from optimization import ParabolaLine
from rendering.mpl_plotter_2D import Plot2D


def main():
    parser = ParserTXT('./data.txt', ',')
    parser.parse()
    parser.data[1].set_new_date_reference_system()

    optimizer = ParabolaLine(parser.data[1])
    optimizer.adjust()
    print(optimizer.line.color.rgb)

    plotter = Plot2D(title='Прогнозирование деформаций', legend=True,
                     horizontal_axis='Дата', vertical_axis='Величина смещения')
    plotter.plot(parser.data[1], optimizer.line)


if __name__ == "__main__":
    main()
