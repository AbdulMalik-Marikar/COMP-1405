#Abdul-Malik Marikar
#101042166

#Key Reference: Gaddis, T. (2015). "Starting out with python" 3rd edition 

#ask various questions so the program can determine the correct symbol
print("Choose one of the symbols and I'll try to guess it buy asking you multiple questions")

#the questions being asked
faceleft = input("Does your symbol face left (not diagonally)? Type yes or no.\n").lower()
faceright = input("Does your symbol face right? (not diagonally) Type yes or no.\n").lower()
curve = input("Does your symbol have a curve (not a turn)? Type yes or no.\n").lower()
facedown= input("Does your symbol face down? Type yes or no.\n").lower()
turn= input("Does your symbol have a turn (not a curve)? Type yes or no.\n").lower()
faceup= input ("Does your symbol point up? Type yes or no.\n").lower()
peices= input ("Does your symbol have more than one peice Type yes or no.\n").lower()
diagonal1=input ("Does your symbol have a diagonal pointing left? Type yes or no.\n").lower()
diagonal2= input("Does your symbol have a diagonal pointing right? Type yes or no.\n").lower()


#the program filtering out the correct symbol by using the information by using the yes and no questions provided by the user
if faceleft== "yes" and not(curve =="yes")and not (facedown== "yes") and not (faceup== "yes") and not (faceright== "yes"):
	print("Your symbol is in the first row and first column")
elif diagonal1== "yes" and turn== "yes" and peices== "yes" and not(diagonal2== "yes"):
	print("Your symbol is in the first row and Fourth 4column")
elif faceleft== "yes" and curve =="yes" and not (facedown== "yes")and not (faceup== "yes") and not (faceright== "yes"):
	print("Your symbol is in the first row and third column")
elif turn== "yes" and peices== "yes" and diagonal2== "yes":
	print("Your symbol is in the first row and second column")
elif facedown=="yes" and peices =="yes"and not (faceup== "yes") and not (faceright== "yes")and not (faceleft== "yes"): 
	print("Your symbol is in the first row and fifth column")
elif facedown=="yes"and turn=="yes"and not(peices =="yes"):
	print("Your symbol is the second row first column")
elif faceup== "yes" and turn=="yes":
	print("Your symbol is in the second row second column")
elif faceleft== "yes" and facedown== "yes" and faceup== "yes" and faceright== "yes":
	print("Your symbol is in the second row third column")
elif faceright== "yes" and not (curve=="yes"):
	print("Your symbol is in the second row fourth column")
elif faceright =="yes" and curve=="yes":
	print("Your symbol is in the second row fifth column")