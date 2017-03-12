import database
import os

def loginProcedure(userName = None):
  print('\nLogging in a user\n')
  # check if this user is in database, if not goto new login procedure
  # on login success, return the users id
  if (userName is None):
    userName = input('Please input your username: ') 
  userPassword = input('Please input your password: ')
  
  userId = database.loginUser(userName, userPassword)
    
  if (userId is None):
    print('Incorrect username or password!')
    userId = loginProcedure() # on login failure
  
  return userId # on login success
