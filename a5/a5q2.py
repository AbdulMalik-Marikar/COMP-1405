#Abdul-Malik Marikar
#101042166

#Key Reference: Gaddis, T. (2015). "Starting out with python" 3rd edition

from random import randint

		
#translating the charcters the user inputs			
def translate(dictionary,word):
	for k in dictionary:
		while True:
			#if character is not in the string exit the loop
			if word.find(k)==-1:
				break
			else:
				#find the position where the character came from 
				word=place[:place.find(k)]+dictionary[x][randint(0,len(dictionary[x])-1)]+word[word.find(k)+1:]
		return word	
				
def myCount(dictionary,key):
	dictionary[key]
	x=len(dictionary[key])
	if x==0:
		return 0
	else:
		return x

def myReplace(my_dict, key, value): 

    if key.upper() in dictionary:        # If it exists
        del dictionary[key.upper()]
        dictionary[key.upper()] = value
        return True
        
    else:
        return False
	


def main():	
	dictionary={}
	file=open('your-assigned-glyphs.dat')
	data=file.read()
	file.close()
	data=data.strip(":")
	data=data.strip(";")
	data=data.split(".")
	print(data)		
	for x in range(0,len(data),2):
		if data[x][0] in dictionary:
			dictionary[data[x][1]].append(data[x][x+1])
		elif x!=0:
			list=[]
			list.append(data[x+1])
			dictionary[data[x-1][0]]=list
		else:
			list=[]
			list.append(data[x+1])
			dictionary[data[x][0]]=list
	
	y=True
	while y==True:
		choice =int(input("Would you like to quit(1),translate(2),count(3),or replace(4)\n"))
		if choice==1:
			break
		elif choice ==2:
			word=input("Enter a word to translate\n").upper()
			new=translate(dictionary,word)
			print("Your set of charcters translated to",new)
		elif choice ==3:
			key=input("Enter a letter\n").upper
			print(myCount(dictionary,key))
		elif choice==4:	
			key = input("\n\nPlease enter a key to assign a value to: ")
			value = input("\nPlease enter a value for the key: ")
			print(myReplace(my_dict, key, value))
		else:
			print("That is not a valid selction. try again\n")
		
main()









