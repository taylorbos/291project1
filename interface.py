import database
import os
import re
import registration
import login
    
def welcomeScreen():
  os.system('clear')
  
  # welcome message
  initalInput = input('Welcome to Twitter!\nMade by: Taylor Bos, Alvin Huang, Oliver Rarog\nTo login, enter your username, to register, type \'register\': ') # get username or register
  
  if (initalInput == 'register'):
    registration.registerProcedure() # goto register procedure
    userId = login.loginProcedure() # now make user login
  else: 
    userId = login.loginProcedure(initalInput) # get userid 
    
  DisplayUserMainPage(userId) # on login success 
  
  
def displayUserMainPage(userId):
  # displays the main page for the selected user according to specs
  println('test\n')

# connect to the database, oracle id and pass should be specified in file
# called connection.info
welcomeScreen()
database.closeDatabase()
