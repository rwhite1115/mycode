#!/usr/bin/env python3

#intialize your prompt string
prompt_name_msg = "Please enter your full name:"

##############################################
#Use the input function to get the user's name
##############################################
user_name = input(prompt_name_msg)

######################################################
#ERROR CHECKING: Check that the user_name is not empty
######################################################
while (user_name == ''):
	#Prompt the user again for their name
	user_name = input(prompt_name_msg)
#END of the while loop, for the USER-NAME intialization


###################################################
#Print out a statement using the user_name variable
###################################################
print()
print("Welcome to the wonderful of Python, " ,user_name)
print()
	