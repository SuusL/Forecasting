from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtWidgets import QStyleFactory, QFileDialog
import sys
# QtCore.qInstallMessageHandler(lambda *args: None)

from parsers import ParserTXT
from optimization import ParabolaLine, ParabolaBilinear, ParabolaCubic
from rendering.mpl_plotter_2D import Plot2D
from datetime import datetime


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        # self.setWindowIcon(QtGui.QIcon('./icon.png'))
        QtWidgets.QApplication.setStyle(QStyleFactory.create('Fusion'))
        uic.loadUi('./Interface.ui', self)
        self.show()

class Interface():

    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = Ui()
        self.parser = None
        self.linear_optimizer = None
        self.bilinear_optimizer = None
        self.cubic_optimizer = None
        self.plotter = Plot2D(title='Линия тренда', legend=True,
                              horizontal_axis='Дата', vertical_axis='Величина смещения')
        self.connect_widgets()
        sys.exit(self.app.exec_())

    def connect_widgets(self):
        self.window.pushButton_5.clicked.connect(lambda: self.select_file())
        self.window.pushButton.clicked.connect(lambda: self.import_data())
        self.window.pushButton_2.clicked.connect(lambda: self.create_trends())
        self.window.pushButton_3.clicked.connect(lambda: self.plot_trends())
        self.window.pushButton_4.clicked.connect(lambda: self.forecasting())

    def select_file(self):
        options = QtWidgets.QFileDialog.Options()
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Выберите файл", "", "Text Document Files (*.txt);;All Files (*)", options=options)
        if file_name:
            self.window.lineEdit.setText(file_name)

    def import_data(self):
        self.parser = ParserTXT(f'{self.window.lineEdit.text()}', f'{self.window.lineEdit_2.text()}')
        self.parser.parse()
        for i in range(1, len(self.parser.data)):
            self.parser.data[i].set_new_date_reference_system()
        self.set_scatter_to_comboboxes()


    def set_scatter_to_comboboxes(self):
        scatter = [f'Point({scatter.lon},{scatter.lat})' for scatter in self.parser.data[1:]]
        self.window.comboBox.addItems(scatter)

    def create_trends(self):

        self.linear_optimizer = ParabolaLine(self.parser.data[int(self.window.comboBox.currentIndex())+1])
        self.linear_optimizer.adjust()
        self.bilinear_optimizer = ParabolaBilinear(self.parser.data[int(self.window.comboBox.currentIndex())+1])
        self.bilinear_optimizer.adjust()
        self.cubic_optimizer = ParabolaCubic(self.parser.data[int(self.window.comboBox.currentIndex())+1])
        self.cubic_optimizer.adjust()

    def plot_trends(self):

        self.plotter.plot(self.window.checkBox.isChecked(), self.window.checkBox_2.isChecked(),
                          self.window.checkBox_3.isChecked(),
                          self.parser.data[int(self.window.comboBox.currentIndex())+1])

    def forecasting(self):
        if self.window.radioButton.isChecked():
            line, scatter = self.linear_optimizer.line, self.linear_optimizer.scatter
            days = (datetime.strptime(self.window.lineEdit_3.text(), '%d.%m.%Y') - scatter.reference_date).days
            value = (-line.a * days - line.c) / line.b
            self.window.lineEdit_4.setText(f'{round(value, 3)}')

        if self.window.radioButton_2.isChecked():
            bilinear_line, scatter = self.bilinear_optimizer.bilinear_line, self.bilinear_optimizer.scatter
            days = (datetime.strptime(self.window.lineEdit_3.text(), '%d.%m.%Y') - scatter.reference_date).days
            value = (bilinear_line.a * days**2 + bilinear_line.b * days + bilinear_line.c)
            self.window.lineEdit_4.setText(f'{round(value, 3)}')

        if self.window.radioButton_3.isChecked():
            cubic_line, scatter = self.cubic_optimizer.cubic_line, self.cubic_optimizer.scatter
            days = (datetime.strptime(self.window.lineEdit_3.text(), '%d.%m.%Y') - scatter.reference_date).days
            value = (cubic_line.a * days**3 + cubic_line.b * days**2 + cubic_line.c * days + cubic_line.d)
            self.window.lineEdit_4.setText(f'{round(value, 3)}')


if __name__ == "__main__":
    interface = Interface()
