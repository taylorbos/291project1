import cx_Oracle

def connectToDatabase():
  f = open('connection.info')
  username = f.readline().strip()
  password = f.readline().strip()
  con = cx_Oracle.connect(username, password, "gwynne.cs.ualberta.ca:1521/CRS")	
  return con


def closeDatabase():
  con.commit()
  con.close()


def getUserid(username):	
  statement = "SELECT USR FROM USERS WHERE USERS.NAME = :s"
  curs.execute(statement, {'s':username})
  if(curs.rowcount is 0):
    return None	
  rs = curs.fetchone()[0]
  return rs

def registerUser(username, email, password, timezone=None, city=None):
  getHighestId = "SELECT MAX(USR) FROM USERS"
  curs.execute(getHighestId)
  rs = curs.fetchone()[0]
  userId = rs + 1
  statment = "INSERT INTO USERS VALUES (:ui, :p, :un, :e, :c, :t);"
  curs.execute(statement, {'ui':userId,'p':password,'un':username,'e':email,'c':city,'t':timezone})
	
def loginUser(username, password):
  statment = "SELECT USR FROM USERS WHERE USERS.NAME = :u AND USERS.PWD = :p;"
  curs.execute(statement, {'u':username,'p':password})
  rs = curs.fetchone()[0]
  if(curs.rowcount is 0):
    return None
  return rs
	
	
con = connectToDatabase()
curs = con.cursor()
