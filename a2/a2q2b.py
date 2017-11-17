#Abdul-Malik Marikar
#101042166

#Key Reference: Gaddis, T. (2015). "Starting out with python" 3rd edition 

#this will spilt up the symbols
directions=int(input("How many directions do the arrows in your symbol point in?\n"))

#using the remaining symbols the program will ask questions for each parameter
if directions > 1:
	print("Your symbol is in the second row and third column")
elif directions == 1:
	#this will ask questions based on the direction of the arrows in the symbol
	direction=input("Which direction does your symbol point in. Type the direction\n").lower()
	if direction =="left":
		parts=int(input("How many parts are in your symbol?\n"))
		if parts == 2:
			print("Your symbol is in the first row fourth column")
		elif parts == 1:
			curve=input("Is your symbol straight or curved?\n").lower()
			if curve =="curved":
				print("Your symbol is in the first row and third column")
			elif curve == "straight":
				print("Your symbol is in the first row first column")
	elif direction =="right":
		parts2=int(input("How many parts are in your symbol?\n"))
		if parts2 == 2:
			print("Your symbol is in the first row and second column")
		elif parts2 == 1:
			curve2=input("Is your symbol straight or curved?\n").lower() 
			if curve2== "curved":
				print("Your symbol is in the second row and fifth column")
			elif curve2 == "straight":
				print("Your symbol is in the second row fourth column")
	elif direction =="down":
		parts3 = int(input("How many parts are in your symbol?\n"))
		if parts3 >1:
			print("Your symbol is in the first row and fifth column")
		elif parts3 ==1:
			print ("Your symbol is in the second row and first column")
	elif direction =="up":
		print("Your symbol is in the second row and second column")
	
			