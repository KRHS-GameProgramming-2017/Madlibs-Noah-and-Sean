# Written by Chris Spooner
from Screens import *
from Getter import *
from story0 import *
from Story1 import *
from Story2 import *
from Story3 import *

def madlibs(debug = False):
    if debug: print "--Debugging Activated--"
    
    print splash(debug)
    raw_input("Press Enter to Continue")
    
    end = False
    while not end:
        print menu(debug)
        response = getMenuResponse(debug)
        
        if response == "q":
            exit()
        elif response == "1":
            print story1()
            raw_input("Press Enter to Continue")
        elif response == "2":
            print story2()
            raw_input("Press Enter to Continue")
        elif response == "3":
            print story3()
            raw_input("Press Enter to Continue")
        elif response == "0":
            print story0()
            raw_input("Press Enter to Continue")
        
            
            
    
    
madlibs(True)
