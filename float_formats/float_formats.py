#!/usr/bin/env python3

my_num = 1234.6789
my_pi = 3.1415926535

print("My number is:",my_num)
print("The value of pi:",my_pi)

##########################################################
# Format to 2 decial places 
# NOTE that you don't need the 0 before the .2f
##########################################################
print(format(my_num, "0.2f"), "Print using 2 decimal places")
print(format(my_num, ".2f"), "Also prints using 2 decimal places")
print("NOTE that it rounded my result!!!")
print()

#Format to the only 1 decimal place
print(format(my_num, ".1f"), "Also prints using 1 decimal places")
print("NOTE that it rounded my result!!!")

#Format PI from 10 decimal places to 6 deciaml places
print(format(my_pi, ",6f"), "Also prints using 6 decimal places")
print("NOTE that it rounded my result!!!")