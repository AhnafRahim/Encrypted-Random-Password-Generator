#------------------------------------------------------------------------------------------------------
#Ahnaf Rahim
#Objective: To make a working random password generator which provides the user with a random password 
#Version 1.1: Forces at least 1 number and special character
#------------------------------------------------------------------------------------------------------
import random
import secrets

#user input for password 
while True: 
    try:
        password_length = int(input("How many characters would you like your password to be? "))
        break                      
    except ValueError:
      print("You haven't input a proper number. Please try again: ")

#printing the password
print("Your password is: " + secrets.token_urlsafe(password_length-1))

