from polyglot.text import Text, Word
import string

def getPolyglotName(userReply):
    text = Text(userReply, hint_language_code="hi")
    userReplyEntities = {}

    loc_list = []
    for e in text.entities:
        if e.tag == "I-PER":
            loc = " "
            for i in e:
                loc += i + " "
            loc_list.append(loc)
            userReplyEntities["person_mod"] = loc_list
            userReplyEntities["person"] = e
    return userReplyEntities

def getName(mystr):
    if "nan"== str(mystr):
        return "nil"
    else:
        nameEntities = getPolyglotName(mystr)
        if(bool(nameEntities)):
            entity = nameEntities["person_mod"]
            return entity
        else:
            entity = "no name"
            return entity