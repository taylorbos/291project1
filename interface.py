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
    
  displayUserMainPage(userId) # on login success 
  
  
def displayUserMainPage(userId):
  # displays the main page for the selected user according to specs
  os.system('clear')
  print('Displaying main page for user: %s' % database.getUsername(userId))
  print('Here are some tweets and retweets from people you follow')
  info = database.getUserMainPageInfo(userId)
  for results in info:
    print(results) 
# connect to the database, oracle id and pass should be specified in file
# called connection.info
welcomeScreen()
database.closeDatabase()
