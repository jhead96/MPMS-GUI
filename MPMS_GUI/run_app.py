import sys
from PyQt5 import QtWidgets
from file_manager.FileManager import FileManager
from plot_manager import PlotManager
from display import Ui_MainWindow


class App(QtWidgets.QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_signals()

        self.file_manager = FileManager()


    def connect_signals(self) -> None:
        self.ui.AddDatafileBtn.clicked.connect(self.add_datafile)
        self.ui.RemoveDatafileBtn.clicked.connect(self.remove_datafile)

    def add_datafile(self) -> None:
        # Get filepath using Qdialog
        self.file_manager.add_datafile("test.txt")
        print(self.file_manager)
        # Add new Datafile to FileManager
        self.update_file_list()
        # Update table widget
        pass
        
    def remove_datafile(self) -> None:
        self.file_manager.remove_datafile(0)
        print(self.file_manager)
        # Update table widget
        self.update_file_list()    
        pass

    def update_file_list(self) -> None:
        # Clear table widget
        self.clear_file_list()

        # Get files from FileManager
        files = self.file_manager.get_all_datafiles_as_dict()
        
        # Iterate through datafiles
        for f in files:
            # Insert row at bottom
            num_rows = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(num_rows)

            # Iterate through fields of Datafiles
            for i, (k, v) in enumerate(f.items()):
                # Insert
                curr_item = QtWidgets.QTableWidgetItem(str(v))
                self.ui.tableWidget.setItem(num_rows, i, curr_item)
        
    def clear_file_list(self) -> None:
        self.ui.tableWidget.setRowCount(0)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = App()
    win.show()
    sys.exit(app.exec())


