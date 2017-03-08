import database
import os
import re
import registration
import login
import UserInput 
    
def welcomeScreen():
  os.system('clear')
  print()
  # welcome message
  initalInput = input('Welcome to Twitter!\nMade by: Taylor Bos, Alvin Huang, Oliver Rarog\nTo login, enter your username, %s, %s: ' % (UserInput.registerString, UserInput.exitString)) # get username or register
  if(initalInput == UserInput.exitInput):
  	os._exit(0)
  if (initalInput == UserInput.registerInput):
    registration.registerProcedure() # goto register procedure
    userId = login.loginProcedure() # now make user login
  else: 
    userId = login.loginProcedure(initalInput) # get userid 
  
  displayUserMainPage(userId) # on login success 
  
  
def displayUserMainPage(userId, currentPage=1):
  # displays the main page for the selected user according to specs
  os.system('clear')
  print('Displaying main page for user: %s' % database.getUsername(userId))
  print('Here are some tweets and retweets from people you follow')
  info = database.getUserMainPageInfo(userId)
  displayPage(info, currentPage)    
  

  userSelection = input('What would you like to do now? Please select an option:\n1. %s\n2.'
		' %s\n3. %s\n4. %s\n5. %s\n6. %s\n...' % 
		(UserInput.scrollDownString, UserInput.scrollUpString, UserInput.infoString, UserInput.replyString, UserInput.retweetString, UserInput.logoutString))

  if (userSelection == UserInput.logoutInput):
    welcomeScreen()
  if(userSelection == UserInput.scrollDownInput): 	
    displayUserMainPage(userId, currentPage+1)
  if(userSelection == UserInput.scrollUpInput): 	
    displayUserMainPage(userId, currentPage-1)
  
  
  displayUserMainPage(userId)


def displayPage(info, pageNumber):
  for i in range(pageNumber*5-5, pageNumber*5):
    if(i < 0 or i >= len(info)):
      break    
    print('%d %s' % (i+1, info[i]))


# connect to the database, oracle id and pass should be specified in file
# called connection.info
welcomeScreen()
database.closeDatabase()
