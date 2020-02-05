from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtWidgets import *
import os
import csv
from PlotCanvas import *
from MyTable import  *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.form_widget = MyTable()
        self.form_widget.tabdata()



















        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.closetab)

        self.tabs.addTab(self.form_widget,"csv")
        self.main = QWidget(self)
        self.setCentralWidget(self.main)
        self.hbox = QHBoxLayout()
        self.pl_scatter = QPushButton("Plot Scatter Points")
        self.pl_sc_smlin = QPushButton("Plot Scatter Points as Smooth Line")
        self.pl_line = QPushButton("Plot lines")

        self.pl_scatter.clicked.connect(self.plot_scatter)
        self.pl_line.clicked.connect(self.plot_line)
        self.pl_sc_smlin.clicked.connect(self.plot_smoothline)

        self.hbox.addWidget(self.pl_scatter)
        self.hbox.addWidget(self.pl_sc_smlin)
        self.hbox.addWidget(self.pl_line)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.hbox)
        #self.vbox.addWidget(self.form_widget)
        self.vbox.addWidget(self.tabs)
        self.main.setLayout(self.vbox)

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

        save_png = QAction('&Save as png', self)
        save_png.setShortcut('Ctrl+P')
        file.addAction(save_png)

        quit_action = QAction('&Quit', self)
        file.addAction(quit_action)
        edit = self.bar.addMenu("Edit")
        edit.addAction("Edit data")

        quit_action.triggered.connect(self.quit_app)
        save_action.triggered.connect(self.form_widget.save_sheet)
        load_action.triggered.connect(self.form_widget.open_sheet)
        save_png.triggered.connect(self.save_png)

        self.copyright = QLabel("To plot the graph", self)
        self.copyright.setStyleSheet(" color: black;  background-color: white; font-size: 15px;   ")
        self.copyright.setAlignment(QtCore.Qt.AlignCenter)
        self.statusBar = QtWidgets.QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.addPermanentWidget(self.copyright, 50)
        self.show()

    def quit_app(self):
        qApp.quit()

    def plot_scatter(self):
        self.tab1 = QWidget()
        self.tabs.addTab(self.tab1, "Tab 1")

        self.tabs.setCurrentWidget(self.tab1)
        self.m = PlotCanvas(self, width=4, height=4)
        self.m.plot_scatter()
        self.tab1.layout = QVBoxLayout(self)
        self.tab1.layout.addWidget(self.m)
        self.tab1.setLayout(self.tab1.layout)
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
        self.tab3.setLayout(self.tab3.layout)

    def save_png(self):
        pass

    @QtCore.pyqtSlot(int)
    def closetab(self,index):
        widget = self.tabs.widget(index)
        if widget:

            widget.deleteLater()

        self.tabs.removeTab(index)




if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    sales = MainWindow()
    sales.show()
    sys.exit(app.exec_())