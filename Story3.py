from Getter import *


def story3(debug= False):
	if debug: print "--In story1 function--"
	
	friend1 = getWord("A Name: ", debug)
	distance1 = getNumber("A Number: ", debug)
	store1 = getWord("A Store: ", debug)
	
	out += " Good afternoon said " + name1
	out += " to Billy, as he was walking towards " + building1
