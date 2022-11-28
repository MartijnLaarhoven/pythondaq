import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Slot
import pyqtgraph as pg
from pythondaq.ui_mainwindow import Ui_MainWindow
from pythondaq.diode_experiment import DiodeExperiment


# PyQtGraph global options
pg.setConfigOption("background", "w")
pg.setConfigOption("foreground", "k")

port = "ASRL4::INSTR"

Experiment = DiodeExperiment()

voltagelist, Currentlist = Experiment.scan(0,1023)

class UserInterface(QtWidgets.QMainWindow):
    """The class of the user interface which makes the interface

    Args:
        QtWidgets (module): the widgets which make the interface
    """
    def __init__(self):
        """The init module
        """        
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Starting.valueChanged.connect(self.plot)
        self.ui.Ending.valueChanged.connect(self.plot)
        self.ui.Numpoints_Value.valueChanged.connect(self.plot)
        self.ui.Startbutton.clicked.connect(self.plot)
        self.plot()

    @Slot()
    def plot(self):
        """The plot module
        """
        self.ui.plot_widget.clear()
        start = int(self.ui.Starting.value() * (1023/3.3))
        end = int(self.ui.Ending.value() * (1023/3.3))
        voltagelist, Currentlist = Experiment.scan(start,end)
        self.ui.plot_widget.plot(voltagelist, Currentlist, pen=None, symbol = 'o')
        self.ui.plot_widget.setLabel("left", "'I [A]'")
        self.ui.plot_widget.setLabel("bottom", 'U_LED [V]')
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
