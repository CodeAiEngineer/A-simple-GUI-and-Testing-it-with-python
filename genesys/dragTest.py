import sys
import unittest
from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from son import Ui_Dialog
import time
import inspect
class TestMyApp(unittest.TestCase):
    def setUp(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.dialog)


    def test_draggable_button(self):
        # simulate a mouse press followed by a move and a release
        QtTest.QTest.mousePress(self.ui.btn_drag, QtCore.Qt.LeftButton, pos=QtCore.QPoint(10, 10))
        QtTest.QTest.mouseMove(self.ui.btn_drag, QtCore.QPoint(20, 20))
        QtTest.QTest.mouseRelease(self.ui.btn_drag, QtCore.Qt.LeftButton, pos=QtCore.QPoint(20, 20))
        


        # check if the button moved
        self.assertEqual(self.ui.btn_drag.pos(), QtCore.QPoint(20, 20))



if __name__ == '__main__':
    try:
        unittest.main()
    except AssertionError as error:
        print(error)