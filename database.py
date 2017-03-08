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
	
def getUsername(userId):
	statement = "SELECT NAME FROM USERS WHERE USERS.USR = :ui"
	curs.execute(statement, {'ui':userId})
	rs = curs.fetchone()
	if(rs is None):
		return None
	return rs[0]
  
def loginUser(username, password):
  statement = "SELECT USR FROM USERS WHERE USERS.NAME = :u AND USERS.PWD = :p"
  curs.setinputsizes(u = curs.var(cx_Oracle.FIXED_CHAR, 20), p = curs.var(cx_Oracle.FIXED_CHAR, 4))
  curs.execute(statement, {'u':username,'p':password})
  r = curs.fetchone()
  if(r is None):
    return None
  return r[0]

def getUserMainPageInfo(userId):	
	statement = ("SELECT * FROM ((SELECT TWEETS.WRITER, TWEETS.TEXT, TWEETS.TDATE FROM FOLLOWS,"
	" TWEETS WHERE FOLLOWS.FLWEE = TWEETS.WRITER AND FOLLOWS.FLWER = :ui) UNION (SELECT RETWEETS.USR,"
	" TWEETS.TEXT, RETWEETS.RDATE FROM FOLLOWS, RETWEETS, TWEETS WHERE FOLLOWS.FLWEE = RETWEETS.USR "
	"AND FOLLOWS.FLWER = :ui AND TWEETS.TID = RETWEETS.TID)) A ORDER BY A.TDATE DESC")
	curs.execute(statement, {'ui':userId})
	r = curs.fetchall()
	result = []
	for rows in r:
		tweeterName = getUsername(rows[0])
		resultString =  '%s %s At: %s' % (tweeterName, rows[1], rows[2])
		result.append(resultString) 
	return result
def searchTweets():
  keywords = input("Enter #hastags or words to search: ").split()
  statement = "SELECT DISTINCT * FROM ("
  n = 0
  sizes = ()
  args = ()
  for keyword in keywords:
    if n != 0:
      statement = statement + "union "
    if keyword[0] == "#":
      n = n + 1
      statement = statement + "(SELECT TWEETS.* FROM TWEETS, MENTIONS WHERE TWEETS.TID = MENTIONS.TID AND MENTIONS.TERM = :" + str(n) + ") "
      sizes = sizes + (curs.var(cx_Oracle.FIXED_CHAR, 10),)
      args = args + (keyword[1:],)
    else:
      n = n + 1
      statement = statement + "(SELECT TWEETS.* FROM TWEETS WHERE TWEETS.TEXT LIKE :" + str(n) + ") "
      sizes = sizes + (curs.var(cx_Oracle.FIXED_CHAR, 10),)
      args = args + ("%" + keyword + "%",)
  statement = statement + ")"
  curs.setinputsizes(*sizes)
  curs.execute(statement, args)
  r = curs.fetchall()
  if r == []:
    print("No search results")
  else:
    for s in r:
      print(s)

con = connectToDatabase()
curs = con.cursor()
