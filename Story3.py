from Getter import *


def story3(debug= False):
	if debug: print "--In story1 function--"
	
	name1 = getWord("A Name: ", debug)
	building1 = getWord("A Restaurant: ", debug)
	food1 = getWord("A Food: ", debug)
	
	out += " Good afternoon said " + name1
	out += " to Billy, as he was walking towards " + restaurant1
    out += " when Billy arrived he asked for some " + food1
