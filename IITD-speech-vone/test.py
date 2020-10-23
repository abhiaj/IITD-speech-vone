from utils import get_name, get_loc, get_dob, remove_silence_url, get_gender_url, get_quality_url, get_themes, get_dob

s = "उठाया जाता है बिहार की आने वाली सीमा से मिल जायगी दिलीप पांडे मोबाइल वाणी "
t = "शंकर सिंह कुंदन कुमार अरविन्द झा सहित कई अन्य ने बताया कि दिन भर खेत में म्हणत से टमाटर को तोडना पड़ता है "
u = " "
v = "उत्तर प्रदेश बी एच यू वाराणसी"
name1 = get_name(s)    # Can check for s,t,u and v

print("Name is : {}".format(name1))

s = "मैं सिद्धेश अभियान जिला का छत्तीसगढ़ में रहने वाला हूं ब्लाइंड स्कूल आरा वालों में पढ़ाई करता हूं मैं नवी कक्षा में पढ़ाई करता हूं अरे नाम और गांव जिला"
t = "उत्तर प्रदेश बी एच यू वाराणसी"
u = "शंकर सिंह कुंदन कुमार"
v = " "
loc1 = get_loc(s)

print("Location is : {}".format(loc1))

s = "12 अक्टूबर 2015"
t = "13 अप्रैल 2016"
u = "3 तारीख नौवां महीना 2014"
v = "आषाढ़ महीना 4 तारीख"
w = ""

date1 = get_dob(s)

print("Date of Birth is : {}".format(date1))

# Remove Silence
remove_silence_url("http://voice.gramvaani.org/fsmedia/recordings/137/295538.mp3")

# Get gender
print("Gender of user : {}".format(get_gender_url("http://voice.gramvaani.org/fsmedia/recordings/137/301897.mp3")))

# Get Audio quality (Acceptable or Blank/Noisy)
print("Audio Quality : {}".format(get_quality_url("http://voice.gramvaani.org/fsmedia/recordings/137/295538.mp3")))

# Get themes
print("Theme is : {}".format(get_themes("samp.txt")))

#from utils import get_transcript
