__author__ = 'Administrator'
import sys
sys.stderr = sys.stdout

from PyQt4.Qt import *
from PyQt4 import QtGui
import MainView

import cut
CONST_CELL_SIZE = 256
CONST_QUALITY = 30

class MainForm(QtGui.QMainWindow,MainView.Ui_MainWindow):


    def __init__(self,app,parent=None):
        super(MainForm, self).__init__(parent)
        self.setupUi(self)
        self.connect(self.pushButton,SIGNAL("clicked()"),self.open)
        self.connect(self.pushButton_2,SIGNAL("clicked()"),self.cut)
        self.fileName = None

    def cut(self):
        try:
            CONST_CELL_SIZE = int(self.cellSize.toPlainText())
            CONST_QUALITY = int(self.quality.toPlainText())
        except:
            print "invalid input"

        if not self.fileName:
            QtGui.QMessageBox.question(self, 'Message',"click open button to select a image first", QtGui.QMessageBox.Yes)
            return
        path = unicode(self.fileName.toUtf8(), 'utf-8', 'ignore')
        cut.cut_image(path,CONST_CELL_SIZE,CONST_QUALITY)
        QtGui.QMessageBox.question(self, 'Message',"cut finish", QtGui.QMessageBox.Yes)

    def open(self):
        fileName= QFileDialog.getOpenFileName(self, "open")
        if fileName:
            self.fileName = fileName

def main():
    app = QtGui.QApplication(sys.argv)
    form = MainForm(app)
    form.show()
    app.exec_()

if __name__ == '__main__':
     main()
