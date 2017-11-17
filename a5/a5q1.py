#Abdul-Malik Marikar
#101042166
#Key Reference: Gaddis, T. (2015). "Starting out with python" 3rd edition

num=int(input("Enter value\n"))
def f1(num):
	#base cases
	values=[5,0,5,1,3,9]		
	if num<=5:	
		#returns the base case uptill the value inputed
		return values[num]
	#this is calculating every integer after the base case from position 6 to 11	
	elif num>5 and num<12:
		new=f1(num-6)
		new2=f1(num-4)	
		
		if new2==0:
			result=0
		else:
			result= new%new2
		return result
	#this is calculating every integer after the base case and positions 5 to eleven, and calculates
	#the integers from 12 to infinity
	elif num>=12:
		new=f1(num-8)
		new2=(num-2)
		new3=(num-5)		
		result= new+((new2)//(new3))
		return result		
		
def f2(num):
    
    if num < 0:
        return None

    else:
        list.insert(0,f1(num))
        f2(num-1)        
    return list    

list= []
print(f2(num))
        		
	
		


	