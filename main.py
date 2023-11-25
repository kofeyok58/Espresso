import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableWidgetItem
from PyQt5 import uic


class Coffee(QMainWindow):
    def __init__(self):
        super(Coffee, self).__init__()
        uic.loadUi('main.ui', self)

        self.conn = sqlite3.connect("coffee.sqlite")
        self.cur = self.conn.cursor()

        self.setWindowTitle("Coffee")
        self.cur.execute("SELECT * FROM espresso")
        rows = self.cur.fetchall()

        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setColumnCount(len(rows[0]))
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        # self.tableWidget.setWordWrap(True)
        self.tableWidget.setVerticalHeaderLabels([])
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах',
                                                    'описание вкуса', 'цена', 'объем упаковки'])

        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(col)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Coffee()
    wnd.show()
    sys.exit(app.exec())
