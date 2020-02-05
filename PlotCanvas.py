from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import random
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtWidgets import *

class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        #self.plot()


    def plot(self):
        #data = [random.random() for i in range(25)]
        x = [1,2,3,4,5]
        y = [1,2,3,4,5]
        ax = self.figure.add_subplot(111,)
        ax.scatter(x,y)

        ax.set_title()
        self.draw()
    def plot_scatter(self):
        x = [1, 2, 3, 4, 5]
        y = [1, 2, 8, 4, 5]
        ax = self.figure.add_subplot(111)
        ax.scatter(x, y)
        ax.set_xlabel('dfgh')
        ax.set_ylabel('gghhj')
        ax.set_title('Scattered Plot')

        self.draw()

    def plot_line(self):
        self.tab2 = QWidget()
        self.tabs.addTab(self.tab2, "Tab 2")
        self.tabs.setCurrentWidget(self.tab2)
        self.m = PlotCanvas(self, width=4, height=4)

        self.tab2.layout = QVBoxLayout(self)
        self.tab2.layout.addWidget(self.m)
        self.tab2.setLayout(self.tab2.layout)

    def plot_smoothline(self):
        self.tab3 = QWidget()
        self.tabs.addTab(self.tab3, "Tab 3")
        self.tabs.setCurrentWidget(self.tab3)
        self.m = PlotCanvas(self, width=4, height=4)


        self.tab3.layout = QVBoxLayout(self)
        self.tab3.layout.addWidget(self.m)