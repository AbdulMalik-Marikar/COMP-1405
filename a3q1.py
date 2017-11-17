#Abdul-Malik Marikar
#101042166

#Key Reference: Gaddis, T. (2015). "Starting out with python" 3rd edition

#import helper
from helper import*

#first movement
for firstmovement in range (0,3):
	goRight()

#second movement
secondmovment=0
while secondmovment<1:
	goDown()
	secondmovment+=1

#third movement
for thirdmovement in range (0,1):
	goRight()

#fourth movement
fourthmovement=0
while fourthmovement<2:
	goDown()
	fourthmovement+=1

#fifth movements
for fifthmovements in range (0,6):
	goLeft()

#sixth movement
sixthmovement=0
while sixthmovement<2:
	goDown()
	sixthmovement+=1
	
#seventh movement
for seventhmovement in range (0,4):
	goRight()

#eight movement	
eightmovement=0
while eightmovement<5:
	goDown()
	eightmovement+=1

#ninth movement	
for ninthmovement in range (0,1):
	goRight()

#tenth movement
tenthmovement= 0
while tenthmovement <1:
	goDown()
	tenthmovement+=1

#eleventh movement
for eleventhmovement in range (0,1):
	goRight()

#twelfth movement
twelfthmovement=0
while twelfthmovement<1:
	goDown()
	twelfthmovement+=1

#thirteenth movement using a flag
thirteenthmovement=0	
stay=True
while stay:
	goLeft()
	thirteenthmovement+=1
	if not thirteenthmovement<8:
		stay=False

		
#final movement using a break
lastmovement=0
while True:
	goDown()	
	lastmovement+=1
	if lastmovement==2:
		break
	