'''                                                                         v0.8
##
#  A partial implementation / variant of the classic "Spacewar" video game
#
#  Copyright (C) 2015 Robert Collier
#
#  Known Issues: 
#
#    * At the moment there is no collision detection, so the "lasers" do not
#      have any effect other than the depletion of energy
#
#    * The following and fleeing behaviour controller of the opponent does not
#      factor in the "wrapping" of the game world at the border of the window
#
#  Revision History:
#    v0.0 -- The starting point for a live programming demonstration
#
#    v0.1 -- Draws some text to the window to indicate the keys currently held
#
#    v0.2 -- Uses variables to store the player angle, position, and velocity
#            Uses a random number generator to select an angle and energy level
#            Uses trig to determine the placement of the nose of the player
#            Draws the player ship and an energy bar to the window
#
#    v0.3 -- Uses the angle of the player to determine a velocity vector
#            Uses the velocity vector to update the position of the player
#
#    v0.4 -- Adds variables to store the opponent ship data
#            Opponent moves at constant speed with no change to angle
#
#    v0.5 -- Uses trig to determine the target angle between opponent and player
#            Uses the target angle to determine how the opponent should rotate
#            Opponent changes angle to follow player
#
#    v0.6 -- Opponent changes angle to avoid player
#
#    v0.7 -- Opponent selects between follow and avoid according to energy level
#            Opponent fires on player if following and within range
#
#    v0.8 -- Player can now fire as well if player energy level is sufficient
#
'''


# for rendering the elements of our game window
from SimpleGraphics import *

# for calculating angles and updating positions/velocities
from math import sin, cos, degrees, radians, sqrt, atan2, fabs

# for generating random values
from random import randint

# for slowing the game down to p1_Angle playable speed
from time import sleep

# this turns off SimpleGraphics auto refresh and speeds everything up
setAutoUpdate(False)

# this changes the background colour to black and the line width to 0
background("black")
setOutline("lawn green")
setWidth(0)

# this is the size of the ships
shipRadius = 10

# these are the values associated with the player
p1_X_Position = 400
p1_Y_Position = 100
p1_Angle = 0
p1_X_Velocity = 0
p1_Y_Velocity = 0
p1_Energy = 100

# these are the values associated with the opponent
p2_X_Position = 400
p2_Y_Position = 300
p2_Angle = 0
p2_X_Velocity = 0
p2_Y_Velocity = 0
p2_Energy = 100

# this will be the initial setting for the opponent ai mode
mode = "hunt"

while not closed():

	'''
	# render the scene
	'''
	
	# clear the screen
	clear()

	# calculate the location for the "nose" of the player
	p1_X_Fore = shipRadius*sin(radians(p1_Angle))
	p1_Y_Fore = shipRadius*cos(radians(p1_Angle))

	# draw the energy bar and ship of the player in blue with no outline
	setFill("steel blue")
	ellipse(p1_X_Position-shipRadius, p1_Y_Position-shipRadius, 2*shipRadius, 2*shipRadius)
	ellipse(p1_X_Position+p1_X_Fore-(shipRadius/2), p1_Y_Position+p1_Y_Fore-(shipRadius/2), shipRadius, shipRadius)
	rect(20, 20, p1_Energy, 20) 

	# calculate the location for the "nose" of the opponent
	p2_X_Fore = shipRadius*sin(radians(p2_Angle))
	p2_Y_Fore = shipRadius*cos(radians(p2_Angle))
	
	# change the colour of the ship to indicate its current ai state
	if mode == "flee":
		setFill("dark orange")
	else:
		setFill("deep pink")
	
	# draw the energy bar and ship of the opponent with no outline
	rect(780-p2_Energy, 20, p2_Energy, 20) 
	ellipse(p2_X_Position-shipRadius, p2_Y_Position-shipRadius, 2*shipRadius, 2*shipRadius)
	ellipse(p2_X_Position+p2_X_Fore-(shipRadius/2), p2_Y_Position+p2_Y_Fore-(shipRadius/2), shipRadius, shipRadius)

	
	'''
	# get the player input
	'''
	
	# reset the Boolean flag to indicate whether or not the player is firing
	p1_IsFiring = False
	
	# get the set of keys being held by the player
	keys = getHeldKeys()
	
	# if the left or right arrow key is in that set, adjust the player angle
	if "Left" in keys:
		p1_Angle = p1_Angle + 2
	elif "Right" in keys:
		p1_Angle = p1_Angle - 2

	# if the up arrow key is in that set, adjust the player velocity
	if "Up" in keys:
		p1_X_Velocity = p1_X_Velocity+(0.01*p1_X_Fore)
		p1_Y_Velocity = p1_Y_Velocity+(0.01*p1_Y_Fore)

	# if the left control key is in that set, set the player firing flag
	if "Control_L" in keys:
		p1_IsFiring = True
	
			
	'''
	perform the game logic (i.e., update the world)...
	'''

	'''
	     ...with respect to the player
	'''
	
	# move the player by adding velocities to positions
	p1_X_Position = p1_X_Position+p1_X_Velocity
	p1_Y_Position = p1_Y_Position+p1_Y_Velocity
	
	# check if the player has passed the edge of the screen and if so wrap
	if p1_X_Position > 800:
		p1_X_Position = p1_X_Position - 800
	elif p1_X_Position < 0:
		p1_X_Position = p1_X_Position + 800
	if p1_Y_Position > 600:
		p1_Y_Position = p1_Y_Position - 600
	elif p1_Y_Position < 0:
		p1_Y_Position = p1_Y_Position + 600

	# with probability 1/6 draw a "laser" from the player and deduct energy
	if p1_IsFiring and randint(1,6) == 1 and p1_Energy >= 5:
		setWidth(3)
		line(p1_X_Position+p1_X_Fore,p1_Y_Position+p1_Y_Fore,p1_X_Position+8*p1_X_Fore+randint(-3, 3),p1_Y_Position+8*p1_Y_Fore+randint(-3, 3))
		setWidth(0)
		p1_Energy = p1_Energy - 5

	# increase the player energy level by a small amount
	if p1_Energy < 100:	
		p1_Energy = p1_Energy + .1

	'''
	     ...with respect to the opponent
	'''

	# move the opponent by calculating velocities and adding these to positions		
	p2_X_Velocity = 2*shipRadius*sin(radians(p2_Angle))
	p2_Y_Velocity = 2*shipRadius*cos(radians(p2_Angle))
	p2_X_Position = p2_X_Position+0.1*p2_X_Velocity
	p2_Y_Position = p2_Y_Position+0.1*p2_Y_Velocity

	# check if the opponent has passed the edge of the screen and if so wrap
	if p2_X_Position > 800:
		p2_X_Position = p2_X_Position - 800
	elif p2_X_Position < 0:
		p2_X_Position = p2_X_Position + 800
	if p2_Y_Position > 600:
		p2_Y_Position = p2_Y_Position - 600
	elif p2_Y_Position < 0:
		p2_Y_Position = p2_Y_Position + 600

	# calculate the direction in which the opponent should be facing
	p2_TargetAngle = (degrees(atan2(-(p2_Y_Position-p1_Y_Position),(p2_X_Position-p1_X_Position)))-90)
	
	# if the ai mode is set to "flee", reverse that angle
	if mode == "flee":
		p2_TargetAngle = p2_TargetAngle+180

	# use modulation to convert the angles to a range of (0, 359)
	p2_Angle = p2_Angle % 360
	p2_TargetAngle = p2_TargetAngle%360

	# turn the opponent ship depending upon the target angle
	if (p2_TargetAngle - p2_Angle >=0 and p2_TargetAngle - p2_Angle <= 180) or (p2_TargetAngle - p2_Angle <=- 180 and p2_TargetAngle - p2_Angle >= -360):
		p2_Angle = p2_Angle + 2
	else:
		p2_Angle = p2_Angle - 2
		
	# if the ai mode is set to "hunt" and the opponent is close enough, attack
	if mode == "hunt" and fabs(p2_TargetAngle - p2_Angle) % 360 < 10 and sqrt((p2_X_Position-p1_X_Position)**2+(p2_Y_Position-p1_Y_Position)**2) < 120 and randint(1,6)==1:
		setWidth(3)
		line(p2_X_Position+p2_X_Fore,p2_Y_Position+p2_Y_Fore,p1_X_Position+randint(-3, 3),p1_Y_Position+randint(-3, 3))
		setWidth(0)
		p2_Energy = p2_Energy - 5
	
	# adjust the ai mode based on the energy level of the opponent
	if p2_Energy < 20:
		mode = "flee"
	elif p2_Energy > 60:
		mode = "hunt"

	# increase the opponent energy level by a small amount
	if p2_Energy < 100:	
		p2_Energy = p2_Energy + .1

		
	# pause for a moment so the game runs at a playable speed
	sleep(0.01)
		