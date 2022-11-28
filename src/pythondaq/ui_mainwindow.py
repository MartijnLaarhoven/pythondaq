# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(880, 694)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.plot_widget = PlotWidget(self.centralwidget)
        self.plot_widget.setObjectName(u"plot_widget")
        self.plot_widget.setGeometry(QRect(30, 50, 781, 421))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 470, 779, 89))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Starting = QDoubleSpinBox(self.widget)
        self.Starting.setObjectName(u"Starting")
        self.Starting.setMinimum(0.000000000000000)
        self.Starting.setMaximum(3.300000000000000)
        self.Starting.setSingleStep(0.100000000000000)

        self.horizontalLayout_3.addWidget(self.Starting)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.Ending = QDoubleSpinBox(self.widget)
        self.Ending.setObjectName(u"Ending")
        self.Ending.setMinimum(0.000000000000000)
        self.Ending.setMaximum(3.300000000000000)
        self.Ending.setSingleStep(0.100000000000000)

        self.horizontalLayout_3.addWidget(self.Ending)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.Numpoints_Value = QSpinBox(self.widget)
        self.Numpoints_Value.setObjectName(u"Numpoints_Value")
        self.Numpoints_Value.setMinimum(2)
        self.Numpoints_Value.setMaximum(100)
        self.Numpoints_Value.setValue(2)

        self.horizontalLayout_3.addWidget(self.Numpoints_Value)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.Startbutton = QPushButton(self.centralwidget)
        self.Startbutton.setObjectName(u"Startbutton")
        self.Startbutton.setGeometry(QRect(34, 553, 781, 91))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 880, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Statvalue", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Endlabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Repeats", None))
        self.Startbutton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
    # retranslateUi

