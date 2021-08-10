# !/usr/bin/env python
# encoding: utf-8


"""
  @author: gaogao
  @file: demo.py
  @time: 2021/8/9 9:53
  @desc:
"""
import sys
from PySide6.QtGui import QIcon, QPainter, QColor, QPen,QBrush
from PySide6.QtCore import QCoreApplication, QRect, QSize, Qt, QRectF
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGraphicsScene, QGraphicsView,QGridLayout


class Map(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def setColumnSize(self, columnSize):
        self.columns = columnSize

    def setRowsSize(self, rowSize):
        self.rows = rowSize

    def initUI(self):
        self.setMinimumSize(500, 500)  # min-size of the widget
        self.columns = 14  # num of columns in grid
        self.rows = 49  # num of rows in grid

        grid = QGridLayout(self)
        self.view = QGraphicsView()
        grid.addWidget(self.view)
        self.view.setRenderHints(QPainter.Antialiasing)

        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

        brush = QBrush(QColor(QColor(255, 255, 255)))  # background color of square
        pen = QPen(Qt.black)  # border color of square
        side = 10
        rect = QRectF(0, 0, side, side)
        for i in range(self.rows):
            for j in range(self.columns):
                self.scene.addRect(rect.translated(i * side, j * side), pen, brush)
        # this is required to ensure that fitInView works on first shown too
        self.resizeScene()

    def resizeScene(self):
        self.view.fitInView(self.scene.sceneRect())

    def resizeEvent(self, event):
        # call fitInView each time the widget is resized
        self.resizeScene()

    def showEvent(self, event):
        # call fitInView each time the widget is shown
        self.resizeScene()

    def paintEvent(self, event):
        grid = QGridLayout()
        self.sceneWithPen(grid)
        self.setLayout(grid)
        # creates the grid of squares

    def sceneWithPen(self, grid):
        scene = QGraphicsScene()
        w = QGraphicsView()
        w.setScene(scene)
        side = self.squareSize
        brush = QBrush(QColor(qRgb(255, 255, 255)))  # background color of square
        pen = QPen(Qt.black)  # border color of square
        for i in range(self.rows):
            for j in range(self.columns):
                r = QRectF(QPointF(
                    i * side, j * side), QSizeF(side, side))  # each square
                scene.addRect(r, pen, brush)
        grid.addWidget(w)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = Map()
    view.show()
    sys.exit(app.exec())
