from Getter import *


def story1(debug= False):
    if debug: print "--In story1 function--"
    
    car1 = getWord("A Car: ", debug)
    food1 = getWord("A Food: ", debug)
    game1 = getWord("A Game: ", debug)
    person1= getWord("A Person: ", debug)
    word1= getWord("A Word: ", debug)
    place1= getWord("A Place: ", debug)
    person2= getWord("A Person: ", debug)
    weapon1= getWeapon("A Weapon: ", debug)
   
   
    out = ""
    out += "There once was a little boy who got in the wrong, " + car1
    out += ",He wanted some " + food1
    out += " Once he got the " + food1
    out += " he left and decided to eat the " + food1
    out += " after he ate it he went home and played " + game1
    out += " as he was playing " + game1
    out += ", " + person1
    out += " came up and said " + word1
    out += " the little boy didnt listen to " + person1
    out += " so " + person1
    out += " told him to go to " + place1
    out += " once he got to " + place1
    out += " he saw " + person2
    out += " then " + person2
    out += " killed him with a " + weapon1 
    
    return out
