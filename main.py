import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main2 import Ui_MainWindow
from PySide6.QtGui import QPixmap
from PySide6.QtCore import SIGNAL
import ui_main2
from graphic import Get_trace
from time import sleep

class Trace_calc(QMainWindow):
    def __init__(self):
        super(Trace_calc, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
      
        self.ui.ok_button.connect(self.ui.ok_button, SIGNAL("clicked()"), self.button_click)
        
    def button_click(self):
        angle = int(self.ui.line_for_angle.text())
        speed = int(self.ui.line_for_speed.text())
        
        trace = Get_trace(speed, angle)
        trace.graph_init()
        trace.get_pic()
            
        pixmap = QPixmap(f'pics\graphic{Get_trace.counter}.png') 
        self.ui.picspace.setPixmap(pixmap)

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Trace_calc()
    window.show()
    sys.exit(app.exec())