#Abdul-Malik Marikar
#101042166

#Key Reference: Gaddis, T. (2015). "Starting out with python" 3rd edition
#Ahmed,S.(personal communication,2016-11-14).

def program ():	
	#creating a new list for the multiple choice questions
	multiplechoice=[]
	#creating each question with answers, and a position for the user input to be store in
	multiplechoice.append([0,1,["12","15","13","11"],-1,"How many months are there in a year?"])
	multiplechoice.append([3,2,["6 billion","18 billion","7 million","7 billion"],-1,"How many people live on earth?"])
	multiplechoice.append([2,3,["18","16","19","21"],-1,"What is the legal drinking age in Ontario?"])
	multiplechoice.append([1,4,["Earth","Mercury","Mars","Jupiter"],-1,"Which planet is closest to the sun?"])
	multiplechoice.append([2,5,["Rio","Seoul","Tokyo","Sydney"],-1,"Where wil the 2020 olymipcs be held?"])
	multiplechoice.append([0,6,["Game of Thrones","The walking Dead", "Suits","Breaking Bad"],-1,"Which show does the charcter Jon Snow come from?"])
	multiplechoice.append([3,7,["The Queen","sir Wilfred Laurier","Peirre elliot Trudeau","sir John A. Macdonald"],-1,"Who is featured on the canadian $10 bill?"])
	multiplechoice.append([1,8,["Austalia","Asia","North America","Africa"],-1,"What is the largest continent?"])	
	multiplechoice.append([2,9,["Gazelle","Ostrich","Cheeta","Horse"],-1,"What is the fastest land animal?"])	
	multiplechoice.append([0,10,["35 million","75 million","150 million","5 million"],-1,"What is the population of Canada?"])
	
	#creating a list for the true and false questions
	trueorfalse=[]
	#creating each querstion with answers and a position for the user input
	trueorfalse.append([True,11,-1,"Are we are the third planet from the sun?"])
	trueorfalse.append([False,12,-1,"Is the chemical composition of water is H2O2?"])
	trueorfalse.append([False,13,-1,"Does the month of November have 31 days?"])
	trueorfalse.append([True,14,-1,"Is breakfast the most important meal of the day?"])
	trueorfalse.append([True,15,-1,"Justin Trudeau is the Prime Minister of Canada"])
	
	#printing and asking, and storing user input
	def MCanswers(x):
		#printing questions and options
		print("Question",x[1],".",x[4])
		print("a:",x[2][0])
		print("b:",x[2][1])
		print("c:",x[2][2])
		print("d:",x[2][3])
		choice= input("Pick an answer( Type a,b,c,or d)\n").upper()
		if choice=="A":
			choice=0
		if choice =="B":
			choice=1
		if choice =="C":
			choice=2
		if choice== "D":
			choice=3
		#taking the user input and replacing it on the third position in the list
		x[3]=choice
		
	#asks the user if they want to quit after each question	
	for x in multiplechoice:
		MCanswers(x)
		keepgoing=input("Type q to quit or any key to continue\n").upper()
		if keepgoing =="Q":
			break
	#printing and asking, and storing user input		
	def TFanswers(x):
	#printing questions and options
		print("Question",x[1],".",x[3])
		print("True")
		print("False")
		choice2=input("Type T or F to answer\n").upper()
		if choice2=="T":
			choice2=True
		if choice2=="F":
			choice2=False
		#taking the user input and replacing it on the second position in the list
		x[2]=choice2
	
	for x in trueorfalse:
		TFanswers(x)
		keepgoing2=input("Type q to quiz or any key to continue\n").upper()
		if keepgoing2=="Q":
			break
	#used to create a score variable
	score=0
	for x in multiplechoice:
		if x[0]==x[3]:
			print("Correct")
			score+=1
		else:
			print("incorrect")
			
	for x in trueorfalse:
		if x[0]==x[2]:
			print("Correct")
			score+=1
		else:
			print("incorrect")
	print("Your mark is",score,"/15")
	percent=(score/15)*100
	print("You got",percent,"%")
	
restart="Y"

while restart=="Y":		
	program()
	restart=input("do you want to retry the quiz type y or n\n").upper()
	
	
	
	
	
	
	
	
	
	
	
	
	
	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	