import sys
import unittest
import inspect
from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from son import Ui_Dialog
import pyautogui
import time

class TestMyApp(unittest.TestCase):
    def setUp(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.dialog)
        self.dialog.showNormal()
        
    def tearDown(self):
        self.dialog.close()
        self.ui = None
        self.dialog = None
        self.app.quit()
   
    def test_show_only_selected(self):
        expected_texts = ["apple", "avakado", "lemon"]
        expected_textsColorCodes=["#ff0000","#32cd32","#808000"]
        
        self.ui.checkBox.setChecked(False)
        QtTest.QTest.mouseClick(self.ui.btn_open_window, QtCore.Qt.LeftButton)
        
        for i in range(1,self.ui.new_window.layout().count()):
            widget = self.ui.new_window.layout().itemAt(i).widget()
            if widget:

                print('//**//////////////////////////////' + widget.palette().color(QtGui.QPalette.WindowText).name())

                self.assertEqual(widget.text(), expected_texts[i-1], "Incorrect text in new window")
                self.assertEqual( widget.palette().color(QtGui.QPalette.WindowText).name(), expected_textsColorCodes[i-1], "Incorrect text in new window")

        print("test_show_only_selected passed")



if __name__ == '__main__':
    try:
        unittest.main()
    except AssertionError as error:
        print(error)
