from turtle import color

from PyQt6.QtCharts import QLineSeries, QChart, QChartView, QSplineSeries, QValueAxis, QAbstractAxis, QDateTimeAxis
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QBrush, QColor, QPen


# Package: PyQt6-Charts
# https://github.com/chey00/qchart
class WeltChart(QChartView):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.background_image = QPixmap("Europe_1871_map_de.png")
        self.background_image = self.background_image.scaled(1200, 600)

        self.series = QLineSeries()
        self.series.setName("WeltChart")


        pen = QPen(QColor(144, 238, 144))
        pen.setWidth(5)

        self.series.setPen(pen)

        self.chart = QChart()
        self.chart.setTitle("Karte")
        self.chart.addSeries(self.series)

        axis_y = QValueAxis()
        axis_y.setRange(0, 10)
        axis_x = QValueAxis()
        axis_x.setRange(0, 10)

        self.chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        self.chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)

        self.chart.setBackgroundVisible(True)
        self.chart.setBackgroundBrush(QBrush(self.background_image))

        self.setChart(self.chart)

    def mouseReleaseEvent(self, event) -> None:
        my_point = self.chart.mapToValue(event.pos().toPointF(), self.series)
        self.series.append(my_point)
