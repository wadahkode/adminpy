from PySide2.QtWidgets import QApplication,QWidget,QLabel,QHBoxLayout
import sys
from setup import session as s
from views import dashboard

class Dashboard():
  def main(self):
    sessid = s.get()
    
    if sessid == None:
      return dashboard.Dashboard().main()
    else:
      self.app = QApplication(sys.argv)
      self.window = QWidget()
      self.label = QLabel("Ini dashboard")
      self.layout = QHBoxLayout()
      
      self.layout.addWidget(self.label)
      
      self.window.setGeometry(420,200,480,320)
      self.window.setLayout(self.layout)
      self.window.setWindowTitle("Welcome administrator")
      self.window.show()
      
      self.app.exec_()
    
if __name__ == '__main__':
  Dashboard()