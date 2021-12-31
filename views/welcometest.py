from PySide2.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QLineEdit, QSizePolicy,QPushButton, QCheckBox, QHBoxLayout
from PySide2.QtCore import Slot
from PySide2 import QtCore
from PySide2.QtGui import QCursor
from setup import connection as db, session as s
import bcrypt
from views.dashboard import Dashboard

class WelcomeTest():
  @Slot()
  def btn_clicked(self):
    email=self.email.text()
    password=self.password.text()
    
    if email == "" and password == "":
      self.error.setText("Field is required")
      self.error.setStyleSheet("background: red; padding: 1ex; color: white;")
    elif email != "" and password == "":
      self.error.setText("Password is required")
      self.error.setStyleSheet("background: red; padding: 1ex; color: white;")
    else:
      self.error.setText("")
      self.error.setStyleSheet("background: transparent; padding: 0; color: #ccc;")
      
      sql = "SELECT * FROM public.users WHERE public.users.email='"+email+"'"
      result = db.read(sql)
      
      if not result:
        print("Account not registered")
        return False
      else:
        # Check password verify
        hashed = result[5].encode("utf8")
        passwd = b''+password.encode("utf8")
        matched = bcrypt.checkpw(passwd, hashed)
        
        if not matched:
          print("Passwords do not match")
        else:
          # Save id(uuid) to session
          s.save(str(result[0]))
          
          Dashboard().main()
    
  def main(self):
    app = QApplication([]);
    window = QWidget()
    self.label = QLabel()
    email_label = QLabel("Email")
    password_label = QLabel("Password")
    self.email=QLineEdit()
    self.password=QLineEdit()
    checkbox=QCheckBox("remember me")
    forget_password=QLabel("Forget password?")
    
    self.error = QLabel();
    
    btn_login=QPushButton("Login")
    
    self.email.setPlaceholderText("Input your email")
    self.email.setStyleSheet("padding: 1ex;")
    self.email.setObjectName("email")
    self.password.setPlaceholderText("Input your password")
    self.password.setStyleSheet("padding: 1ex;")
    self.password.setObjectName("password")
    self.password.setEchoMode(QLineEdit.Password)
    forget_password.setStyleSheet("color: blue;")
    forget_password.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    btn_login.setStyleSheet("padding: 1.5ex 2ex; background: rgb(0, 100, 100); font-size: 12pt;")
    btn_login.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    btn_login.clicked.connect(self.btn_clicked)
    
    layout=QVBoxLayout()
    helpers=QHBoxLayout()
    helpers.setSpacing(240)
    
    
    layout.addWidget(self.error)
    layout.addWidget(self.label)
    layout.addWidget(email_label)
    layout.addWidget(self.email)
    layout.addWidget(password_label)
    layout.addWidget(self.password)
    helpers.addWidget(checkbox)
    helpers.addWidget(forget_password)
    layout.addLayout(helpers)
    layout.addWidget(btn_login)
    
    window.setGeometry(420,200,480,320)
    window.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    window.setLayout(layout)
    window.setWindowTitle("Welcome administrator")
    window.show()
    
    app.exec_()
    
if __name__ == "__main__":
  w = WelcomeTest()
  w.main()