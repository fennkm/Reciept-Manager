from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog

from .mainWindow import Ui_MainWindow
from ui.itemBox import ItemBox

class Application(QMainWindow, Ui_MainWindow):
    def __init__(self, fileCallback, buttonCallback) -> None:
        self.app: QApplication = QApplication([])

        super().__init__()

        self.setupUi(self)

        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","*.eml")
        self.items = fileCallback(fileName)

        self.actionButton.clicked.connect(lambda _ : buttonCallback(self.items, self))

        for item in reversed(self.items):
            itemBox = ItemBox(self.itemList, *item)
            self.itemList.layout().insertWidget(0, itemBox)

        self.show()

    def exec(self) -> None:
        self.app.exec()