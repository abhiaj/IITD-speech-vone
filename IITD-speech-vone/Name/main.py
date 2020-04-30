import numpy as np
import pandas as pd

from sklearn.metrics import confusion_matrix, f1_score
from sklearn.metrics import accuracy_score, precision_score, recall_score

from Name.classifier_utils import replaceNameTags, getFiveGrams, getFiveGrams_2, removeBlanks
from Name.classifier_utils import vectoriseData, insertColumn, loadModel, predict, getLabels
from Name.classifier_utils import save_obj, load_obj, predictMain, getLabelsMain, getfivegrams
from Name.classifier_utils import svm_predict

from Name.polyglot_utils import getName

######################################
######################################
### SVM on Polyglot
######################################

def get_name(t):
    vocabData = load_obj('vocabData')
    if (isinstance(t, str)) and (t.strip()!=""):
        pn = str(getName(t))
        if not pn=="no name":
            xp, x_mid = getfivegrams(t, pn)
            xp = pd.DataFrame(xp)

            model = loadModel()
            labels_output, labels_confidence = predictMain(model, vocabData, xp)
            labels = getLabelsMain(labels_output, labels_confidence, x_mid)
        else:
            labels = "[]"
    else:
        labels = "[]"
    return labels

