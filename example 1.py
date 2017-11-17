
diameter = float(input("what is the diameter of your first circle\n"))

diameter1 = float(input("What is the diameter of your second circle\n"))

perimeter1= (diameter/2)*3.141592654
perimeter2= (diameter1/2)*3.141592654

if perimeter1>perimeter2:
	print("Your first circle has a larger perimeter")
else:
	print("YOur second circle has a larger perimeter")