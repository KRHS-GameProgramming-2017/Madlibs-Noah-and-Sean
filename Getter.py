def getMenuResponse(debug = False):
    if debug: print "--In getMenuResponse function--"
    goodInput = False
    while not goodInput:
        response = raw_input("Make a selection please: ")
        if (response == "1" or 
            response == "one" or 
            response == "story 1"):
                goodInput = True
                response = "1"
        elif (response == "2" or 
            response == "two" or 
            response == "story 2"):
                goodInput = True
                response = "2"
        elif (response == "3" or 
            response == "three" or 
            response == "story 3"):
                goodInput = True
                response = "3"
        elif (response == "0" or 
            response == "zero" or 
            response == "story 0"):
                goodInput = True
                response = "0"
        elif (response == "q" or 
              response == "quit" or 
              response == "exit"):
            goodInput = True
            response = "q"
        else:
            print "Please enter a valid input!"
    return response
        
def getWord(prompt, debug):
    if debug: print "--In getWord function--"
    goodInput = False
    while not goodInput:
        response = raw_input(prompt)
        if isSwear(response):
            goodInput = False
            print "Please dont swear thats not nice thanks"
        elif response == "":
            goodInput = False
            print "Type something"
        else:
            goodInput = True
    return response
        
def getNumber(prompt, debug):
    if debug: print "--In getWord function--"
    goodInput = False
    numbers = "1234567890."
    while not goodInput:
        response = raw_input(prompt)
        goodInput = True    
        for letter in response:
            if letter not in numbers:
                goodInput = False
                print letter + " is not a number"
    return response 
def getWeapon(prompt, debug):
    if debug: print "--In getWeapon function--"
    weaponList =["gun",
                "knife",
                "bat",
                "bottle",
                "fist",
                "bomb",
                "chainsaw",
                "wrench",
                "sword",
                "rope",
                "bow"]
                
    goodInput = False
    while not goodInput:
        response = raw_input(prompt)
        if response in weaponList:
            goodInput = True
        else:
            print "whats that weapon"
            goodInput = False
    return response 
        
def getfeeling(prompt, debug):
    if debug: print "--In get feeling function--"
    feelingList =["sad",
                "happy",
                "angry",
                "mad",
                "depressed",
                "embarrassed",
                "scared",
                "hopeful",
                "bored",
                "triggered",
                "salty"]
    goodInput = False
    while not goodInput:
        response = raw_input(prompt)
        if response in feelingList:
            goodInput = True
        else:
            print "whats that feeling"
            goodInput = False
    return response
   
   
def getaction(prompt, debug):
    if debug: print "--In get action function--"
    actionList =["hit",
                "punched",
                "kicked",
                "ran",
                "watched",
                "read",
                "helped",
                "fixed",
                "killed",
                "made",
                "wrote"]
    goodInput = False
    while not goodInput:
        response = raw_input(prompt)
        if response in actionList:
            goodInput = True
        else:
            print "whats that action"
            goodInput = False
    return response
    
    
def isSwear(word):
    swearList = ["poop",
                 "dumb",
                 "stupid",
                 "retard",
                 "fuck",
                 "dick",
                 "dic",
                 "sex",
                 "ass",
                 "pussy",
                 "kys",
                 "zeb",
                 "dylanmonnetespaghetii",
                 "virgin",
                 "penis",
                 "god",
                 "jesus",
                 "cock",
                 "cunt",
                 "nigger",
                 "niqqer",
                 "nig",
                 "motherfucker",
                 "vagina",
                 "bitch",
                 "slit",
                 "cum",
                 "pissoff",
                 "Twat",
                 "dickwead",
                 "wanker",
                 "fucknugget",
                 "daddy",
                 "wtf",
                 "anul",
                 "sperm",
                 "jerk",
                 "dumbfuck"
                 "Gay"
                 "faggot"
                 "lesbian"
                 "shit"
                 "slut"
                 "whore"
                 "fucked"]
    if word.lower() in swearList:
        return True
    else:
        return False
    
