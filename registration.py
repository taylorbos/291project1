import os
import re
import database

def registerEmail():
  # uses regex to make sure email is valid
  userEmail = input('Please enter your email address, maximum of 15 characters: ')
  if(re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", userEmail, flags=0) is None):
    print('Entered email is not in a valid form')
    registerEmail()
  if (len(userEmail) > 15):
  	print('Entered email is too long')
  	registerEmail()
  return userEmail


def registerUsername():
	userName = input('Please type in your name, maximum of 20 characters: ')
	if (len(userName) > 20):
		print('Name is too long')
		registerUsername()
	
	if (database.getUserid(userName) is not None):
		print('Username already taken\n')
		registerUsername()
	return userName


# TODO: maybe add a list of timezones that the user can select
def registerTimezone():
	userTimezone = input('Please enter a timezone: ')
	return userTimezone	
	
	
def registerCity():
	userCity = input('Please enter a city, maximum of 12 characters: ')
	if (len(userCity) > 12):
		print('City name is too long\n')
		registerCity()
	return userCity	
	

def registerPassword():
	userPassword = input('Please enter a password, maximum of 4 characters: ')
	if (len(userPassword) > 4):
		print('Password is too long')
		registerPassword()
	return userPassword	
	
	
def registerProcedure():
  os.system('clear')
  
  print('You are now registring a new user: ')
  userName = registerUsername()
  userEmail = registerEmail()
  userTimezone = registerTimezone() # TODO: might want to list a bunch of timezones and the user selects one
  userCity = registerCity()
  userPassword = registerPassword()
  database.registerUser(userName, userEmail, userPassword, userTimezone, userCity)
  
  # TODO: make sure that we successfully added
  print('Registration complete!')

