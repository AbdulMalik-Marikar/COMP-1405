#Abdul-Malik Marikar
#101042166

dictionary = {
'A': '.-',     
'B': '-...',
'C': '-.-.', 
'D': '-..',    
'E': '.',      
'F': '..-.',
'G': '--.',    
'H': '....',   
'I': '..',
'J': '.---',   
'K': '-.-',    
'L': '.-..',
'M': '--',     
'N': '-.',     
'O': '---',
'P': '.--.',   
'Q': '--.-',  
'R': '.-.',
'S': '...',    
'T': '-',      
'U': '..-',
'V': '...-',   
'W': '.--',    
'X': '-..-',
'Y': '-.--',   
'Z': '--..',}

def translate(message):
	new=len(message)
	if new == 1:
		return dictionary[message]
	else:
		return dictionary[message[0]] + dictionary[message[1:new]]
		

#def reverse(morse):	
#	news = list(morse)
#	word=[]
#	string=""
#	for x in range (len(news)):
#		if news[x] in dictionary:
#			string+=dictionary[news[x]]
#	return string
	
message=input("Enter a word or sentence\n")

print(translate(message))