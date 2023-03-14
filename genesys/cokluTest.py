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
        
    
    def test_increment_number(self):
        # Check if the initial value of number is 0
        self.assertEqual(self.ui.number, 0)

        # Click the increment button twice
        QtTest.QTest.mouseClick(self.ui.pushButton_2, QtCore.Qt.LeftButton)
        QtTest.QTest.mouseClick(self.ui.pushButton_2, QtCore.Qt.LeftButton)
        
        # Check if the value of number is 2
        self.assertEqual(self.ui.number, 2, "yanlis rakam")
  
        

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)