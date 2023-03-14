import sys
from PyQt5 import QtCore, QtGui, QtWidgets

radio1 ='apple'

radio2 ='avokado'
radio3 ='lemon'
class Ui_Dialog(object):
    radio1 ='apple'

    radio2 ='avokado'
    radio3 ='lemon'
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(401, 300)
        Dialog.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 401, 151))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color:rgb(255, 0, 0)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        
        
        self.btn_drag = DraggableButton(self.frame)
        self.btn_drag.setGeometry(QtCore.QRect(160, 60, 75, 23))
        self.btn_drag.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.btn_drag.setObjectName("btn_drag")
        
        self.dragging = False  # flag to track if the button is being dragged
        self.offset = None  # offset between the mouse cursor and the button position


        
        
        
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 180, 61, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.btn_open_window = QtWidgets.QPushButton(Dialog)
        self.btn_open_window.setGeometry(QtCore.QRect(260, 230, 75, 23))
        self.btn_open_window.setObjectName("btn_open_window")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 210, 147, 22))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        
        
        
        # self.radioButton_1 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        # self.radioButton_1.setObjectName("radioButton_1")       
        
        
        self.radioButton_2 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        

        
        self.gridLayout.addWidget(self.radioButton_2, 0, 1, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 0, 2, 1, 1)
        self.radioButton_1 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_1.setObjectName("radioButton_1")
        self.gridLayout.addWidget(self.radioButton_1, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(10, 260, 161, 16))
        self.checkBox.setObjectName("checkBox")
        self.frame.raise_()
        self.gridLayoutWidget.raise_()
        self.pushButton_2.raise_()
        self.btn_open_window.raise_()
        self.checkBox.raise_()



        self.number_label = QtWidgets.QLabel(Dialog)
        self.number_label.setGeometry(QtCore.QRect(10, 180, 20, 20))
        self.number_label.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.number_label.setAlignment(QtCore.Qt.AlignCenter)
        self.number_label.setObjectName("number_label")
        self.number = 0
        self.update_number_label()

        self.pushButton_2.clicked.connect(self.increment_number)
        self.btn_open_window.clicked.connect(self.open_new_window)

        
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def increment_number(self):
        self.number += 1
        self.update_number_label()

    def update_number_label(self):
        self.number_label.setText(str(self.number))
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_drag.setText(_translate("Dialog", "Drag"))
        self.pushButton_2.setText(_translate("Dialog", "+"))
        self.btn_open_window.setText(_translate("Dialog", "Open Window"))
        self.radioButton_2.setText(_translate("Dialog", "2"))
        self.radioButton_3.setText(_translate("Dialog", "3"))
        self.radioButton_1.setText(_translate("Dialog", "1"))
        self.checkBox.setText(_translate("Dialog", "Show Only Selected"))
        
        
    def open_new_window(self):
        if self.radioButton_1.isChecked():
            yazim=radio1
            
            self.new_window = NewWindow(yazim)
            self.new_window.exec_()         
        
        
        if self.radioButton_2.isChecked():
            yazim=radio2
            
            self.new_window = NewWindow(yazim)
            self.new_window.exec_()    
            
        if self.radioButton_3.isChecked():
            yazim=radio3
            
            self.new_window = NewWindow(yazim)
            self.new_window.exec_()             
        # if self.radioButton_3.isChecked():
    
        
                
class DraggableButton(QtWidgets.QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__mousePressPos = None
        self.__mouseMovePos = None

    def mousePressEvent(self, event):
        self.__mousePressPos = event.globalPos()
        self.__mouseMovePos = event.globalPos()

        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.__mousePressPos:
            delta = event.globalPos() - self.__mouseMovePos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.__mouseMovePos = event.globalPos()

        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.__mousePressPos = None

        super().mouseReleaseEvent(event)
        
        
class NewWindow(QtWidgets.QDialog):
    def __init__(self,yazim):
        super().__init__()
        self.setWindowTitle("New Window")
        self.setFixedSize(200, 200)
        self.label = QtWidgets.QLabel(yazim)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)



        
        
        
        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
