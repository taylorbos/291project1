import cx_Oracle
import os
import re

def connectToDatabase():
  f = open('connection.info')
  username = f.readline().strip()
  password = f.readline().strip()
  con = cx_Oracle.connect(username, password, "gwynne.cs.ualberta.ca:1521/CRS")	
  return con


def validateEmail():
  # uses regex to make sure email is valid
  userEmail = input('Please enter your email address: ')
  if(re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", userEmail, flags=0) is None):
    print('Entered email is not in a valid form')
    validateEmail()
  return userEmail


def registerProcedure():
  os.system('clear')
  
  print('You are now registring a new user: ')
  userName = input('Please type in your name: ')
  userEmail = validateEmail()
  userTimezone = input('Please input a timezone: ') # TODO: might want to list a bunch of timezones and the user selects one
  userPassword = input('Please create a password for the account: ')
  
  # TODO: Now we should generate a user id, and put the user into the user table
  # *****************
  # *****************
  
  return userName
  
  
def loginProcedure(userName = None):
  os.system('clear')
  
  # check if this user is in database, if not goto new login procedure
  # on login success, return the users id
  if (userName is None):
    userName = input('Please input your username: ')
  userPassword = input('Please input your password: ')
  
  # TODO: Now we must check if this user is in the database and their password is correct
  # *****************
  # *****************
  
  # TODO: this is what should be done on login failure
  #if (LOGIN_FAILURE):
    #printf('Incorrect username or password!\n')
    #loginProcedure() # on login failure
  
  return userID # on login success
  
  
def welcomeScreen():
  os.system('clear')
  
  # welcome message
  initalInput = input('Welcome to Twitter!\nMade by: Taylor Bos, Alvin Huang, Oliver Rarog\nTo login, enter your username, to register, type \'register\': ') # get username or register
  
  if (initalInput == 'register'):
    userName = registerProcedure() # goto register procedure
    userId = loginProcedure(userName) # now make user login
  else: 
    userId = loginProcedure(initalInput) # get userid 
  
  # TODO: need to pass the function the userid of the found user
  DisplayUserMainPage(userId) # on login success 
  
  
def displayUserMainPage(userId):
  # displays the main page for the selected user according to specs
  println('test\n')




# connect to the database, oracle id and pass should be specified in file
# called connection.info
con = conectToDatabase()

welcomeScreen()
