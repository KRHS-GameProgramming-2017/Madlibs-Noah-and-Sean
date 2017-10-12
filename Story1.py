from Getter import *


def story1(debug= False):
	if debug: print "--In story1 function--"
	
	friend1 = getWord("A Name: ", debug)
	distance1 = getNumber("A Number: ", debug)
	store1 = getWord("A Store: ", debug)
	
	out = ""
	out += "One day me and my friend, " + friend1
	out += ", walked " + distance1
	out += " miles to " + store1
	out += ". " + friend1
	out += " loves " + store1
	
	return out
