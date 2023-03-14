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

    

    def test_increment_number(self):
        initial_number = self.ui.number
        for i in range(10):
            QtTest.QTest.qWait(200)
            QtTest.QTest.mouseClick(self.ui.pushButton_2, QtCore.Qt.LeftButton)
        QtTest.QTest.qWait(1500)
        try:
           
            self.assertEqual(self.ui.number, initial_number + 21, "yanlis rakam")
            print(inspect.stack()[0][3]+'  calisiyor')
            QtTest.QTest.qWait(1500)
            
        except:
            print(inspect.stack()[0][3]+'  CALISMIYOR!!!')
            
        pyautogui.hotkey('alt', 'f4')  
        

    def test_show_only_selected(self):
        self.ui.radioButton_1.setChecked(False)
        self.ui.checkBox.setChecked(False)
        QtTest.QTest.qWait(1500)
        self.ui.radioButton_1.setChecked(True)
        QtTest.QTest.qWait(1500)
        self.ui.checkBox.setChecked(True)
        QtTest.QTest.qWait(1500)
        QtTest.QTest.mouseClick(self.ui.btn_open_window, QtCore.Qt.LeftButton)
        label = self.ui.new_window.findChild(QtWidgets.QLabel)
        self.assertEqual(label.text(), self.ui.radio1,  "hata")  
        time.sleep(0.5)
       # pyautogui.hotkey('alt', 'f4')
        print(inspect.stack()[0][3]+'  calisiyor')
        
        


if __name__ == '__main__':
    try:
        unittest.main()
    except AssertionError as error:
        print(error)