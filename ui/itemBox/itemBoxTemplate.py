# Form implementation generated from reading ui file 'ui/itemBox/itemBoxTemplate.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 50)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(0, 50))
        Form.setMaximumSize(QtCore.QSize(16777215, 50))
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nameLabel = QtWidgets.QLabel(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameLabel.sizePolicy().hasHeightForWidth())
        self.nameLabel.setSizePolicy(sizePolicy)
        self.nameLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.nameLabel.setObjectName("nameLabel")
        self.horizontalLayout.addWidget(self.nameLabel)
        self.quantityLabel = QtWidgets.QLabel(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quantityLabel.sizePolicy().hasHeightForWidth())
        self.quantityLabel.setSizePolicy(sizePolicy)
        self.quantityLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.quantityLabel.setObjectName("quantityLabel")
        self.horizontalLayout.addWidget(self.quantityLabel)
        self.priceLabel = QtWidgets.QLabel(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.priceLabel.sizePolicy().hasHeightForWidth())
        self.priceLabel.setSizePolicy(sizePolicy)
        self.priceLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.priceLabel.setObjectName("priceLabel")
        self.horizontalLayout.addWidget(self.priceLabel)
        self.widget = QtWidgets.QWidget(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(50)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox1 = QtWidgets.QCheckBox(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox1.sizePolicy().hasHeightForWidth())
        self.checkBox1.setSizePolicy(sizePolicy)
        self.checkBox1.setBaseSize(QtCore.QSize(0, 0))
        self.checkBox1.setAcceptDrops(False)
        self.checkBox1.setText("")
        self.checkBox1.setObjectName("checkBox1")
        self.horizontalLayout_2.addWidget(self.checkBox1)
        self.checkBox2 = QtWidgets.QCheckBox(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox2.sizePolicy().hasHeightForWidth())
        self.checkBox2.setSizePolicy(sizePolicy)
        self.checkBox2.setText("")
        self.checkBox2.setObjectName("checkBox2")
        self.horizontalLayout_2.addWidget(self.checkBox2)
        self.checkBox3 = QtWidgets.QCheckBox(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox3.sizePolicy().hasHeightForWidth())
        self.checkBox3.setSizePolicy(sizePolicy)
        self.checkBox3.setText("")
        self.checkBox3.setObjectName("checkBox3")
        self.horizontalLayout_2.addWidget(self.checkBox3)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.nameLabel.setText(_translate("Form", "Item Name"))
        self.quantityLabel.setText(_translate("Form", "Quantity"))
        self.priceLabel.setText(_translate("Form", "Price"))
