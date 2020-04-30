from polyglot.text import Text, Word

def getPolyglotLocation(userReply):
    """
    Called inside of getLocation Function. 
    Return complete polyglot result on the userReply String
    """
    text = Text(userReply, hint_language_code="hi")
    userReplyEntities = {}

    loc_list = [] 
    for e in text.entities:
        if e.tag == "I-LOC":
            loc = " "
            for i in e:
                loc += i + " "
            loc_list.append(loc)
            userReplyEntities["location_mod"] = loc_list
            userReplyEntities["location"] = e
    return userReplyEntities
    
def getLocation(mystr):
    """
    Outputs entity identified by polyglot if present otherwise outputs n
    """
    locationEntities = getPolyglotLocation(mystr)
    if(bool(locationEntities)):
        entity = locationEntities["location_mod"]
        # print(entity)
    else:
        entity = "n"
        # print("No location Found in Polyglot")
    return entity

