import sys
import unittest
import pyautogui
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QApplication, QDialog
from son import Ui_Dialog
import time


class TestDraggableButton(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.dialog = QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.dialog)
        self.dialog.show()

    def tearDown(self):
        self.dialog.close()
        self.app.quit()

    def test_draggable_button(self):
        # get the initial position of the button
        initial_pos = self.ui.btn_drag.pos()

        # simulate mouse press event on the button
        QTest.mousePress(self.ui.btn_drag, Qt.LeftButton, pos=initial_pos)

        # calculate drag distance and drag to the new position
        drag_distance = pyautogui.Point(100, 100)
        drag_destination = QPoint(initial_pos.x() + drag_distance.x, initial_pos.y() + drag_distance.y)
        
        # hide physical cursor and use virtual cursor instead
        QCursor.setPos(initial_pos)
        pyautogui.FAILSAFE = False
        pyautogui.PAUSE = 0.1

        pyautogui.moveTo(initial_pos.x(), initial_pos.y())
        time.sleep(1)
        pyautogui.dragTo(drag_destination.x(), drag_destination.y(), duration=1)
        time.sleep(1)

        # show physical cursor again
        pyautogui.FAILSAFE = True
        QCursor.setPos(drag_destination)

        # simulate mouse release event
        QTest.mouseRelease(self.ui.btn_drag, Qt.LeftButton, pos=drag_destination)

        # get the final position of the button
        final_pos = self.ui.btn_drag.pos()

        # assert that the position has changed
        self.assertNotEqual(initial_pos, final_pos)


if __name__ == '__main__':
    unittest.main()
