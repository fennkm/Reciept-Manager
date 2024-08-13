from PyQt6.QtWidgets import QWidget

from .itemBoxTemplate import Ui_Form
    
class ItemBox(QWidget, Ui_Form):
    def __init__(self, parent: QWidget, name, quantity, price) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.nameLabel.setText(name)
        self.quantityLabel.setText(str(quantity))
        self.priceLabel.setText("£" + "{:,.2f}".format(price / 100))