#Abdul-Malik Marikar
#101042166

#Key Reference: Starting out with python 3rd edition
#---next 2 lines from Abdul Siddiqui. used to clear screen
import os
os.system("cls")

#one guntha is equal to 101.7 square meters
guntha = 101.17
#one board is equal to 0.007742 square meters
board = 0.007742

#function concept from generator-for-A1.py
#printing selection menu
def startscreen():    
	print("Select an option from below")
	print("")
	print("Type 1 to convert Guntha's to Board's")
	print ("Type 2 to convert Board's to Guntha's")
	print ("Type 3 to Quit")
	
#Taking the values inputed by the user and converting it	
def selections():

    #user inputs values here
	selectionvalue = int(input(">>>>"))
	
	#enters the corresponding selection when the correct value is inputed
	if selectionvalue == 1:
		#to convert gunthas to boards
		gunthavalue = int(input("How many Guntha's would you like to convert?\n"))
		x= ((gunthavalue*guntha)/board)
		print("")
		print(gunthavalue,"Guntha's are equivalent to",x ,"Board's\n")
	 
	else:
		#enters the corresponding selection when the correct value is inputed
		if selectionvalue == 2:
			#to covert boards to gunthas
			boardvalue = int(input("How many boards's would you like to convert?\n"))
			y= ((boardvalue*board)/guntha)
			print("")
			print(boardvalue, "Board's are equivilent to",y ,"Guntha's\n")
		
		#This is used to exit the program
		else:
			if selectionvalue == 3:
				os.system("cls")
				return
	

#create a variable to control the loop
again = 'y'

#the actual program with a while loop so the user can convert more than once
while again == 'y':
	startscreen()
	selections()	
	#built in loop with an exit
	print("Do you want to calculate again? Type 'y' for yes and 'n' for no\n")
	again=input(">>>>")
	os.system("cls")



