from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
import sys as _s

class mainF(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)

        self.date_widget = QDateEdit()
        self.date_widget.setAlignment(Qt.AlignCenter)

        button = QPushButton(text='Tamam')
        
        self.label = QLabel(text='Tarih: ')
        self.label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.date_widget)
        layout.addWidget(self.label)
        layout.addWidget(button)

        button.clicked.connect(self.show_date)

        self.setCentralWidget(widget)

    def show_date(self):
        self.date = self.date_widget.date()

        print(self.date.toPyDate())

        

if __name__=="__main__":
    sp = QApplication(_s.argv)
    sw = mainF()
    sw.show()
    _s.exit(sp.exec_())
