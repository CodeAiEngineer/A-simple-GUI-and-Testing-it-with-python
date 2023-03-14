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
    # Get the initial position of the button
    initial_pos = self.ui.btn_drag.mapToGlobal(self.ui.btn_drag.pos())

    # Simulate a mouse press followed by a move and a release
    QtTest.QTest.mousePress(self.ui.btn_drag, QtCore.Qt.LeftButton, pos=QtCore.QPoint(10, 10))
    QtTest.QTest.mouseMove(self.ui.btn_drag, QtCore.QPoint(20, 20))
    QtTest.QTest.mouseRelease(self.ui.btn_drag, QtCore.Qt.LeftButton, pos=QtCore.QPoint(20, 20))

    # Get the final position of the button
    final_pos = self.ui.btn_drag.mapToGlobal(self.ui.btn_drag.pos())

    # Print some debug information
    print(f"Initial position: {initial_pos}")
    print(f"Final position: {final_pos}")
    print(f"Relative position: {self.ui.btn_drag.pos()}")

    # Check if the button moved
    expected_pos = self.ui.btn_drag.parent().mapToGlobal(QtCore.QPoint(20, 20))
    self.assertEqual(self.ui.btn_drag.mapToGlobal(self.ui.btn_drag.pos()), expected_pos)


"""
    def test_draggable_button(self):
        # simulate a mouse press followed by a move and a release
        QtTest.QTest.mousePress(self.ui.btn_drag, QtCore.Qt.LeftButton, pos=QtCore.QPoint(10, 10))
        QtTest.QTest.mouseMove(self.ui.btn_drag, QtCore.QPoint(20, 20))
        QtTest.QTest.mouseRelease(self.ui.btn_drag, QtCore.Qt.LeftButton, pos=QtCore.QPoint(20, 20))
        


        # check if the button moved
        # check if the button moved
        expected_pos = self.dialog.mapToGlobal(QtCore.QPoint(20, 20))
        self.assertEqual(self.ui.btn_drag.mapToGlobal(self.ui.btn_drag.pos()), expected_pos)
"""



if __name__ == '__main__':
    try:
        unittest.main()
    except AssertionError as error:
        print(error)

