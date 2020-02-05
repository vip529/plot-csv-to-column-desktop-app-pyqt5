from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtWidgets import *
import os
import csv

class MyTable(QTableWidget):

    def __init__(self):
        super().__init__()
        self.check_change = True
        self.init_ui()

    def init_ui(self):
        self.cellChanged.connect(self.c_current)
        self.show()

    def c_current(self):
        if self.check_change:
            row = self.currentRow()
            col = self.currentColumn()
            value = self.item(row, col)
            value = value.text()
            print("The current cell is ", row, ", ", col)
            print("In this cell we have: ", value)





    def open_sheet(self):
        self.check_change = False
        path = QFileDialog.getOpenFileName(self, 'Open CSV', os.getenv('HOME'), 'CSV(*.csv)')
        if path[0] != '':
            with open(path[0], newline='') as csv_file:
                self.setRowCount(0)
                self.setColumnCount(10)
                my_file = csv.reader(csv_file, dialect='excel')
                for row_data in my_file:
                    row = self.rowCount()
                    self.insertRow(row)
                    if len(row_data) > 10:
                        self.setColumnCount(len(row_data))
                    for column, stuff in enumerate(row_data):
                        item = QTableWidgetItem(stuff)
                        self.setItem(row, column, item)
        self.check_change = True
    def tabdata(self):

        indexes = []
        for selectionRange in self.selectedRanges():
            indexes.extend(range(selectionRange.topRow(), selectionRange.bottomRow() + 1))
            print
            "indexes", indexes  # indexes is a list like [0, 2] of selected rows

        for i in indexes:
            print
            "specific item", self.item(i, 1).text()
            results.append(str(self.item(i, 1).text()))

        # selectedItems()
        for item in self.selectedItems():
            print
            "selectedItems", item.text()

        # selectedIndexes()
        for item in self.selectedIndexes():
            print
            "selectedIndexes", item.row(), item.column()

    def save_sheet(self):
        path = QFileDialog.getSaveFileName(self, 'Save CSV', os.getenv('HOME'), 'CSV(*.csv)')
        if path[0] != '':
            with open(path[0], 'w') as csv_file:
                writer = csv.writer(csv_file, dialect='excel')
                for row in range(self.rowCount()):
                    row_data = []
                    for column in range(self.columnCount()):
                        item = self.item(row, column)
                        if item is not None:
                            row_data.append(item.text())
                        else:
                            row_data.append('')
                    writer.writerow(row_data)
