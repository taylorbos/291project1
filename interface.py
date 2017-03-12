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
  info, ids = database.getUserMainPageInfo(userId)
  displayPage(info, currentPage)    
  userSelection = input('What would you like to do now? Please select an option:\n1. %s\n2.'
		' %s\n3. %s\n4. %s\n5. %s\n6. %s\n7. %s\n8. %s\n...' % 
		        (UserInput.scrollDownString, UserInput.scrollUpString, UserInput.tweetString, UserInput.infoString, UserInput.replyString, UserInput.retweetString, UserInput.searchString, UserInput.logoutString))

  if (userSelection == UserInput.logoutInput):
    welcomeScreen()
  elif(userSelection == UserInput.scrollDownInput): 	
    displayUserMainPage(userId, currentPage+1)
  elif(userSelection == UserInput.scrollUpInput): 	
    displayUserMainPage(userId, currentPage-1)
  elif(userSelection == UserInput.tweetInput):
  	 composeTweet(userId)
  elif(userSelection == UserInput.searchInput):
    searchScreen(userId)
  elif(userSelection == UserInput.infoInput):
	#TODO: make sure the user types a number, so cast can work    
    while(True):
      selection = input('What tweet would you like to know about? ')
      if(int(selection) < 1 or int(selection) > currentPage*5 or int(selection) > len(ids)):
        print('Selection out of bounds!')
        continue
      else: displayMoreInfo(ids[int(selection)-1])
      break
  
  
  displayUserMainPage(userId)


def displayMoreInfo(tweet):
	print('This tweet has been retweeted %i times and replied to %i times' % (database.getNumberRetweets(tweet), database.getNumberReplies(tweet)))  	

def composeTweet(userId):
	os.system('clear')
	print('You are now composing a tweet, type your tweet on the next line, there is a maximum of 80 characters')
	tweet = input('...')
	if (len(tweet) > 80):
		print('Tweet is too long!')
	database.registerTweet(userId, tweet)


def displayPage(info, pageNumber):
  for i in range(pageNumber*5-5, pageNumber*5):
    if(i < 0 or i >= len(info)):
      break    
    print('%d %s' % (i+1, info[i]))

def searchScreen(userId):
  os.system('clear')
  keywords = input("Enter #hashtags or words you would like to search: ").split()
  r = database.searchTweets(keywords)
  displaySearch(userId, 1, r)
  #if r == []:
   # print("No search results")
  #else:
   # displayPage(r, currentPage)

def displaySearch(userId, currentPage, r):
  if r == []:
    print("No search results")
  else:
    displayPage(r, currentPage)
  userSelection = input("What would you like to do now? Please select an option:\n1. %s\n2. %s\n3. %s\n4. %s\n5. %s\n6. %s\n..."
                        % (UserInput.scrollDownString, UserInput.scrollUpString, UserInput.infoString, UserInput.replyString, UserInput.retweetString, UserInput.mainPageString))
  if (userSelection ==  UserInput.scrollDownInput):
    displaySearch(userId, currentPage+1, r)
  if (userSelection == UserInput.scrollUpInput):
    displaySearch(userId, currentPage-1, r)
  if (userSelection == UserInput.mainPageInput):
    displayUserMainPage(userId, 1)

  displaySearch(userId, 1, r)

# connect to the database, oracle id and pass should be specified in file
# called connection.info
welcomeScreen()
database.closeDatabase()


