#Abdul-Malik Marikar
#101042166

from SimpleGraphics import *
setAutoUpdate(False)
img = loadImage("circle.gif")
width=getWidth(img)
height= getHeight(img)
new=createImage(width,height)
new2= createImage(width,height)
for column in range (width):
	for row in range(height):
		r,g,b = getPixel (img,column,row)
		putPixel(new,column,row,255-r,255-g,255-b)
		putPixel(new2,column,row,r,g,b,)
	clear()
	drawImage(new2,0,0)
	drawImage(new,270,0)
	update()
