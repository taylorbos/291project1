import database

def loginProcedure(userName = None):
  os.system('clear')
  print('Logging in a user\n')
  # check if this user is in database, if not goto new login procedure
  # on login success, return the users id
  if (userName is None):
    userName = input('Please input your username: ') 
  userPassword = input('Please input your password: ')
  
  userId = database.loginUser(userName, userPassword)
    
  if (userId is None):
    printf('Incorrect username or password!\n')
    loginProcedure() # on login failure
  
  return userId # on login success
