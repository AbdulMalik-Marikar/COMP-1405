#Abdul-Malik Marikar
#101042166

class pet:
	
	def __init__(self,name,type,age,bill):
		self.__name=name
		self__.type=type
		self.__age=age
		self.__bill=bill
		

	def growOlder(self):
		self.__age=self.__age+1
	
	def addToBill(self,add):
		self.__bill=self.__bill+add
		
def main():
	name=input("What is the name of your pet?\n")
	type=input("What type of pet do you want?\n ")
	age=int(input("How old is your pet?\n"))
	bill=0
	
	pet1=pet(name,type,age,0)	
	
	a= True		
	while a== True:
		bill=float(input("How much have you spent on your pet this year?\n"))
		pet1.__growOlder()
		pet1.__addToBill(bill)		
		exit=input("Type q to exit\n").upper()	
		
		if exit =="Q":
			break
		
main()		