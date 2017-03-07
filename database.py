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
  curs.setinputsizes(s = curs.var(cx_Oracle.FIXED_CHAR, 20))
  curs.execute(statement, {'s':username})
  r = curs.fetchone()
  if(r is None):
    return None	
  return r[0]

def registerUser(username, email, password, timezone=None, city=None):
  getHighestId = "SELECT MAX(USR) FROM USERS"
  curs.execute(getHighestId)
  rs = curs.fetchone()[0]
  userId = rs + 1
  statement = "INSERT INTO USERS VALUES (:ui, :p, :un, :e, :c, :t)"
  curs.setinputsizes(ui = int, p = curs.var(cx_Oracle.FIXED_CHAR, 4), un = curs.var(cx_Oracle.FIXED_CHAR, 20), e = curs.var(cx_Oracle.FIXED_CHAR, 15), c = curs.var(cx_Oracle.FIXED_CHAR, 12), t = float)
  curs.execute(statement, {'ui':userId,'p':password,'un':username,'e':email,'c':city,'t':timezone})
  con.commit()
	
def loginUser(username, password):
  statement = "SELECT USR FROM USERS WHERE USERS.NAME = :u AND USERS.PWD = :p"
  curs.setinputsizes(u = curs.var(cx_Oracle.FIXED_CHAR, 20), p = curs.var(cx_Oracle.FIXED_CHAR, 4))
  curs.execute(statement, {'u':username,'p':password})
  r = curs.fetchone()
  if(r is None):
    return None
  return r[0]

def searchTweets(keywords):
  statement = "SELECT DISTINCT * FROM ("
  n = 0
  for keyword in keywords:
    if n != 0:
      statement = statement + "union "
    if keyword[0] == "#":
      n = n + 1
      statement = statement + "(SELECT TWEETS.* FROM TWEETS, MENTIONS WHERE TWEETS.TID = MENTIONS.TID AND MENTIONS.TERM = '" + keyword[1:] + "') "	
  statement = statement + ")"
  curs.execute(statement)
  r = curs.fetchall()
  for s in r:
    print(s[0])

con = connectToDatabase()
curs = con.cursor()
