#Abdul-Malik Marikar
#101042166

class pet:
	
	def __init__(self,name,type,age,bill):
		self.__name=name
		self.__type=type
		self.__age=age
		self.__bill=bill

	def getName(self):
		return self.__name
		
	def setName(self, name):
		self.__name=name
		
	def getType(self):
		return self.__type
		
	def setType(self,type):
		if type in ("CAT","DOG","BIRD"):
			self.__type=type
			
	def getAge(self):
		return self.age
		
	def getBill(self):
		return self.bill

	def growOlder(self):
		self.__age=self.__age+1
	
	def addToBill(self,add):
		self.__bill=self.__bill+add
		
def main():
	name=input("What is the name of your pet?\n").upper()
	type=input("What type of pet do you want?\n ").upper()
	age=int(input("How old is your pet?\n"))
	bill=0
	
	pet1=pet(name,type,age,0)	
	
	a= True		
	while a== True:
		bill=float(input("How much have you spent on your pet this year?\n"))
		pet1.growOlder()
		pet1.addToBill(bill)		
		exit=input("Type q to exit\n").upper()	
		
		if exit =="Q":
			break
		
main()		