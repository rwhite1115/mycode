#!/usr/bin/env python3
#Created by Robert White
#This code will pull data from a mixed list.

#Data
my_list = [ "192.168.0.5", 5060, "UP" ]

#This code will pull the first line in the list

print("The first item in the list (IP): " + my_list[0] )

#This code will pull the second line in the list

print("The second item in the list (port): " + str(my_list[1]) )

# This print will pull the last line in the list
print("The last item in the list (state): " + my_list[2] )

# New List

new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

# This prints new list in one line. 
print("When I " + new_list[5] + " into IP addresses " + new_list[3] + " or " + new_list[4] + " I am unable to ping ports " + str(new_list[0]) + new_list[1] + " or " + str(new_list[2]) )