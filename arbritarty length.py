#Abdul-Malik Marikar
#101042166

li=[]

for i in li:
	print("do you want to add a value, remove a value, or exit")
	choice=input("type a to add,r to remove and e to exit\n").upper()
	if choice =="A":
		add=int(input("enter a value you would like to insert\n"))
		li.insert(i,add)
	elif choice=="R":
		li.pop()
	elif choice =="E":
			print(li)
			print("Theis is the list you created")
		
	
	