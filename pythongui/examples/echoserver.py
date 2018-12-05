import sys
from ui_echoserver import Ui_Dialog
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class EchoServerDialog(QDialog):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super(EchoServerDialog, self).__init__(parent=parent, flags=flags)
        self.setWindowTitle('fake udp echo server')
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked(self.sendmessage)
    
    @pyqtSlot()
    def sendmessage(self):
        self.ui.output_label.setText('Echo: '+ self.ui.input_edit.text())

app = QApplication(sys.argv)

window = EchoServerDialog()
window.show()

sys.exit(app.exec_())