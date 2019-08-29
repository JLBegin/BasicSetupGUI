from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUiType
import os

mainWindowPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'ui', 'mainWindow.ui')
Ui_MainWindow, QtBaseClass = loadUiType(mainWindowPath)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.liveGraph = self.mainPlot.canvas
        self.pushButton.setText("Start")
        self.pushButton.clicked.connect(self.startGraph)

    def startGraph(self):
        self.liveGraph.start()

        self.pushButton.clicked.disconnect()
        self.pushButton.setText("Stop")
        self.pushButton.clicked.connect(self.stopGraph)

    def stopGraph(self):
        self.liveGraph.stop()
        self.pushButton.setText("Start")
        self.pushButton.clicked.connect(self.startGraph)
