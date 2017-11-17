#Abdul-Malik Marikar
#101042166

#A number is prime if it's only divisble by 1 and itself
#Checking if  5 is prime

#5 % 2 == 0 #false
#5 % 3 == 0 #false
#5 % 4 == 0 #false

def prime ():
	n=int(input("Enter a number between 1 and 12\n"))
	for i in range (2,n,1):
		new= n%i==0
	if  new == False:
		print("Your number is prime")		
	else:
		print("Your number is not prime")
		
		
prime()

		
		
	

