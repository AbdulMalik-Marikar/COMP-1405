#Abdul-Malik Marikar
#101042166

from SimpleGraphics import *
setAutoUpdate(False)
img = loadImage("circle.gif")
width=getWidth(img)
height= getHeight(img)
new=createImage(width,height)
new1=createImage(width,height)
new2=createImage(width,height)
new3=createImage(width,height)
for column in range (width):
	for row in range(height):
		r,g,b = getPixel (img,column,row)
		putPixel(new,column,row,r,g,b)
		putPixel(new1,column,row,r,0,0)
		putPixel (new2,column,row,0,g,0)
		putPixel (new3,column, row,0,0,b)
	clear()
	drawImage(new,0,0)
	drawImage(new1,270,0)
	drawImage(new2,540,0)
	drawImage(new3,270,270)
	update()
