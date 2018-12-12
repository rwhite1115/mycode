#!/usr/bin/env python3
#######################################
a_list = [1,2,3,4]
b_list = [4,2,1,3]

print("List A:" ,a_list)
print("List B:" ,b_list)

print()    #This simply print an empty line(more below)

##################################
#Show that the LIST order matters 
#a_list is NOT EQUAL to b_list
##################################
if (a_list!= b_list):
    print("a_list is NOT EQUAL to b_list.")

###################################
#Modify LIST a_list
#Add the item 5 to the end of this list 
###################################

a_list.append(5)

print("The modified list using the APPEND: ",a_list)
