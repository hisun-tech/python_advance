# !/usr/bin/env python
# encoding: utf-8


"""
  @author: gaogao
  @file: mymain.py
  @time: 2021/8/12 16:53
  @desc:
"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QSizeGrip
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve

import sys
import os
from interface import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        # 设置窗口的透明属性，在使用动画的时候，出现UpdateLayeredWindowIndirect failed 的错误
        # self.setAttribute(Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 550))
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        self.setWindowIcon(QtGui.QIcon("icons/github.svg"))
        self.setWindowTitle("MODERN UI")

        QSizeGrip(self.ui.size_grip)

        self.bind_event()

        def moveWindow(e):
            if not self.isMaximized():
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        self.ui.header.mouseMoveEvent = moveWindow

        self.show()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def bind_event(self):
        self.ui.minimize_window_button.clicked.connect(lambda: self.showMinimized())
        self.ui.close_window_button.clicked.connect(lambda: self.close())
        self.ui.exit_window_button.clicked.connect(lambda: self.close())
        self.ui.restore_window_button.clicked.connect(lambda: self.restore_or_maximize_window())
        self.ui.open_close_side_bar_btn.clicked.connect(lambda: self.slideLeftMenu())

    def slideLeftMenu(self):
        width = self.ui.slide_menu_container.width()
        print("width0", width)
        if width == 0:
            new_width = 200
            self.ui.open_close_side_bar_btn.setIcon(QIcon("icons/chevron-left.svg"))
        else:
            new_width = 0
            self.ui.open_close_side_bar_btn.setIcon(QIcon("icons/align-left.svg"))
        print("new_width", new_width)
        self.animation = QPropertyAnimation(self.ui.slide_menu_container, b"maximumWidth")
        self.animation.setDuration(200)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.restore_window_button.setIcon(QtGui.QIcon("icons/maximize-2.svg"))
        else:
            self.showMaximized()
            self.ui.restore_window_button.setIcon(QtGui.QIcon("icons/minimize-2.svg"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    app.exec_()
