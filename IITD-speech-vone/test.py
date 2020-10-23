from utils import get_name

s = "उठाया जाता है बिहार की आने वाली सीमा से मिल जायगी दिलीप पांडे मोबाइल वाणी "
t = "शंकर सिंह कुंदन कुमार अरविन्द झा सहित कई अन्य ने बताया कि दिन भर खेत में म्हणत से टमाटर को तोडना पड़ता है "
u = " "
v = "उत्तर प्रदेश बी एच यू वाराणसी"
name1 = get_name(s)
# name2 = get_name(t)
# name3 = get_name(u)
# name4 = get_name(v)
print(name1)
# print(name2)
# print(name3)
# print(name4)

from utils import get_loc

s = "मैं सिद्धेश अभियान जिला का छत्तीसगढ़ में रहने वाला हूं ब्लाइंड स्कूल आरा वालों में पढ़ाई करता हूं मैं नवी कक्षा में पढ़ाई करता हूं अरे नाम और गांव जिला"
t = "उत्तर प्रदेश बी एच यू वाराणसी"
u = "शंकर सिंह कुंदन कुमार"
v = " "
loc1 = get_loc(s)
# loc2 = get_loc(t)
# loc3 = get_loc(u)
# loc4 = get_loc(v)
#
print(loc1)
# print(loc2)
# print(loc3)
# print(loc4)

# For DOB
# from utils import get_dob
# s = "12 अक्टूबर 2015"
# t = "13 अप्रैल 2016"
# u = "3 तारीख नौवां महीना 2014"
# v = "आषाढ़ महीना 4 तारीख"
# w = ""

# date1 = get_dob(s)
# date2 = get_dob(t)
# date3 = get_dob(u)
# date4 = get_dob(v)
# date5 = get_dob(w)

# print(date1)
# print(date2)
# print(date3)
# print(date4)
# print(date5)

from utils import remove_silence_url
remove_silence_url("http://voice.gramvaani.org/fsmedia/recordings/137/295538.mp3")

from utils import get_gender_url
print(get_gender_url("http://voice.gramvaani.org/fsmedia/recordings/137/301897.mp3"))

from utils import get_quality_url
print(get_quality_url("http://voice.gramvaani.org/fsmedia/recordings/137/295538.mp3"))

from utils import get_themes
print(get_themes("samp.txt"))

from utils import get_dob
print(get_dob(s))

from utils import get_transcript
