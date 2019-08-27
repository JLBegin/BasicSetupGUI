from PyQt5 import QtWidgets
from PyQt5.QtCore import QThreadPool
from utils.threadWorker import Worker
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
matplotlib.use('QT5Agg')


class LiveGraph(Canvas):
    def __init__(self):
        self.axes = [None]  # correction only for one plot with subplots
        self.fig, self.axes[0] = plt.subplots(1)

        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        Canvas.updateGeometry(self)

        self.x = []
        self.y = []

        self.running = None
        self.line = None

        self.graphWorker = Worker(self.liveGraphThread)
        self.threadPool = QThreadPool()

        self.initGraph()

    def initGraph(self):
        self.line, = self.axes[0].plot(self.x, self.y, color='b', linestyle='', marker='o', markersize='8')
        self.axes[0].set_ylim(0, 1)
        self.axes[0].set_xlim(0, 10)
        self.draw()

    def start(self):
        self.running = True
        self.threadPool.start(self.graphWorker)

    def liveGraphThread(self, statusSignal=None):  # statusSignal argument required for threaded functions
        """
        Simple random graph
        (Use a Queue object from multiprocessing to handle external data flow inside this thread)
        """
        self.line.set_xdata(np.arange(0, 11))

        while True:
            if self.running:
                self.line.set_ydata(np.random.rand(11))
                self.draw()
                time.sleep(0.1)

    def stop(self):
        self.running = False
