#!/usr/bin/env python3
loginfail = 0
Loginsuccess = 0
FAILIP = []
keystone_file = open('/home/student/mycode/attemptlogin/keystone.common.wsgi','r')
keystone_file_lines=keystone_file.readlines()

for i in range(len(keystone_file_lines)):
    if "-]] Authorization failed" in keystone_file_lines[i]:
     Loginsuccess += 1
print("The number of successful login attempts is " +str(Loginsuccess))

for i in range(len(keystone_file_lines)):
    if "- - - - -] Authorization failed" in keystone_file_lines[i]:    
     loginfail += 1 #this is the same as loginfail = loginfail + 1
print('The number of failed login attempts is ' + str(loginfail))

for i in range(len(keystone_file_lines)):
    if "- - - - -] Authorization failed" in keystone_file_lines[i]:
     FAILIP.append(keystone_file_lines[i])
print("The IP address associated with the failed login is") 

for x in range(len(FAILIP)):
     print(FAILIP[x].split("from", 1)[1])


       

