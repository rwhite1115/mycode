#!/usr/bin/env python3

#####################################################
# Prompt the user to enter number grade
# Also, convert this string value to an integer value
######################################################
mygrade = int(input("Enter you number grade:"))

if mygrade < 59:
   print("Your grade is F!")
elif mygrade >= 90 and mygrade < 100:
   print("Congrats. You got an A!")
elif mygrade >= 80 and mygrade < 89:
   print("Nice work. You got an B!")
elif mygrade >= 70 and mygrade < 79:
   print("Needs Improvement. You got a C.")
elif mygrade >= 60 and mygrade < 69:
   print("Did you study. You grade is a D.")
