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
  ids = []
  for rows in r:
    tweeterName = getUsername(rows[1])
    resultString = '%s %s At: %s' % (tweeterName, rows[3], rows[2])
    result.append(resultString)
    ids.append(rows[0])
  return result, ids

def searchUsers(keyword):
  keyword = input("Enter #hastags or words to search: ")
  statement = "SELECT DISTINCT * FROM ("
  n = 0
  sizes = ()
  args = ()

  statement = statement + "(SELECT * FROM USERS WHERE USERS.TEXT LIKE :" + str(n) + ") "

  sizes = sizes + (curs.var(cx_Oracle.FIXED_CHAR, 20),)
  args = args + ("%" + keyword + "%",)
  statement = statement + ")"
  
  curs.setinputsizes(*sizes)
  curs.execute(statement, args)
  r = curs.fetchall()
  result = []
  ids = []
  for rows in r:
    tweeterName = getUsername(rows[1])
    resultString = '%s %s At: %s' % (tweeterName, rows[3], rows[2])
    result.append(resultString)
    ids.append(rows[1])
  return result, ids


def registerTweet(userId, tweet, replyTo=None):
  getHighestId = "SELECT MAX(TID) FROM TWEETS"
  curs.execute(getHighestId)
  tid = curs.fetchone()[0]
  if(tid is None): tid = 0
  else: tid = tid + 1
  cdate = datetime.datetime.now()
  statement = "INSERT INTO TWEETS VALUES (:tid, :userid, :cdate, :text, :rplyto)"
  curs.setinputsizes(tid = int, userid = int, cdate = datetime.datetime, text = curs.var(cx_Oracle.FIXED_CHAR, 80))  
  curs.execute(statement, {'tid':tid, 'userid':userId, 'cdate':cdate, 'text':tweet, 'rplyto':replyTo})

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

def registerRetweet(userId, tweet):
  statement = "SELECT FROM RETWEETS WHERE RETWEETS.USR = :userid AND TID = :tid"
  curs.execute(statement, {'userid':userId, 'tid':tweet})
  rs = curs.fetchall()
  if(rs is not None):
    print("You have already retweeted this tweet!")
    return

  cdate = datetime.datetime.now()
  statement = "INSERT INTO RETWEETS VALUES (:userid, :tid, :cdate)"
  curs.execute(statement, {'userid':userId, 'tid':tweet, 'cdate':cdate})
  con.commit()


def getNumberRetweets(tweet):
  statement = "SELECT COUNT(*) FROM RETWEETS WHERE RETWEETS.TID = :tid"
  curs.execute(statement, {'tid':tweet})
  rs = curs.fetchall()
  if (rs is None):
    return 0
  return rs[0][0]

def getNumberReplies(tweet):
  statement = "SELECT COUNT(*) FROM TWEETS WHERE TWEETS.REPLYTO = :tid"
  curs.execute(statement, {'tid':tweet})
  rs = curs.fetchall()
  if (rs is None):
    return 0
  return rs[0][0]

def findFollowers(userId):
  curs.execute("SELECT FOLLOWS.FLWER, FOLLOWS.START_DATE FROM FOLLOWS WHERE FOLLOWS.FLWEE = :u", {'u':userId})
  r = curs.fetchall()
  result = []
  ids = []
  for rows in r:
    followerName = getUsername(rows[0])
    resultString = '%s Since: %s' % (followerName, rows[1])
    result.append(resultString)
    ids.append(rows[0])
  return result, ids

def followerInfo(Id):
  curs.execute("SELECT COUNT(*) FROM TWEETS WHERE WRITER = :u", {'u':Id})
  ntweets = curs.fetchone()[0]
  curs.execute("SELECT COUNT(*) FROM FOLLOWS WHERE FLWER = :u", {'u':Id})
  nflwees = curs.fetchone()[0]
  curs.execute("SELECT COUNT(*) FROM FOLLOWS WHERE FLWEE = :u", {'u':Id})
  nflwers = curs.fetchone()[0]
  info = "Number of tweets: %s\nNumber of users they follow: %s\nNumber of followers: %s" % (ntweets, nflwees, nflwers)
  curs.execute("SELECT TWEETS.* FROM TWEETS WHERE WRITER = :u", {'u':Id})
  t = curs.fetchall()
  tweets = []
  for rows in t:
    resultString = '%s At: %s' % (rows[3], rows[2])
    tweets.append(resultString)
  return info, tweets


def follow(flwer, flwee):
  curs.execute("SELECT * FROM FOLLOWS WHERE FLWER = :r AND FLWEE = :e", {'r':flwer, 'e':flwee})
  if curs.fetchone() is None:
    cdate = datetime.datetime.now()
    statement = "INSERT INTO FOLLOWS VALUES(:r, :e, :cdate)"
    curs.setinputsizes(r = int, e = int, cdate = datetime.datetime)
    curs.execute(statement, {'r':flwer, 'e':flwee, 'cdate':cdate})
    con.commit
    return "You are now following %s" % (getUsername(flwee))
  else:
    return "You already follow %s" % (getUsername(flwee))

def yourLists(userId):
  curs.execute("SELECT LISTS.LNAME FROM LISTS WHERE OWNER = :u", {'u':userId})
  l = curs.fetchall()
  lists = []
  for n in l:
    lists.append(n[0])
  return lists

def otherLists(userId):
  curs.execute("SELECT INCLUDES.LNAME FROM INCLUDES WHERE MEMBER = :u", {'u':userId})
  l = curs.fetchall()
  lists = []
  for n in l:
    lists.append(n[0])
  return lists

def getMembers(listName):
  statement = "SELECT INCLUDES.MEMBER FROM INCLUDES WHERE LNAME = :l"
  curs.setinputsizes(l = curs.var(cx_Oracle.FIXED_CHAR, 12))
  curs.execute(statement, {'l':listName})
  ms = curs.fetchall()
  names = []
  ids = []
  for m in ms:
    ids.append(m[0])
    names.append(getUsername(m[0]))
  return names, ids
                                                          
  
def createList(listName, userId):
  statement = "INSERT INTO LISTS VALUES (:l, :u)"
  curs.setinputsizes(l = curs.var(cx_Oracle.FIXED_CHAR, 12), u = int)
  curs.execute(statement, {'l':listName,'u':userId})
  con.commit

def deleteMember(listName, userId):
  statement = "DELETE FROM INCLUDES WHERE LNAME = :l AND MEMBER = :u"
  curs.setinputsizes(l = curs.var(cx_Oracle.FIXED_CHAR, 12), u = int)
  curs.execute(statement, {'l':listName,'u':userId})
  con.commit

def ifList(listName):
  statement = "SELECT * FROM LISTS WHERE LNAME = :l"
  curs.setinputsizes(l = curs.var(cx_Oracle.FIXED_CHAR, 12))
  curs.execute(statement, {'l':listName})
  if curs.fetchall() is None:
    return False
  else:
    return True
                                  
                                
con = connectToDatabase()
curs = con.cursor()
