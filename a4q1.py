#Abdul-Malik Marikar
#101042166

#Key Reference: Gaddis, T. (2015). "Starting out with python" 3rd edition

#taking the string and splicing it to create a new word and printing it
def concat_slices_and_print ():
	string="gfecbhjkmsonpqrudvwxzaefghjlikmnptyqruv"
	newstring= string[9:11]+string[16]+string[21]+string[27:29]+string[33:35]
	print (newstring)
	return None

#taking the string and splicing it to create a new word when num is greaterthan or equal to 0
def if_positive_concat_slices(num):
	if num>=0:
		string="edbzyxfghjlackpqrtuonivwxyzsdefgmhjkpqr"
		newstring= string[10:13]+string[19:22]+string[27]+string[32]	
		print(newstring)
	return None

#taking the string and splicing it to create a new word but doesnt print it
def return_concat_slices():
	string="yxwvrpzquifghjlcmnoprkvwxyzesbdfghtjlmn"
	newstring= string[7:10]+string[15]+string[21]+string[27:29]+string[34]
	return newstring

def concat_arg_slices_and_return(string):	
# the if else and elif statements are checking for which string to slice and concat 
	if string=="wutsqxyzovcfghjekmnpqsrtuwxylazidghjk":
		newstring= string[8:10]+string[15]+string[22]+string[28:30]+string[31:33]		
	elif string=="tqmlkuvwxreyzpdfhjklomqtuvsiwxyzngabcd":
		newstring= string[9:11]+string[13]+string[20]+string[26:28]+string[32:34]	
	elif string=="kjhgflmpqsotwxyzuabcdfgvhjklmenpqtwirxyza":
		newstring=string[9:11]+string[16]+string[23]+string[29:31]+string[35:37]
	else:
		return None
	return newstring

#prints out the new strings based on specifications from the assignment generator
def program():
	print("Test 1 of 7:", concat_slices_and_print())
	print("Test 2 of 7:", if_positive_concat_slices(1))
	print("Test 3 of 7:", if_positive_concat_slices(-1))
	print("Test 4 of 7:", return_concat_slices())	
	print("Test 5 of 7:", concat_arg_slices_and_return("wutsqxyzovcfghjekmnpqsrtuwxylazidghjk"))
	print("Test 6 of 7:", concat_arg_slices_and_return("tqmlkuvwxreyzpdfhjklomqtuvsiwxyzngabcd"))
	print("Test 7 of 7:", concat_arg_slices_and_return("kjhgflmpqsotwxyzuabcdfgvhjklmenpqtwirxyza"))
	
program()