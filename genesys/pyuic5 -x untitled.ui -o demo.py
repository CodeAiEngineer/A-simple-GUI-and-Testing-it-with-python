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
        del self.dialog
        self.app.quit()

    
        
    def test_show_only_selected(self):
        self.ui.radioButton_1.setChecked(True)
        self.ui.radioButton_2.setChecked(False)
        self.ui.radioButton_3.setChecked(False)
        self.ui.checkBox.setChecked(True)

        QtTest.QTest.mouseClick(self.ui.btn_open_window, QtCore.Qt.LeftButton)

        label = self.ui.new_window.findChild(QtWidgets.QLabel)
        self.assertEqual(label.text(), "apple", "Incorrect text in new window")

        self.ui.radioButton_1.setChecked(False)
        self.ui.radioButton_2.setChecked(True)
        self.ui.radioButton_3.setChecked(False)

        QtTest.QTest.mouseClick(self.ui.btn_open_window, QtCore.Qt.LeftButton)

        label = self.ui.new_window.findChild(QtWidgets.QLabel)
        self.assertEqual(label.text(), "avakado", "Incorrect text in new window")

        self.ui.radioButton_1.setChecked(False)
        self.ui.radioButton_2.setChecked(False)
        self.ui.radioButton_3.setChecked(True)

        QtTest.QTest.mouseClick(self.ui.btn_open_window, QtCore.Qt.LeftButton)

        label = self.ui.new_window.findChild(QtWidgets.QLabel)
        self.assertEqual(label.text(), "lemon", "Incorrect text in new window")

        self.ui.checkBox.setChecked(False)

        QtTest.QTest.mouseClick(self.ui.btn_open_window, QtCore.Qt.LeftButton)

        #self.assertTrue(self.ui.new_window.isVisible())
        #self.assertEqual(self.ui.new_window.layout().count(), 3, "Incorrect number of labels in new window")
        labels = [self.ui.new_window.layout().itemAt(i).widget() for i in range(3)]
        texts = [label.text() for label in labels]
        self.assertCountEqual(texts, ["apple", "avakado", "lemon"], "Incorrect text in new window")

        print("test_show_only_selected passed")


if __name__ == '__main__':
    try:
        unittest.main()
    except AssertionError as error:
        print(error)