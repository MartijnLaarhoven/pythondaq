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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QVBoxLayout,
    QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(880, 694)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plot_widget = PlotWidget(self.centralwidget)
        self.plot_widget.setObjectName(u"plot_widget")

        self.verticalLayout.addWidget(self.plot_widget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Starting = QDoubleSpinBox(self.centralwidget)
        self.Starting.setObjectName(u"Starting")
        self.Starting.setMinimum(0.000000000000000)
        self.Starting.setMaximum(3.300000000000000)
        self.Starting.setSingleStep(0.100000000000000)

        self.horizontalLayout_3.addWidget(self.Starting)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.Ending = QDoubleSpinBox(self.centralwidget)
        self.Ending.setObjectName(u"Ending")
        self.Ending.setMinimum(0.000000000000000)
        self.Ending.setMaximum(3.300000000000000)
        self.Ending.setSingleStep(0.100000000000000)

        self.horizontalLayout_3.addWidget(self.Ending)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.Numpoints_Value = QSpinBox(self.centralwidget)
        self.Numpoints_Value.setObjectName(u"Numpoints_Value")
        self.Numpoints_Value.setMinimum(2)
        self.Numpoints_Value.setMaximum(100)
        self.Numpoints_Value.setValue(2)

        self.horizontalLayout_3.addWidget(self.Numpoints_Value)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Startbutton = QPushButton(self.centralwidget)
        self.Startbutton.setObjectName(u"Startbutton")

        self.horizontalLayout.addWidget(self.Startbutton)

        self.select_device = QComboBox(self.centralwidget)
        self.select_device.setObjectName(u"select_device")

        self.horizontalLayout.addWidget(self.select_device)

        self.SaveButton = QPushButton(self.centralwidget)
        self.SaveButton.setObjectName(u"SaveButton")

        self.horizontalLayout.addWidget(self.SaveButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

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
        self.SaveButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

