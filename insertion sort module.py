#Abdul-Malik Marikar
#101042166

unsorted=[1,0,3,8,9,4,5,1,2,9]

def insertionsort(unsorted):
	print(unsorted)

	for i in range (1,len(unsorted)):
		j=i
		while j>0 and unsorted[j]<unsorted[j-1]:
			unsorted[j], unsorted[j-1]= unsorted[j-1], unsorted[j]
			j=j-1
		
	return unsorted
	
print (insertionsort(unsorted))
	