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
  
  os.system('clear')
  displayUserMainPage(userId) # on login success 
  
  
def displayUserMainPage(userId, currentPage=1):
  # displays the main page for the selected user according to specs
  print('Displaying main page for user: %s' % database.getUsername(userId))
  print('Here are some tweets and retweets from people you follow')
  info, ids = database.getUserMainPageInfo(userId)
  displayPage(info, currentPage)    
  userSelection = input('What would you like to do now? Please select an option:\n1. %s\n2.'
		' %s\n3. %s\n4. %s\n5. %s\n6. %s\n7. %s\n8. %s\n9. %s\n10. %s\n...' % 
		        (UserInput.scrollDownString, UserInput.scrollUpString, UserInput.tweetString, UserInput.infoString, UserInput.replyString, UserInput.retweetString, UserInput.searchString, UserInput.userString, UserInput.followersString, UserInput.logoutString))

  if (userSelection == UserInput.logoutInput):
    welcomeScreen()
  elif(userSelection == UserInput.scrollDownInput): 	
    displayUserMainPage(userId, currentPage+1)
  elif(userSelection == UserInput.scrollUpInput): 	
    displayUserMainPage(userId, currentPage-1)
  elif(userSelection == UserInput.tweetInput):
    composeTweet(userId)
  elif(userSelection == UserInput.replyInput):
    while(True):
      selection = input('What tweet would you like to reply to? ')
      if(int(selection) < 1 or int(selection) > currentPage*5 or int(selection) > len(ids)):
        print('Selection out of bounds!')
        continue
      else: composeTweet(userId, ids[int(selection)-1])
      break
  elif(userSelection == UserInput.searchInput):
    searchScreen(userId)
  elif(userSelection == UserInput.userInput):
    userScreen(userId)
  elif(userSelection == UserInput.followersInput):
    listFollowers(userId)
  elif(userSelection == UserInput.infoInput):   
    while(True):
      selection = input('What tweet would you like to know about? ')
      if(int(selection) < 1 or int(selection) > currentPage*5 or int(selection) > len(ids)):
        print('Selection out of bounds!')
        continue
      else: displayMoreInfo(ids[int(selection)-1])
      break
  
  
  displayUserMainPage(userId)


def displayMoreInfo(tweet):
	print('\nThis tweet has been retweeted %i times and replied to %i times\n' % (database.getNumberRetweets(tweet), database.getNumberReplies(tweet)))  	

def composeTweet(userId, replyTo=None):
  os.system('clear')
  print('You are now composing a tweet, type your tweet on the next line, there is a maximum of 80 characters')
  tweet = input('...')
  if (len(tweet) > 80):
    print('Tweet is too long!')
    composeTweet(userId, replyTo)
  database.registerTweet(userId, tweet, replyTo)


def displayPage(info, pageNumber):
  for i in range(pageNumber*5-5, pageNumber*5):
    if(i < 0 or i >= len(info)):
      break    
    print('%d %s' % (i+1, info[i]))

def searchScreen(userId):
  os.system('clear')
  keywords = input("Enter #hashtags or words you would like to search: ")
  keywordslist = keywords.split()
  r, ids = database.searchTweets(keywordslist)
  displaySearch(userId, 1, r, keywords, ids)
  #if r == []:
   # print("No search results")
  #else:
   # displayPage(r, currentPage)



def displaySearch(userId, currentPage, r, keywords, ids):
  os.system('clear')
  print("Keywords: %s" %keywords)
  if r == []:
    print("No search results")
  else:
    displayPage(r, currentPage)
  userSelection = input("What would you like to do now? Please select an option:\n1. %s\n2. %s\n3. %s\n4. %s\n5. %s\n6. %s\n..."
                        % (UserInput.scrollDownString, UserInput.scrollUpString, UserInput.infoString, UserInput.replyString, UserInput.retweetString, UserInput.mainPageString))
  if (userSelection ==  UserInput.scrollDownInput):
    displaySearch(userId, currentPage+1, r, keywords, ids)
  if (userSelection == UserInput.scrollUpInput):
    displaySearch(userId, currentPage-1, r, keywords, ids)
  if (userSelection == UserInput.mainPageInput):
    displayUserMainPage(userId, 1)
  #TODO: handle info, reply, retweet

  displaySearch(userId, 1, r, keywords, ids)


def userScreen(userId):
  os.system('clear')
  keyword = input("Enter the user or city you would like to search: ")
  r, ids = database.searchTweets(keyword)
  displayUserSearch(userId, 1, r, keyword, ids)
  #if r == []:
   # print("No search results")
  #else:
   # displayPage(r, currentPage)

def displayUserSearch(userId, currentPage, r, keyword, ids):
  os.system('clear')
  print("Keyword: %s" %keyword)
  if r == []:
    print("No search results")
  else:
    displayPage(r, currentPage)
  userSelection = input("What would you like to do now? Please select an option:\n1. %s\n2. %s\n3. %s\n4. %s\n..."
                        % (UserInput.scrollDownString, UserInput.scrollUpString, UserInput.infoString, UserInput.mainPageString))
  if (userSelection ==  UserInput.scrollDownInput):
    displaySearch(userId, currentPage+1, r, keywords, ids)
  if (userSelection == UserInput.scrollUpInput):
    displaySearch(userId, currentPage-1, r, keywords, ids)
  if (userSelection == UserInput.mainPageInput):
    displayUserMainPage(userId, 1)
  #TODO: handle info

  displaySearch(userId, 1, r, keyword, ids)



def isInt(s):
  try:
    int(s)
    return True
  except ValueError:
    return False
#stackoverflow.com/questions/1265665/python-check-if-a-string-represents-an-int-without-using-try-except

def listFollowers(userId):
  r, ids = database.findFollowers(userId)
  displayFollowers(userId, 1, r, ids)

def displayFollowers(userId, currentPage, r, ids):
  os.system('clear')
  if r == []:
    print("No followers")
  else:
    print("Your followers:")
    displayPage(r, currentPage)
  userSelection = input("What would you like to do now? Please select an option :\n1. %s\n2. %s\n3. %s\n4. %s\n..."
                        % (UserInput.scrollDownString, UserInput.scrollUpString, UserInput.followerInfoString, UserInput.mainPageString))
  if (userSelection == UserInput.scrollDownInput):
    displayFollowers(userId, currentPage+1, r, ids)
  if (userSelection == UserInput.scrollUpInput):
    displayFollowers(userId, currentPage-1, r, ids)
  if (userSelection == UserInput.mainPageInput):
    displayUserMainPage(userId, 1)
  if (userSelection == UserInput.followerInfoInput):
    while(True):
      selection = input("Which follower (by number) would you like to know about? ")
      if isInt is False:
        print("Please input a number")
        continue
      elif(int(selection) <= (currentPage*5)-5  or int(selection) > currentPage*5 or int(selection) > len(r)):
        print("Selection out of bounds")
        continue
      else:
        os.system('clear')
        displayFollowersInfo(userId, ids[int(selection)-1], 0)
      break
  displayFollowers(userId, currentPage, r, ids)

def displayFollowersInfo(userId, followerId, currentPage):
  info, tweets = database.followerInfo(followerId)
  print(info)
  if tweets == []:
    print("This user has no tweets")
  else:
    print("Tweets:")
    if currentPage == 0:
      for i in range(0, 3):
        if (i < len(tweets)):
          print('%d %s' % (i+1, tweets[1]))
    else:
      displayPage(tweets, currentPage)
  if currentPage == 0:
    userSelection = input("What would you like to do now? Please select an option:\n1. To show more tweets, type \'more\'\n2. %s\n3. %s\n..."
                          % (UserInput.followString, UserInput.backString))
  else:
    userSelection = input("What would you like to do now? Please select an option:\n1. %s\n2. %s\n3. %s\n4. %s\n..."
                          % (UserInput.scrollDownString, UserInput.scrollUpString, UserInput.followString, UserInput.backString))
  if (userSelection == 'more'):
    os.system('clear')
    displayFollowersInfo(userId, followerId, currentPage+1)
  if (userSelection == UserInput.scrollDownInput):
    os.system('clear')
    displayFollowersInfo(userId, followerId, currentPage+1)
  if (userSelection == UserInput.scrollUpInput):
    os.system('clear')
    displayFollowersInfo(userId, followerId, currentPage+1)
  if (userSelection == UserInput.backInput):
    listFollowers(userId)
  if (userSelection == UserInput.followInput):
    os.system('clear')
    f = database.follow(userId, followerId)
    print(f)
    displayFollowersInfo(userId, followerId, currentPage)
  os.system('clear')
  displayFollowersInfo(userId, followerId, currentPage)
 

# connect to the database, oracle id and pass should be specified in file
# called connection.info
welcomeScreen()
database.closeDatabase()


