#!/usr/bin/env python3
# Created by RobW
#If statement, entering a host name

#Custome enters a host name
prompt_hostname= ("Please enter the hostname: ")

#Input the host name

hostname= input(prompt_hostname)

#Upper case the hostname

hostname= hostname.upper()

if hostname == "MTG":
  print("Hostname matches excepted config")
   
print("Exiting the script")