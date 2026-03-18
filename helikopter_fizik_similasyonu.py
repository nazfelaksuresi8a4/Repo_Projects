from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import * 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavToolbar
import matplotlib.pyplot as plt
import sys as _s
import math as m
import numpy as np 
import winsound as wsx

class fMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Kaldırma kuvveti similasyonu')

        main_widget = QWidget()
        main_layout = QHBoxLayout()

        main_widget.setLayout(main_layout)

        panel_splitter = QSplitter(Qt.Vertical)
        monitor_splitter = QSplitter(Qt.Vertical)

        self.plotter_fig,self.plotter_ax = plt.subplots(2,1) 
        self.plotter_monitor = FigureCanvas(self.plotter_fig)

        self.plotter_navbar = NavToolbar(self.plotter_monitor)

        self.m_spinbox = QSpinBox()
        self.m_spinbox.setRange(1,2000)
        self.m_spinbox.setValue(1000)
        self.m_spinbox.setFixedHeight(60)

        self.rpm_slider = QSlider(Qt.Horizontal)
        self.rpm_slider.setRange(1,600)
        self.rpm_slider.setValue(150)
        self.rpm_slider.setFixedHeight(60)

        self.lift_label = QLabel(f'Kaldırma kuvveti: ?N')
        self.lift_label.setAlignment(Qt.AlignCenter)

        self.rpm_label = QLabel(f'RPM: ?')
        self.rpm_label.setAlignment(Qt.AlignCenter)

        self.mg_label = QLabel(f'm: ?')
        self.mg_label.setAlignment(Qt.AlignCenter)

        panel_splitter.addWidget(self.lift_label)
        panel_splitter.addWidget(self.mg_label)
        panel_splitter.addWidget(self.rpm_label)
        panel_splitter.addWidget(self.m_spinbox)
        panel_splitter.addWidget(self.rpm_slider)

        monitor_splitter.addWidget(self.plotter_navbar)
        monitor_splitter.addWidget(self.plotter_monitor)

        main_layout.addWidget(panel_splitter)
        main_layout.addWidget(monitor_splitter)

        self.pbar = QProgressBar(self)
        self.pbar.setRange(0,1024)

        self.compute_timer = QTimer(self)
        self.compute_timer.start(1)
        self.compute_timer.timeout.connect(self.calculate_lift)

        self.rpm_array = []
        self.lift_array = []

        self.rpm_array_ref = []
        self.lift_array_ref = []

        self.setCentralWidget(main_widget)

    def draw_graphs(self):
        if len(self.rpm_array) > 0 and len(self.lift_array) > 0:
            if len(self.rpm_array_ref) > 0 and len(self.lift_array_ref) > 0:
                if len(self.lift_array) == len(self.lift_array_ref):
                    if len(self.rpm_array) == len(self.rpm_array_ref):
                        nd_lift,lift_Ref = np.array(self.lift_array),np.array(self.lift_array_ref)
                        nd_rpm,rpm_Ref = np.array(self.rpm_array),np.array(self.rpm_array_ref)

                        rpm_main_to_ref = lift_Ref - nd_lift
                        lift_main_to_ref = rpm_Ref - nd_rpm 

                        self.plotter_ax[0].clear()
                        self.plotter_ax[0].plot(nd_rpm,c='green',label='Açısal hız')
                        self.plotter_ax[0].plot(nd_lift,c='blue',label='Kaldırma kuvveti')
                        self.plotter_ax[0].legend()
                        
                        self.plotter_ax[1].clear()
                        self.plotter_ax[1].plot(rpm_main_to_ref,c='green',label='Açısal hız farkı')
                        self.plotter_ax[1].plot(lift_main_to_ref,c='blue',label='Kaldırma kuvveti farkı')
                        self.plotter_ax[1].legend()

                        print(len(rpm_main_to_ref), '       ', len(lift_main_to_ref))

                        self.plotter_monitor.draw()
                    else:
                        print('y')

                else:
                    print(len(self.lift_array), ',,,,,'   ,len(self.lift_array_ref))
                    self.pbar.setValue(len(self.lift_array_ref))
                    if len(self.lift_array_ref) == 1024:
                        self.pbar.close()
        else:
            print('x')
    def write_values(self,lift,rpm,mg):
        self.mg_label.setText(f'mg: {mg}')
        self.rpm_label.setText(f'Rpm: {rpm}')
        self.lift_label.setText(f'Kaldırma kuvveti: {lift} N')
        self.draw_graphs()

    def calculate_lift(self):
        N = 1024
        RPM = self.rpm_slider.value()
        mX = self.m_spinbox.value()
        g = 9.81
        p = 1.225
        D = 10 
        R = D / 2
        A = m.pi * R ** 2
        
        mg = mX * g
        omega = (2 * m.pi * RPM) / 60
        v = omega * R

        Cl = 0.5

        L = (((2 * m.pi ** 3) * p * (R ** 4) * Cl) / 3600 ) * (RPM ** 2)

        self.lift_array.append(L)
        self.rpm_array.append(omega)

        if len(self.lift_array) > N:
            refValX =self.lift_array.pop(0)
            self.lift_array_ref.append(refValX)

            if len(self.lift_array_ref) > N:
                self.lift_array_ref.pop(0)
        
        if len(self.rpm_array) > N:
            refValY = self.rpm_array.pop(0)
            self.rpm_array_ref.append(refValY)
            
            if len(self.rpm_array_ref) > N:
                self.rpm_array_ref.pop(0)

        #print(L, '   ',mg)

        self.write_values(L,RPM,mX)


if __name__ == "__main__":
    sp = QApplication(_s.argv)
    sw = fMainWindow()
    sw.show()
    _s.exit(sp.exec_())
