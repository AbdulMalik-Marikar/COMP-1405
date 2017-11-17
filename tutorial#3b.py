#101042166
#Abdul-Malik Marikar

#get number of days
elapsedtime =int(input("How many days would you like to covert?\n"))

#calculate amount of years
year = elapsedtime//365

#use remainder to calculate months
remainder = (elapsedtime%365)
month = remainder//30

#use remainder of months to calculate weeks
remainder2 = (remainder%30)
week = remainder2//7

#use the remainder as days
days = remainder2%7

#output the covertion
print(elapsedtime,"days is",year,"year(s),",month,"month(s),",week,"week(s), and",days," days")