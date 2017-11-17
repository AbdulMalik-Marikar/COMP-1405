#Abdul-Malik Marikar
#101042166

#Key Reference: Gaddis, T. (2015). "Starting out with python" 3rd edition 
#---next 2 lines from Abdul Siddiqui. used to clear screen
import os
os.system("cls")

#one guntha is equal to 101.7 square meters
guntha = 101.17
#one board is equal to 0.007742 square meters
board = 0.007742

#to convert gunthas to boards
gunthavalue = int(input("How many Guntha's would you like to convert?\n"))
x= ((gunthavalue*guntha)/board)
print("")
print(gunthavalue,"Guntha's are equivalent to",x ,"Board's\n")

#to covert boards to gunthas
boardvalue = int(input("How many boards's would you like to convert?\n"))
y= ((boardvalue*board)/guntha)
print("")
print(boardvalue, "Board's are equivilent to",y ,"Guntha's\n")


