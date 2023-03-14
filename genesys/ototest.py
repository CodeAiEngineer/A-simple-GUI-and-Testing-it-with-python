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
        for tlw in QtWidgets.QApplication.topLevelWidgets():
            if tlw != self.dialog and tlw.isVisible():
                for child in tlw.children():
                    if isinstance(child, QtWidgets.QDialog) and child.isVisible():
                        child.reject()
                tlw.close()
        self.dialog.close()


    def test_increment_number(self):
        initial_number = self.ui.number
        time.sleep(0.5)
        QtTest.QTest.mouseClick(self.ui.pushButton_2, QtCore.Qt.LeftButton)
        
        
        self.assertEqual(self.ui.number, initial_number + 12, "yanlis rakam")
        time.sleep(0.5)
        pyautogui.hotkey('alt', 'f4')
        print(inspect.stack()[0][3]+'  calisiyor')
        

    def test_open_new_window(self):
        self.assertFalse(self.ui.new_window.isVisible())
        
        QtTest.QTest.mouseClick(self.ui.btn_open_window, QtCore.Qt.LeftButton)
        self.ui.new_window.accepted.connect(lambda: self.assertTrue(self.ui.new_window.isVisible()))
        self.ui.new_window.rejected.connect(lambda: self.assertFalse(self.ui.new_window.isVisible()))
        
        self.assertEqual(self.dialog.isVisible(), True)
        time.sleep(0.5)
        pyautogui.hotkey('alt', 'f4')
        print(inspect.stack()[0][3]+'  calisiyor')
        

    def test_show_only_selected(self):
        self.ui.radioButton_1.setChecked(True)
        self.ui.checkBox.setChecked(True)
        QtTest.QTest.mouseClick(self.ui.btn_open_window, QtCore.Qt.LeftButton)
        label = self.ui.new_window.findChild(QtWidgets.QLabel)
        self.assertEqual(label.text(), self.ui.radio1)
        time.sleep(0.5)
        pyautogui.hotkey('alt', 'f4')
        print(inspect.stack()[0][3]+'  calisiyor')
        
        
    def test_tumyazilar(self):
        QtTest.QTest.mouseClick(self.ui.btn_open_window, QtCore.Qt.LeftButton)
        label2 = self.ui.new_window.findChild(QtWidgets.QLabel)
        
        self.assertEqual(label2.text(), self.ui.radio1)
        time.sleep(0.5)
        pyautogui.hotkey('alt', 'f4')
        print(inspect.stack()[0][3]+'  calisiyor')


if __name__ == '__main__':
    try:
        unittest.main()
    except AssertionError as error:
        print(error)