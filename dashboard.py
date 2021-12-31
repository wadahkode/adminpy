from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QPushButton
import sys

def main():
  app=QApplication(sys.argv)
  app.setStyle("Windows")
  
  window=QWidget()
  layout=QVBoxLayout()
  
  top=QPushButton("top")
  layout.addWidget(top)
  layout.addWidget(QPushButton("Bottom"))
  
  window.setGeometry(360,200,680,460)
  top.move(50,20)
  
  window.setWindowTitle("Welcome administrator")
  window.setLayout(layout)
  window.show()
  
  sys.exit(app.exec())
  
if __name__ == "__main__":
  main()