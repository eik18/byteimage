import Image,ImageDraw
im=Image.new("L",(5,5))
draw=ImageDraw.Draw(im)
color=25
for x in range(0,5):
	for y in range (0,5):
		draw.point((x,y),fill=color)
		color=color+10
im.save("test2.png", "PNG")