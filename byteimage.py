#!/usr/local/bin/python
"""ByteImage
Depicts a binary file as an image and calculates Entropy using Shannon Entropy Function

Usage:
	byteimage.py (-c|-g) [-e] <input_file> <output_file>  
	byteimage.py -e <input_file> 
	
Options:
	-c Output in color
	-e Calculate Entropy, with zero being low entropy and approximately 3.2 high entropy
	-g Output in gray-scale
	-h --help This screen.
	--version Version
"""
from PIL import Image, ImageColor, ImageDraw
from scipy import stats
from docopt import docopt 
import math

def arraysize(varray=[]):
	sidelength=math.sqrt(len(varray))
	imagewidth=math.floor(sidelength)
	imagelength=math.ceil(sidelength)
	resultdic={'imagewidth':imagewidth,'imagelength':imagelength}
	return resultdic

def wraparray(varray=[]):
	arraywidth=arraysize(varray)
	endarray=[]
	temparray=[]
	for num,item in enumerate(varray):
		if math.fmod(num,arraywidth['imagewidth'])==0 and num!=0:
			endarray.append(temparray)
			temparray=[]
		temparray.append(item)
	endarray.append(temparray)
	return endarray

def calcentropy(v_array):
	'''
	@todo:  switch entropy base from e to 2.  Currently calculating nats instead of bits
	'''
	#Takes Array, converts to numpy array, flattens, creates a histogram, then runs histogram through entropy function
	#v_array=numpy.array(v_array)
	#v_array=numpy.hstack(v_array)
	v_hist=stats.histogram(v_array)
	return stats.entropy(v_hist[0],base=2)

def read_input (v_input_file_name):
	# Read input file and convert to list by byte
	'''
	@TODO: simplifed using ord
	'''
	try:
		input_file_object = open (v_input_file_name, 'rb')
		linelist = input_file_object.read()
		outarray=[]
		for item in linelist:
			outarray.append(ord(item))
		output_object = outarray
		return output_object
	except Exception as e:
		print "Oh no, something went wrong: %s" % e

def create_image (v_length, v_width, v_dataobject, v_output_file_name,color=False):
	'''
	@TODO: Do we need two functions here, or could we get away with just one?
	Are the behaviors distinct enough to be two functions or does this smell like
	you're breaking the DRY rule? -WL
	''' 
	# create color image
	v_length=int(v_length)
	v_width=int(v_width)
	if color ==True:
		coloroption='RGB'
	else:
		coloroption='L'
	
	im = Image.new(coloroption,
				 (v_width, v_length))
	draw = ImageDraw.Draw(im)
	t_row=0
	t_column=0
	for num,item in enumerate(v_dataobject):
		#print "x:{0}y:{1},".format(t_column,t_row)
		if num/(t_row+1)==v_width:
			t_row=t_row+1
			t_column=0
		if color==True:
			t_colorvalue = item * .703
			t_colorstring = "hsl({0},100%,50%)".format(int(t_colorvalue))
			t_rgbcolor = ImageColor.getrgb(t_colorstring)
			draw.point((t_column, t_row), fill=t_rgbcolor)
		if color==False:
			draw.point((t_column, t_row), fill=item)
		t_column=t_column+1
	im.save(v_output_file_name, "PNG")

def main():
	arguments = docopt(__doc__, version='byteimage 0.5')  
	in_file = arguments['<input_file>']
	out_file = arguments['<output_file>']
	processed_file = read_input(in_file)
	imagesize=arraysize(processed_file)
	imagewidth = imagesize['imagewidth']
	imagelength = imagesize['imagelength']
	if arguments['-c']:
		print "Generating Color Image...this may take a minute or so for large files"
		create_image (imagelength, imagewidth, processed_file, out_file,True)
	if arguments['-g']:
		print "Generating Grayscale Image...this may take a minute or so for large files"
		create_image (imagelength, imagewidth, processed_file, out_file,False)
	if arguments['-e']:
		print "Calculating Entropy"
		print "Entropy Estimate: {0}".format(calcentropy(processed_file))

		
if __name__ == '__main__':
	main()
