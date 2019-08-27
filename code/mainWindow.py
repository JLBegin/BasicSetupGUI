from PyQt5.QtWidgets import QMainWindow
from ui.mainWindowUi import Ui_MainWindow


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
