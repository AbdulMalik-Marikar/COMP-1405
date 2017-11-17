def isMatrix(list):
	if isNumeric(list)==True and isRectangular(list)==True:
		return True
	else:
		return False

def isNumeric(list):
	for x in list:
		for y in x:
			if isinstance(y,(int,float))==False:
				return False
	return True
	
def isRectangular (list):
	x=len(list[0])
	for y in list:	
		if len(y)!=x:
			return False
	return True		



list=[[1,2,3], [4,5,6], [7,8,9]]
print(isMatrix(list))