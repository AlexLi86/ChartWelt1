import random

from PyQt6.QtCore import QTimer, pyqtSlot, pyqtSignal
from PyQt6.QtWidgets import QWidget, QSlider, QHBoxLayout, QGridLayout, QLabel

from WeltChart import WeltChart


class CentralWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.weltchart = WeltChart(parent)

        layout = QHBoxLayout()

        layout.addWidget(self.weltchart)

        self.setLayout(layout)

