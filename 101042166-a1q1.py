#Abdul-Malik Marikar
#101042166
#Completed Sep. 22 2016

#Key References: Gaddis, T. (2015). "Starting out with python" 3rd edition 
#                Simple graphics tutorial part 1&2
#importing simple graphics
from SimpleGraphics import *

#creating the outline of the image
setColor("snow")
rect(0,0,99,49)
setFill(255,255,255)
setOutline("snow")

#box in lower corner
setColor(0,0,0)
rect(19,34,16,15)
line(36,36,36,49)
line(37,42,37,49)
line(38,48,38,49)
line(35,34,35,49)


#Box in the right
rect(57,0,42,49)
rect(56,0,1,42)
rect(55,0,1,34)
rect(54,0,1,23)
rect(53,0,1,11)
rect(52,0,1,2)

#red in the box
setColor(102,0,0)
polygon(63,22,63,30,64,38,65,46,69,46,71,45,71,34,70,28,63,22)


#Gray polygon in the corner
setColor(51,51,51)
polygon(98,47,88,47,73,39,74,34,97,17,98,18,98,47)
line(73,34,73,40)
setColor(126,51,51)
line(72,34,72,40)
