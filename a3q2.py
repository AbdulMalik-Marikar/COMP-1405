#Abdul-Malik Marikar
#101042166

#Key Reference: Gaddis, T. (2015). "Starting out with python" 3rd edition
#ord and chr reference: Built-in Functions.(2016,10,14) Retreived from https://docs.python.org/3/library/functions.html 
#ascii codes reference: ASCII Table and Description.(2016,10,14)Retreived from http://www.asciitable.com/ 

#         the 1st must be a letter between K and R excluding K including R
 #        the 2nd must be a number between 0 and 9 that is divisible by 4
  #      the 3rd must be a number between 5 and 7 excluding 5 excluding 7
   #     the 4th must be a letter between A and E excluding A excluding E
    #    the 5th must be a number between 0 and 3 excluding 0 including 3
    #    the 6th must be a number between 0 and 9 that is divisible by 4

#limiting each parameter and printing all the possibilities
for char1 in range (76,83):
	for num1 in range(0,10,4):
		for num2 in range(6,7,1):
			for char2 in range(66,69):
				for num3 in range (1,4):
					for num4 in range(0,10,4):
						print(chr(char1),num1,num2,chr(char2),num3,num4)
				