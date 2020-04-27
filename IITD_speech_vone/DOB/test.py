import pickle
import json
import numpy as np
from main import findDate

testSentence1 = "5 सितंबर 2016"
testSentence2 = "4 तारीख सातवां महीना 2017"
testSentence3 = "3 तारीख नौवां महीना 2014"#

out1 = json.loads(findDate(testSentence1))
out2 = json.loads(findDate(testSentence2))
out3 = json.loads(findDate(testSentence3))

print(out1)
print(out2)
print(out3) 
