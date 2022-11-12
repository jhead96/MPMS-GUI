import sys
from PyQt5 import QtWidgets
from display import Ui_MainWindow
from file_manager import FileManager
from plot_manager import PlotManager



app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())

