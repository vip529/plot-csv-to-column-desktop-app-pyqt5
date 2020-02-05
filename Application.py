from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtWidgets import *
import os
import random
import csv
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.view = MyView()

        self.form_widget = MyTable()

        self.setCentralWidget(self.view)
        #col_headers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        #self.form_widget.setHorizontalHeaderLabels(col_headers)

        self.setWindowTitle("Plotter")
        self.setGeometry(150, 70, 1400, 900)
        self.setWindowIcon(QtGui.QIcon("window.jpg"))
        self.menu()
    def menu(self):


        self.bar = self.menuBar()
        file = self.bar.addMenu("File")

        load_action = QAction('&Load csv file', self)
        file.addAction(load_action)

        save_action = QAction('&Save file', self)
        save_action.setShortcut('Ctrl+S')
        file.addAction(save_action)

        file.addAction("Save as png")

        quit_action = QAction('&Quit', self)
        file.addAction(quit_action)
        edit = self.bar.addMenu("Edit")
        edit.addAction("Edit data")

        quit_action.triggered.connect(self.quit_app)
        save_action.triggered.connect(self.form_widget.save_sheet)
        load_action.triggered.connect(self.form_widget.open_sheet)

        self.copyright = QLabel("To plot the graph", self)
        self.copyright.setStyleSheet(" color: black;  background-color: white; font-size: 15px;   ")
        self.copyright.setAlignment(QtCore.Qt.AlignCenter)
        self.statusBar = QtWidgets.QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.addPermanentWidget(self.copyright, 50)
        self.show()

    def quit_app(self):
        qApp.quit()