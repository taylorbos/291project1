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
	statement = "SELECT USR FROM USERS WHERE USERS.NAME = '%s'" % username
	curs.execute(statement)
	rs = curs.fetchall()
	if(curs.rowcount is 0):
		return None	

	return rs

def registerUser(username, email, timezone=None, city=None, password):
	userId = 1	
	
	statment = "INSERT INTO USERS VALUES (%n, '%s', '%s', '%s', '%s', %n);" % userId, password, username, email, city, timezone
	curs.execute(statement)
	


con = connectToDatabase()
curs = con.cursor()
