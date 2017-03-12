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
  
  
def displayUserMainPage(userId, currentPage=1, clear=True):
  # displays the main page for the selected user according to specs
  info, ids = database.getUserMainPageInfo(userId)
  displayPage(info, currentPage, clear)
  print('Displaying main page for user: %s' % database.getUsername(userId))
  print('Here are some tweets and retweets from people you follow')    
  # This provides the user with options on what to do
  userSelection = input('What would you like to do now? Please select an option:\n1. %s\n2.'
		' %s\n3. %s\n4. %s\n5. %s\n6. %s\n7. %s\n8. %s\n9. %s\n10. %s\n11. %s\n...' % 
		        (UserInput.scrollDownString, UserInput.scrollUpString, UserInput.tweetString, UserInput.infoString, UserInput.replyString, UserInput.retweetString, UserInput.searchString, UserInput.userString, UserInput.followersString, UserInput.manageListsString, UserInput.logoutString))

  if (userSelection == UserInput.logoutInput):
    welcomeScreen() # user wants to logout, go to welcome screen
  elif(userSelection == UserInput.scrollDownInput): 	
   if(currentPage+1 <= len(info)/5):  displayUserMainPage(userId, currentPage+1) # scroll page down
  elif(userSelection == UserInput.scrollUpInput): 	
    if(currentPage-1 > 0): displayUserMainPage(userId, currentPage-1) # scroll page up
  elif(userSelection == UserInput.tweetInput):
    composeTweet(userId) # goto tweet creation screen
  elif(userSelection == UserInput.replyInput):
    # allows user to select a tweet from a list, then reply to it
    while(True):
      selection = input('What tweet would you like to reply to? ')
      if(selection.isdigit() is False):
        print("Please enter a number only")
        continue
      if(int(selection) < 1 or int(selection) > currentPage*5 or int(selection) > len(ids) or int(selection) < (currentPage*5-5)):
        print('Selection out of bounds!')
        continue
      
      else: composeTweet(userId, ids[int(selection)-1])
      break
  elif(userSelection == UserInput.retweetInput):
    # user selects tweet to retweet
    while(True):
      selection = input('What tweet would you like to retweet? ')
      if(selection.isdigit() is False):
        print("Please enter a number only")
        continue
      if(int(selection) < 1 or int(selection) > currentPage*5 or int(selection) > len(ids) or int(selection) < (currentPage*5-5)):
        print('Selection out of bounds!')
        continue
      else: database.registerRetweet(userId, ids[int(selection)-1])
      break
  elif(userSelection == UserInput.searchInput):
    searchScreen(userId) # goes to search menu
  elif(userSelection == UserInput.manageListsInput):
    manageLists(userId) # goes to list manager menu
  elif(userSelection == UserInput.userInput):
    userScreen(userId) # goes to user select menu
  elif(userSelection == UserInput.followersInput):
    listFollowers(userId) # lists followers
  elif(userSelection == UserInput.infoInput):   
    # user can select a tweet to get more info
    while(True):
      selection = input('What tweet would you like to know about? ')
      if(selection.isdigit() is False):
        print("Please enter a number only")
        continue
      if(int(selection) < 1 or int(selection) > currentPage*5 or int(selection) > len(ids) or int(selection) < (currentPage*5-5)):
        print('Selection out of bounds!')
        continue
      else: displayMoreInfo(ids[int(selection)-1])
      clear = False;
      break
      
  
  # keep displaying the main page
  displayUserMainPage(userId, currentPage, clear)


def displayMoreInfo(tweet):
  os.system('clear')
  # gets the info about the tweet
  print('\nThis tweet has been retweeted %i times and replied to %i times\n' % (database.getNumberRetweets(tweet), database.getNumberReplies(tweet)))  	

def composeTweet(userId, replyTo=None):
  os.system('clear')
  print('You are now composing a tweet, type your tweet on the next line, there is a maximum of 80 characters')
  tweet = input('...')
  if (len(tweet) > 80):
    print('Tweet is too long!')
    composeTweet(userId, replyTo)
  database.registerTweet(userId, tweet, replyTo)



def displayPage(info, pageNumber, clear=True):
  if(clear): os.system('clear')
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



def displaySearch(userId, currentPage, r, keywords, ids, clear=True):
  if(clear): os.system('clear')
  print("Keywords: %s" %keywords)
  if r == []:
    print("No search results")
  else:
    displayPage(r, currentPage, clear)
  userSelection = input("What would you like to do now? Please select an option:\n1. %s\n2. %s\n3. %s\n4. %s\n5. %s\n6. %s\n..."
                        % (UserInput.scrollDownString, UserInput.scrollUpString, UserInput.infoString, UserInput.replyString, UserInput.retweetString, UserInput.mainPageString))
  if (userSelection ==  UserInput.scrollDownInput):
    displaySearch(userId, currentPage+1, r, keywords, ids)
  if (userSelection == UserInput.scrollUpInput):
    displaySearch(userId, currentPage-1, r, keywords, ids)
  if (userSelection == UserInput.mainPageInput):
    displayUserMainPage(userId, 1)
  #TODO: handle info, reply, retweet
  elif(userSelection == UserInput.replyInput):
    while(True):
      selection = input('What tweet would you like to reply to? ')
      if(int(selection) < 1 or int(selection) > currentPage*5 or int(selection) > len(ids) or int(selection) < (currentPage*5-5)):
        print('Selection out of bounds!')
        continue
      else: composeTweet(userId, ids[int(selection)-1])
      break
  elif(userSelection == UserInput.retweetInput):
    while(True):
      selection = input('What tweet would you like to retweet? ')
      if(int(selection) < 1 or int(selection) > currentPage*5 or int(selection) > len(ids) or int(selection) < (currentPage*5-5)):
        print('Selection out of bounds!')
        continue
      else: database.registerRetweet(userId, ids[int(selection)-1])
      break
  elif(userSelection == UserInput.infoInput):   
    while(True):
      selection = input('What tweet would you like to know about? ')
      if(int(selection) < 1 or int(selection) > currentPage*5 or int(selection) > len(ids) or int(selection) < (currentPage*5-5)):
        print('Selection out of bounds!')
        continue
      else: displayMoreInfo(ids[int(selection)-1])
      clear = False
      break
      
  displaySearch(userId, 1, r, keywords, ids, clear)


def userScreen(userId):
  os.system('clear')
  keyword = input("Enter the user or city you would like to search: ")
  r, ids = database.searchUsers(keyword)
  database.searchUsers(keyword)
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
                        % (UserInput.scrollDownString, UserInput.scrollUpString, UserInput.userInfoString, UserInput.mainPageString))
  if (userSelection == UserInput.scrollDownInput):
    displayUserSearch(userId, currentPage+1, r, keyword, ids)
  elif (userSelection == UserInput.scrollUpInput):
    displayUserSearch(userId, currentPage-1, r, keyword, ids)
  elif (userSelection == UserInput.mainPageInput):
    displayUserMainPage(userId, 1)
  elif (userSelection == UserInput.infoInput):
    while(True):
      selection = input("Which user (by number) would you like to know about? ")
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

  displayUserSearch(userId, 1, r, keyword, ids)



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
      if isInt(selection) is False:
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
          print('%d %s' % (i+1, tweets[i]))
    else:
      displayPage(tweets, currentPage)
  if currentPage == 0:
    userSelection = input("What would you like to do now? Please  select an option:\n1. To show more tweets, type \'more\'\n2. %s\n3. %s\n4. Add user to a list, \'list\'\n..."
                          % (UserInput.followString, UserInput.backString))
  else:
    userSelection = input("What would you like to do now? Please select an option:\n1. %s\n2. %s\n3. %s\n4. %s\n5. Add user to a list, type \'list\'\n..."
                          % (UserInput.scrollDownString, UserInput.scrollUpString, UserInput.followString, UserInput.backString))



  if (userSelection == 'more'):
    os.system('clear')
    displayFollowersInfo(userId, followerId, currentPage+1)
  if (userSelection == 'list'):
    os.system('clear')
    ln = input("Which list would you like to add to? ")
    if database.ifList(ln):
      f = database.addMember(ln, followerId, userId)
      print(f)
    displayFollowersInfo(userId, followerId, currentPage)
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
 
def manageLists(userId):
  os.system('clear')
  userSelection = input("What would you like to do? Please select an option:\n1. %s\n2. %s\n3. %s\n4. %s\n..."
                        % (UserInput.yourListsString, UserInput.otherListsString, UserInput.createListString, UserInput.backString))
  if (userSelection == UserInput.backInput):
    displayUserMainPage(userId, 1)
  elif (userSelection == UserInput.yourListsInput):
    displayYourLists(userId)
  elif (userSelection == UserInput.otherListsInput):
    displayOtherLists(userId)
  elif (userSelection == UserInput.createListInput):
    createList(userId)
  else:
    manageLists(userId)
              
def createList(userId):
  listName = input('Choose a name for your list (max 12 characters)\n or type \'back\' to go back\n ')
  if (listName == 'back'):
    manageLists(userId)
  elif len(listName) > 12:
    print("Name too long")
    listName = createList(userId)
  else:
    if database.ifList(listName) is True:
      print("list already exists")
      listName = createList(userId)

    else:
      database.createList(listName, userId)
                    
def displayYourLists(userId):
  os.system('clear')
  lists = database.yourLists(userId)
  if lists == []:
    print("You have no lists")
  else:
    for lst in lists:
      print(lst)
  userSelection = input("What would you like to do? Please select an option:\n1. %s\n2. %s\n..." % (UserInput.listMembersString,UserInput.backString))
  if (userSelection == UserInput.listMembersInput):
    memberList(userId)
  if (userSelection == UserInput.backInput):
    manageLists(userId)
  else:
    displayYourLists(userId)
                                        
def displayOtherLists(userId):
  os.system('clear')
  lists = database.otherLists(userId)
  if lists == []:
    print("You are in no lists")
  else:
    for lst in lists:
      print(lst)
  userSelection = input('To go back type \'back\'\n')
  if (userSelection == 'back'):
    manageLists(userId)
  displayOtherLists(userId)
                                  
def memberList(userId):
  userSelection = input("Which list would you like to see the members of? ")
  if (database.ifList(userSelection)):
    memberNames, memberIds = database.getMembers(userSelection)
    displayMembers(userId, userSelection, memberNames, memberIds, 1)
  else:
    print("That is not a list that you own.")
    uinput = input('If you would like to try again type \'again\'\nElse you can type \'back\' to go back\n...')
    if (uinput == 'again'):
      memberList(userId)
    else:
      displayYourLists(userId)

def displayMembers(userId, listName, memberNames, memberIds, currentPage):
  os.system('clear')
  print("Members of list %s" %listName)
  if memberNames == []:
    print("No members in this list")
  else:
    displayPage(memberNames, currentPage)
  userSelection = input('If you would like to delete a member type \'delete\'\nElse type \'back\' to go back\n%s\n%s\n' % (UserInput.scrollDownString, UserInput.scrollUpString))
  if (userSelection == UserInput.scrollDownInput):
    displayMembers(userId, listName, memberNames, memberIds, currentPage+1)
  if (userSelection == UserInput.scrollUpInput):
    displayMembers(userId, listName, memberNames, memberIds, currentPage-1)
  if (userSelection == 'back'):
    displayYourLists(userId)
  if (userSelection == 'delete'):
    while(True):
      selection = input("Which member (by number) would you like to delete? ")
      if isInt(selection) is False:
        print("Please input a number")
        continue
      elif (int(selection) <= (currentPage*5)-5 or int(selection) > currentPage*5 or int(selection) > len(memberIds)):
        print("Selection out of bounds")
        continue
      else:
        print("User has been deleted")
        database.deleteMember(listName, memberIds[int(selection)-1])
      break
  displayMembers(userId, listName, memberNames, memberIds, currentPage)
                                                                                      
                                                                
# connect to the database, oracle id and pass should be specified in file
# called connection.info
welcomeScreen()
database.closeDatabase()



