#!/usr/bin/env python3

####################################################
#Prompt the user to enter their age.
#Also, convert this string value to an integer value.

myage = int(input("Enter you age:"))

if myage < 13:
   print("Wow! You can still buy a kid's meal!")
elif myage >= 13 and myage < 20:
   print("Wow! you are a teenager. Enjoy those french fries now!")
elif myage >= 20 and myage < 24:
   print("Welcome to the wonderful adult world. Get a Job!")
elif myage> 64:
   print("Congratualtions! You are eligiable for retirement!")
else:
  # calulate how many years the user has to work!
   i = 65 - myage
   print("Sorry! You have to work", i, "more years before retiring.")

#Outside of the IF-ELIF-ELSE block
