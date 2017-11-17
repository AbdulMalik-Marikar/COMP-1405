#Abdul-Malik Marikar
#101042166

def mul (a,b):
	if a==1:
		return b
	if b==1:		 
		return b + mul(a-1,b)
	else:
		return b + mul(a-1,b)
	
print(mul(5,1))


