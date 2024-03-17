#Create new variables named num1, num2, num2 and string1
#Populate these variables with the values 99.23, 23, 150 and "100" respectively
#Convert variables by casting them to different variable types
#Convert num1 to an integer, num2 to a float, num3 to a string and string1 to an integer
#Print these converted variables on separate lines 


import os
#Defining variables

num1 = 99.23
num2 = 23
num3 = 150
string1 = "100"

#Changing variable types
num1 = int(num1)
num2 = float(num2)
string3 = str(num3)
num4 = int(string1)

#Printing variables on separate lines using linesep
print(num1,
num2,
string3,
num4,
sep=os.linesep)
