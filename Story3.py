from Getter import *


def story3(debug= False):
    if debug: print "--In story1 function--"
    
    name1 = getWord("A Name: ", debug)
    restaurant1 = getWord("A Restaurant: ", debug)
    food1 = getWord("A Food: ", debug)
    food2= getWord("A Dessert: ", debug)
    feeling1= getWord("A Feeling: ", debug)
    action1= getWord("An Action: ", debug)
    feeling2= getWord("A Feeling: ", debug)
    out += " Good afternoon said " + name1
    out += " to Billy, as he was walking towards " + restaurant1
    out += " when Billy arrived he asked for some " + food1
    out += " The " + food1
    out += " was very delicious but not very filling so billy asked for some  " + food2
    out += " When the   " + food2
    out += " arrived Billy was  " + feeling1
    out += " so he decided to   " + action1
    out += " when he   " + action1
    out += " The waiter chased him this caused billy to get even more " + feeling2
    
