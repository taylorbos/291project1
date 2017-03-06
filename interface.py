import database
import os
import re
import registration


def loginProcedure(userName = None):
  os.system('clear')
  print('Logging in a user\n')
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
    userName = registration.registerProcedure() # goto register procedure
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
welcomeScreen()

