def isRectangular (list):
	x=len(list[0])
	for y in list:	
		if len(y)!=x:
			return False
	return True		

list=[[1,2,3], [4,5,6], [7,8,9]]	
print(isRectangular(list))
	
	
	