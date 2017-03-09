import cx_Oracle
import datetime
import re

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
  if(rs is None): userId = 0  
  else: userId = rs + 1
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
	statement = ("SELECT * FROM ((SELECT TWEETS.WRITER, TWEETS.TEXT, TWEETS.TDATE, TWEETS.TID FROM FOLLOWS,"
	" TWEETS WHERE FOLLOWS.FLWEE = TWEETS.WRITER AND FOLLOWS.FLWER = :ui) UNION (SELECT RETWEETS.USR,"
	" TWEETS.TEXT, RETWEETS.RDATE, RETWEETS.TID FROM FOLLOWS, RETWEETS, TWEETS WHERE FOLLOWS.FLWEE = RETWEETS.USR "
	"AND FOLLOWS.FLWER = :ui AND TWEETS.TID = RETWEETS.TID)) A ORDER BY A.TDATE DESC")
	curs.execute(statement, {'ui':userId})
	r = curs.fetchall()
	result = []
	ids = []
	for rows in r:
		tweeterName = getUsername(rows[0])
		resultString =  '%s %s At: %s' % (tweeterName, rows[1], rows[2])
		result.append(resultString)
		ids.append(rows[3])
	
	return (result, ids)


def searchTweets(keywords):
  #keywords = input("Enter #hastags or words to search: ").split()
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
  result = []
  for rows in r:
    tweeterName = getUsername(rows[1])
    resultString = '%s %s At: %s' % (tweeterName, rows[3], rows[2])
    result.append(resultString)
  return result


def registerTweet(userId, tweet):
  getHighestId = "SELECT MAX(TID) FROM TWEETS"
  curs.execute(getHighestId)
  tid = curs.fetchone()[0]
  if(tid is None): tid = 0
  else: tid = tid + 1
  cdate = datetime.datetime.now()
  statement = "INSERT INTO TWEETS VALUES (:tid, :userid, :cdate, :text, NULL)"
  curs.setinputsizes(tid = int, userid = int, cdate = datetime.datetime, text = curs.var(cx_Oracle.FIXED_CHAR, 80))  
  curs.execute(statement, {'tid':tid, 'userid':userId, 'cdate':cdate, 'text':tweet})

  hashtagGrabber = re.findall(r"#(\w+)", tweet)
  statement = "SELECT TERM FROM MENTIONS"
  curs.execute(statement)
  rs = curs.fetchall()
  rs = [r[0].strip() for r in rs]
  for hashtags in hashtagGrabber:
    if (len(hashtags) > 10):
      continue
    if (hashtags not in rs):
      curs.execute("INSERT INTO HASHTAGS VALUES (:hashtag)", {'hashtag':hashtags})  	
    statement = "INSERT INTO MENTIONS VALUES (:tid, :hashtag)"
    curs.execute(statement, {'tid':tid, 'hashtag':hashtags})
  	
  con.commit()



con = connectToDatabase()
curs = con.cursor()
