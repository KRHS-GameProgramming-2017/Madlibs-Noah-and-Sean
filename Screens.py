def splash(debug = False):
	if debug: print "--In splash function--"
	output = ""
	output += "***************************************\n"
	output += "*                                     *\n"
	output += "*        Welcome to Madlibs           *\n"
	output += "*           Written by                *\n"
	output += "*        Noah Gray and Sean Tobin     *\n"
	output += "*                                     *\n"
	output += "***************************************\n"
	return output

def menu(debug = False):
	if debug: print "--In menu function--"
	output = ""
	output += "***************************************\n"
	output += "*Main menu                            *\n"
	output += "*1) The Creepy Little Boy             *\n"
	output += "*2) The Crazy Animal                  *\n"
	output += "*3) The Weird Restaurant              *\n"
	output += "*Q) Exit                              *\n"
	output += "***************************************\n"
	return output
