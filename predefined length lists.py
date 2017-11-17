#Abdul-Malik Marikar
#101042166

num=int(input("Enter a whole positive number\n"))
li = [-1 for i in range (num)]
print(li)

for i in range(num):
	num1=int(input("What value do you want to give this number: "))
	li.remove(-1)	
	li.insert(i,num1)
	

print(li)