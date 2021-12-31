import os

def get():
  sessid = None;
  
  if os.path.exists("session.txt"):
    f = open("session.txt")
    sessid = f.read()
    f.close()
    
    return sessid
  else:
    return sessid;
  
def save(id):
  # Save id(uuid) to session
  f = open("./session.txt", "a");
  f.write(str(id));
  f.close();