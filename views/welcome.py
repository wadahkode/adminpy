from setup import connection as db, session as s
import pwinput
import bcrypt

class Welcome():
  def main(self):
    email=input("email: ")
    password=pwinput.pwinput("Password: ")
    
    if email == "" and password == "":
      print("Field input is required")
      return False
    else:
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
          s.save(str(result[0]));
          sessid = result[0];
          
          print(sessid)
    
if __name__ == "__main__":
  Welcome()