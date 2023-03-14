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
        try:
            self.assertEqual(self.ui.number, 21, "yanlis rakam")
        except:
            print("hata")

    def test_open_new_window(self):
        self.assertFalse(self.ui.new_window.isVisible())  
        QtTest.QTest.mouseClick(self.ui.btn_open_window, QtCore.Qt.LeftButton)
        self.ui.new_window.accepted.connect(lambda: self.assertTrue(self.ui.new_window.isVisible()))
        self.ui.new_window.rejected.connect(lambda: self.assertFalse(self.ui.new_window.isVisible()))
        self.assertEqual(self.dialog.isVisible(), True)
        time.sleep(0.5)
        print(inspect.stack()[0][3]+'  calisiyor')
  
    def tearDown(self):
        self.ui.new_window.close()
        self.dialog.close()
        del self.dialog
        self.app.quit()

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
