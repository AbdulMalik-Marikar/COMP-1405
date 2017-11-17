def isNumeric(list):
	for x in list:
		for y in x:
			if isinstance(y,(int,float))==False:
				return False
	return True
list=[[0,1],[2,3]]		
print(isNumeric(list))