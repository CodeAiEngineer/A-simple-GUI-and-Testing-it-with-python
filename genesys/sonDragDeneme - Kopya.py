import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import time
from son import DraggableButton

class TestDraggableButton(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.btn = DraggableButton("Drag me", self)
        self.btn.setGeometry(QtCore.QRect(10, 10, 100, 30))
        

    def test_drag(self):
        # Simulate mouse press at (20, 20) relative to the button
        event = QtGui.QMouseEvent(QtCore.QEvent.MouseButtonPress,
                                  QtCore.QPointF(20, 20),
                                  QtCore.Qt.LeftButton,
                                  QtCore.Qt.LeftButton,
                                  QtCore.Qt.NoModifier)
        QtWidgets.QApplication.sendEvent(self.btn, event)
        time.sleep(1)

        # Simulate mouse move to (50, 50) relative to the button
        event = QtGui.QMouseEvent(QtCore.QEvent.MouseMove,
                                  QtCore.QPointF(50, 50),
                                  QtCore.Qt.NoButton,
                                  QtCore.Qt.LeftButton,
                                  QtCore.Qt.NoModifier)
        QtWidgets.QApplication.sendEvent(self.btn, event)
        time.sleep(1)
        # Assert that the button's position has been updated
        assert self.btn.pos() == QtCore.QPoint(40, 40)

        # Simulate mouse release
        event = QtGui.QMouseEvent(QtCore.QEvent.MouseButtonRelease,
                                  QtCore.QPointF(50, 50),
                                  QtCore.Qt.LeftButton,
                                  QtCore.Qt.LeftButton,
                                  QtCore.Qt.NoModifier)
        QtWidgets.QApplication.sendEvent(self.btn, event)
        time.sleep(1)
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    dialog = TestDraggableButton()
    dialog.show()

    dialog.test_drag()

    sys.exit(app.exec_())
