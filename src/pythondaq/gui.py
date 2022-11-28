import sys
from PySide6 import QtWidgets
import pyqtgraph as pg
from PySide6.QtCore import Slot
import numpy as np
from pythondaq.ui_mainwindow import Ui_MainWindow

class UserInterface(QtWidgets.QMainWindow):
    pass

# PyQtGraph global options
pg.setConfigOption("background", "w")
pg.setConfigOption("foreground", "k")


class UserInterface(QtWidgets.QMainWindow):

    def __init__(self):
        """The init module
        """        
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.Starting.valueChanged.connect(self.plot)
        # self.ui.Ending.valueChanged.connect(self.plot)
        # self.ui.Numpoints_Value.valueChanged.connect(self.plot)
        self.plot()

    @Slot()
    def plot(self):
        """The plot module
        """        
        self.ui.plot_widget.clear()
        x = np.linspace(0, 3.3,100)
        self.ui.plot_widget.setLabel("left", "sin(x)")
        self.ui.plot_widget.setLabel("bottom", "x [radians]")
        self.ui.plot_widget.show() 




def main():
    """main: running the class
    """    
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    main()
