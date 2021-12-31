from setup import session as s
from views.dashboard import Dashboard
from views.welcometest import WelcomeTest

def main() -> None:
  sessid = s.get()
  
  if sessid == None:
    WelcomeTest().main()
  else:
    Dashboard().main()
    
if __name__ == "__main__":
  main()
