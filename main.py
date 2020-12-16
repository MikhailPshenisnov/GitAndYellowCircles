import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circles(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circles(self, qp):
        # Цвет Яндекса же подойдет для желтого? Ну который (255, 204, 0)
        qp.setBrush(QColor(255, 204, 0))
        r = random.randint(10, 200)
        qp.drawEllipse(25, 50, r, r)
        r = random.randint(10, 200)
        qp.drawEllipse(250, 200, r, r)
        r = random.randint(10, 200)
        qp.drawEllipse(500, 150, r, r)
        self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
