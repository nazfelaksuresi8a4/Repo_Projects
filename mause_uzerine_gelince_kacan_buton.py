from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QPushButton,QLineEdit,QApplication,QMainWindow,QMessageBox
import sys as _s
import random

class mainClass(QMainWindow):
    def __init__(self):
        super().__init__()

        a = QMessageBox.information(self,'x,','*x')

        self.btn = QPushButton('Onayla',self)
        self.lineedit = QLineEdit(self)
        self.lineedit.setPlaceholderText('İsim')
        self.a = None
        
        self.btn.move(self.width() // 2,self.height() // 2)
        self.lineedit.move((self.width() // 2), (self.height() // 2) - 50)

        self.btn.enterEvent = self.enterfnc
        self.btn.closeEvent = self.closefnc

        self.s1 = 50
        self.s2 = 50

        self.btn.resize(self.s1,self.s2)

    
    def enterfnc(self,a0):
        if self.s1 == self.s2 or self.s2 == self.s1:
            self.a = 'ok'
        
        else:
            self.a = None

        self.btn.setEnabled(False)
        if self.a is not None:
            x = random.randint(0,self.width() -  self.s1)
            y = random.randint(0,self.height() - self.s2)

        else:
            x = random.randint(0,self.width() -  self.s1)
            y = random.randint(0,self.height() - self.s1)

        self.btn.move(x,y)
    
    def closefnc(self,a0):
        self.btn.setEnabled(True)
        
        

if __name__ == "__main__":
    sp = QApplication(_s.argv)
    sw = mainClass()
    sw.show()
    _s.exit(sp.exec_())
