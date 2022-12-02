import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Slot
import pyqtgraph as pg
from pythondaq.ui_mainwindow import Ui_MainWindow
from pythondaq.diode_experiment import DiodeExperiment
import csv

# PyQtGraph global options
pg.setConfigOption("background", "w")
pg.setConfigOption("foreground", "k")

port = "ASRL4::INSTR"



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
        self.ui.Startbutton.clicked.connect(self.plot)
        # self.plot()
        start_button = QtWidgets.QPushButton("Start")
        start_button.clicked.connect(self.start_button_clicked)
        save_button = QtWidgets.QPushButton("Save")
        save_button.clicked.connect(self.save_button_clicked)
        self.Experiment = DiodeExperiment()

    @Slot()
    def start_button_clicked(self):
        self.voltagelist, self.Currentlist = self.Experiment.scan(0,1023)

    @Slot()
    def plot(self):
        """The plot module
        """
        self.ui.plot_widget.clear()
        start = int(self.ui.Starting.value() * (1023/3.3))
        end = int(self.ui.Ending.value() * (1023/3.3))
        self.voltagelist, self.Currentlist = self.Experiment.scan(start,end)
        self.ui.plot_widget.plot(self.voltagelist, self.Currentlist, pen=None, symbol = 'o')
        self.ui.plot_widget.setLabel("left", "'I [A]'")
        self.ui.plot_widget.setLabel("bottom", 'U_LED [V]')
        self.ui.plot_widget.show() 

    @Slot()
    def save_button_clicked(self):
        """Making the cvs file
        """
        with open("adruinodata.txt", "w",newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["voltage_LED,Current_resistor"])
        for u, i in zip(self.voltagelist,self.Currentlist):
            writer.writerow([u,i])

def main():
    """main: running the class
    """    
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    main()
