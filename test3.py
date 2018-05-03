from PyQt5.QtWidgets import *

import sys

class Windown (QWidget):
    def __init__(self, parent=None):
        super(Windown, self).__init__(parent)


root = QApplication(sys.argv)
app = Windown()
app.show()

sys.exit(root.exec_())