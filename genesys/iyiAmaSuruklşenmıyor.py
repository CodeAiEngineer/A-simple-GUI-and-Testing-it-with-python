import sys
import unittest
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from PyQt5.QtWidgets import QApplication, QDialog
from son import Ui_Dialog, DraggableButton
import unittest
import pyautogui
import time

class TestDraggableButton(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.dialog = QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.dialog)
        self.dialog.show()
        time.sleep(1)

    def tearDown(self):
        self.dialog.close()
        self.app.quit()

    def test_draggable_button(self):
        
        # get the initial position of the button
        initial_pos = self.ui.btn_drag.pos()
        print(initial_pos)
        screenWidth, screenHeight = pyautogui.size()
        # simulate mouse press event on the button
        QTest.mousePress(self.ui.btn_drag, Qt.LeftButton)
                # Fare imlecinin ortalama konumunu hesapla
        x = screenWidth // 2
        y = screenHeight // 2
        # simulate mouse move events to drag the button
       
        QTest.mouseMove(self.ui.btn_drag, QtCore.QPoint(10, 10))
        #pyautogui.mouseDown(x, y, button='left')
        pyautogui.dragTo( x+15,y+15,duration=1,button='left')
        
        time.sleep(5)
        pyautogui.mouseUp(button='left')
        # get the final position of the button
        final_pos = self.ui.btn_drag.pos()

        # assert that the position has changed
        self.assertNotEqual(initial_pos, final_pos)

if __name__ == '__main__':
    unittest.main()
