import sys
import unittest
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication, QDialog
from main import Ui_Dialog
import unittest
import pyautogui


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
    
        initial_pos = self.ui.btn_drag.pos()
        print(initial_pos)
        screenWidth, screenHeight = pyautogui.size()
        QTest.mousePress(self.ui.btn_drag, Qt.LeftButton)
        x = screenWidth // 2
        y = screenHeight // 2
        QTest.mouseMove(self.ui.btn_drag, QPoint(10, 10))
        pyautogui.dragTo(x, y-150, duration=1, button='left')
        QTest.qWait(1400)
        QTest.mouseRelease(self.ui.btn_drag, Qt.LeftButton)
        final_pos = self.ui.btn_drag.pos()
        self.assertNotEqual(initial_pos, final_pos)
        print("Test başarılı,final pos  "+str(final_pos))

if __name__ == '__main__':
    unittest.main()
