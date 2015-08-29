#!/usr/bin/which python
import binascii
import Image, ImageDraw
import pprint
a=open ('ls','rb')
alist=a.readlines()
imatrix=[]
linehighmark=0
for line in alist:
	lmatrix=[]
	for character in line:
		 lmatrix.append (int ((binascii.hexlify(character)), 16))
	imatrix.append(lmatrix)
	if len(lmatrix)>linehighmark:
		linehighmark=len(lmatrix)

imagelength=len(imatrix)
imagewidth=linehighmark
#pprint.pprint(imatrix[1])

#exit()
im=Image.new("L",(imagelength,imagewidth))
draw=ImageDraw.Draw(im)
for x in range(0,imagelength):
	print "row %d" %x
	tempwidth=len(imatrix[x])
	print "line width %s" %tempwidth
	for y in range(0,tempwidth):
		print "character %d" %y
		draw.point((x,y),fill=imatrix[x][y])
im.save("test3.png", "PNG")