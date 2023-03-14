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
        time.sleep(0.5)
        QtTest.QTest.mouseClick(self.ui.pushButton_2, QtCore.Qt.LeftButton)
        
        try:
            self.assertEqual(self.ui.number, initial_number + 21, "yanlis rakam")
            print(inspect.stack()[0][3]+'  calisiyor')
        except:
            print(inspect.stack()[0][3]+'  CALISMIYOR!!!')
            
        
        time.sleep(0.5)
        pyautogui.hotkey('alt', 'f4')
        
        

    def test_open_new_window(self):
        self.assertFalse(self.ui.new_window.isVisible())
        
        QtTest.QTest.mouseClick(self.ui.btn_open_window, QtCore.Qt.LeftButton)
        self.ui.new_window.accepted.connect(lambda: self.assertTrue(self.ui.new_window.isVisible()))
        self.ui.new_window.rejected.connect(lambda: self.assertFalse(self.ui.new_window.isVisible()))
        
        self.assertEqual(self.dialog.isVisible(), True, "hata")
        time.sleep(0.5)
      #  pyautogui.hotkey('alt', 'f4')
        print(inspect.stack()[0][3]+'  calisiyor')
        

    def test_show_only_selected(self):
        self.ui.radioButton_1.setChecked(True)
        self.ui.checkBox.setChecked(True)
        QtTest.QTest.mouseClick(self.ui.btn_open_window, QtCore.Qt.LeftButton)
        label = self.ui.new_window.findChild(QtWidgets.QLabel)
        self.assertEqual(label.text(), self.ui.radio1,  "hata")  
        time.sleep(0.5)
       # pyautogui.hotkey('alt', 'f4')
        print(inspect.stack()[0][3]+'  calisiyor')
        
        
    def test_tumyazilar(self):
        QtTest.QTest.mouseClick(self.ui.btn_open_window, QtCore.Qt.LeftButton)
        label2 = self.ui.new_window.findChild(QtWidgets.QLabel)
        
        self.assertEqual(label2.text(), self.ui.radio1, "hata")
        time.sleep(0.5)
        #pyautogui.hotkey('alt', 'f4')
        print(inspect.stack()[0][3]+'  calisiyor')


if __name__ == '__main__':
    try:
        unittest.main()
    except AssertionError as error:
        print(error)