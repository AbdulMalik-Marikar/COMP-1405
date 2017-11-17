#101042166
#Abdul-Malik Marikar

#define curentyear
currentyear = 2016
#get name
name = input("What is your name?\n")
#get year
birthyear = int(input("What year were you born in?\n"))
#acount for the two possible ages in a year
birthyear2 = birthyear+1
age = currentyear-birthyear
age2 = currentyear-birthyear2

#output possible ages
print(name,"you must be between",age2,"and",age,"years old")