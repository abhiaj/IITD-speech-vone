import os
import sys
import copy
import pickle
import numpy as np

root = os.getcwd()
sys.path.append(root+'/Name/libsvm-3.23/python')

from svmutil import *
import svmutil
from svm import *

def removeBlanks(str_list):
    while '' in str_list:
        str_list.remove('')
    return str_list
    
def replaceNameTags(script):
    script = script.replace("#(firstname)", "#(person)")
    script = script.replace("#(firstname )", "#(person)")
    script = script.replace("#(first name)", "#(person)")
    script = script.replace("#(first name )", "#(person)")
    script = script.replace("#(lastname)", "#(person)")
    script = script.replace("#(lastname )", "#(person)")
    script = script.replace("#(last name)", "#(person)")
    script = script.replace("#(last name )", "#(person)")
    script = script.replace("#(secondname)", "#(person)")
    script = script.replace("#(secondname )", "#(person)")
    script = script.replace("#(second name)", "#(person)")
    script = script.replace("#(second name )", "#(person)")    
    script = script.replace("#(name)", "#(person)")
    script = script.replace("#(name )", "#(person)")
    script = script.replace("#(middlename)", "#(person)")
    script = script.replace("#(middlename )", "#(person)")
    script = script.replace("#(middle name)", "#(person)")
    script = script.replace("#(middle name )", "#(person)")
    return script

def getFiveGrams(splitscript, j):
    postj1 = j+1
    while(postj1 in range(len(splitscript)) and splitscript[postj1].startswith("#")):
        postj1 += 1
    postj2 = postj1+1
    while(postj2 in range(len(splitscript)) and splitscript[postj2].startswith("#")):
        postj2 += 1
    postj3 = postj2+1
    while(postj3 in range(len(splitscript)) and splitscript[postj3].startswith("#")):
        postj3 += 1
    
    prej1 = j-1
    while(prej1>=1 and splitscript[prej1].startswith("#")):
        prej1 -= 1
    prej2 = prej1-1
    while(prej2>=1 and splitscript[prej2].startswith("#")):
        prej2 -= 1
    mystr = ""
    
    if(prej2<0):
        mystr = mystr + "X "
    else:
        mystr = mystr + splitscript[prej2] + " "
    if(prej1<0):
        mystr = mystr + "X "
    else:
        mystr = mystr + splitscript[prej1] + " "
    if(postj1>=len(splitscript)):
        mystr = mystr + "X "
    else:
        mystr = mystr + splitscript[postj1] + " "
    if(postj2>=len(splitscript)):
        mystr = mystr + "X "
    else:
        mystr = mystr + splitscript[postj2] + " "

    if(postj3>=len(splitscript)):
        mystr = mystr + "X "
    else:
        mystr = mystr + splitscript[postj3] + " "
    return mystr

def getFiveGrams_2(splitscript, j):
    postj1 = j
    while(postj1 in range(len(splitscript)) and splitscript[postj1].startswith("#")):
        postj1 += 1
    postj2 = postj1+1
    while(postj2 in range(len(splitscript)) and splitscript[postj2].startswith("#")):
        postj2 += 1
    postj3 = postj2+1
    while(postj3 in range(len(splitscript)) and splitscript[postj3].startswith("#")):
        postj3 += 1


    prej1 = j-1
    while(prej1>=1 and splitscript[prej1].startswith("#")):            
        prej1 -= 1
    prej2 = prej1-1
    while(prej2>=1 and splitscript[prej2].startswith("#")):
        prej2 -= 1
    mystr = ""
    
    if(prej2<0):
        mystr = mystr + "X "
    else:
        mystr = mystr + splitscript[prej2] + " "
    if(prej1<0):
        mystr = mystr + "X "
    else:
        mystr = mystr + splitscript[prej1] + " "
    if(postj1>=len(splitscript)):
        mystr = mystr + "X "
    else:
        mystr = mystr + splitscript[postj1] + " "
    if(postj2>=len(splitscript)):
        mystr = mystr + "X "
    else:
        mystr = mystr + splitscript[postj2] + " "

    if(postj3>=len(splitscript)):
        mystr = mystr + "X "
    else:
        mystr = mystr + splitscript[postj3] + " "
    return mystr

def getfivegrams(t, pn):
    xp = []
    x_mid = []
    if not (pn == "no name"):
        
        names = pn.split(" ")[1:-1]
        while "'," in names:
            names.remove("',")
        while "'" in names:
            names.remove("'")
        while "." in names:
            names.remove(".")
            
        for x in names:
            
            hi = t.split(" ")
            try:
                index = hi.index(x)
                if(index==0):
                    mystr = "X X "
                elif(index==1):
                    mystr = "X " + hi[0] + " "
                else:
                    mystr = hi[index-2] + " " + hi[index-1] + " "

                mystr = mystr + hi[index] + " "

                if(index==len(hi)-1):
                    mystr = mystr + "X X "
                elif(index==len(hi)-2):
                    mystr = mystr + hi[len(hi)-1] + " X "
                else:
                    mystr = mystr + hi[index+1] + " " + hi[index+2] + " "
                xp.append(mystr)
                x_mid.append(hi[index])
            except:
                pass
    return xp, x_mid
    
def vectoriseData(xp, vocabData):
    personsData=np.array(xp)
    (a,b)=xp.shape
    dataMade=np.zeros((a,len(vocabData)))
    for j in range(a):
        for word in xp[0][j].split():
            if word in vocabData:
                dataMade[j][vocabData[word]]=1
            else:
                pass
    return dataMade

def insertColumn(datafile, labelstring, labels):
    try:
        datafile.insert(4,labelstring, labels)
    except:
        del datafile[labelstring]
        datafile.insert(4,labelstring, labels)
    return

def loadModel():
    model = svm_load_model(root+'/Name/libsvm.model')
    return model

def predict(xp, yp, vocabData, model):
    dataMade = vectoriseData(xp, vocabData)
    testy = yp.squeeze()
    labels = svm_predict(testy, dataMade, model)
    labels_output = np.array(labels[0])
    labels_confidence = np.array(labels[2])
    tX = xp.squeeze() ############### Check it was testX earlier
    to = labels_output.squeeze()
    tc = labels_confidence.squeeze()
    print("accuracy ", accuracy_score(yp,to))
    print("confusion ", confusion_matrix(yp,to))
    print("precision_score ", precision_score(yp,to))
    print("recall_score ", recall_score(yp,to))
    print("f1_score ", f1_score(yp,to))

    return tX, to, tc

def predictMain(model, vocabData, xp, yp = None):
    if yp==None:
        yp = np.array([0]*len(xp))
    dataMade = vectoriseData(xp, vocabData)
    testy = yp.squeeze()
    labels = svm_predict(testy, dataMade, model, '-q')
    labels_output = np.array(labels[0])
    labels_confidence = np.array(labels[2])
    
    return labels_output, labels_confidence

def getAccuracy(labels_true, labels_output, labels_confidence):
    to = labels_output.squeeze()
    tc = labels_confidence.squeeze()
    print("accuracy ", accuracy_score(labels_true,to))
    print("confusion ", confusion_matrix(labels_true,to))
    print("precision_score ", precision_score(labels_true,to))
    print("recall_score ", recall_score(labels_true,to))
    print("f1_score ", f1_score(labels_true,to))
    return

def getLabels(x_in, x_mid, to, datafile_len, tc = None, alpha=0):
    to_c = copy.deepcopy(to)
    if alpha!=0:
        for i in range(len(to)):
            if tc[i]>alpha:
                to_c[i] = 1
            else:
                to_c[i] = 0

    labels = [[] for i in range(datafile_len)] #### change from len(datafile)
    for i in range(len(to_c)):
        if to_c[i]==1:
            labels[x_in[i]].append(x_mid[i])
    return labels

def getLabelsMain(to, tc, x_mid, alpha=0):
    to_c = copy.deepcopy(to)

    for i in range(len(to)):
        if tc[i]>alpha:
            to_c[i] = 1
        else:
            to_c[i] = 0

    labels = []
    for i in range(len(to_c)):
        if to_c[i]==1:
            labels.append(x_mid[i])
    return labels

def save_obj(obj, name ):

    with open(root+"/Name/"+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open(root+"/Name/"+ name + '.pkl', 'rb') as f:
        return pickle.load(f)