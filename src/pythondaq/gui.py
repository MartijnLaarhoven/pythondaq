import sys
from PySide6 import QtWidgets
import pyqtgraph as pg

class UserInterface(QtWidgets.QMainWindow):
    pass

# PyQtGraph global options
pg.setConfigOption("background", "w")
pg.setConfigOption("foreground", "k")





def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    main()
