#Abdul-Malik Marikar
#101042166

#Key Reference: Gaddis, T. (2015). "Starting out with python" 3rd edition

#ask user a question to reduce the possibilities to 5 characters
character = input("Does you character have a wig? Type yes or no.\n")

#ask a question to reduce the possibilities to one character
if character == "yes":
	character2 = input("does you chracter have a scar\n")
	if character2 == "yes":
		print("Your charcter is the 3rd row, 2nd column")
else: 
	print("Don't lie to me")
