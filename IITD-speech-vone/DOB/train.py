import pandas as pd
import numpy as np
data1 = pd.read_csv('file1.csv')
date1 = data1['Transcript(Hindi by google library)']
groundTruthDate=data1['gTruthDate']
groundTruthMonth=data1['gTruthMonths']
groundTruthYear=data1['gTruthYears']
originalDate = data1['Date Original']
originalMonth = data1['Month Original']
originalYear = data1['Year Original']


#Setting up for different months
rawMonths=['जनवरी','फरवरी','मार्च','अप्रैल','मई','जून','जुलाई','अगस्त','सितंबर','अक्टूबर','नवंबर','दिसंबर']
hindiMonths=['चैत्र','बैसाख','ज्येष्ठ','आषाढ़','सावन','भाद्रपद','आश्विन','कार्तिक','अग्रहायण','पौष','माघ','फाल्गुन']
hindiMonthsDict = {i:j for (j,i) in enumerate(hindiMonths)}
hindiMonthPrefix=['पहला','दूसरा','तीसरा','चौथा','पांचवां','छठा','सातवां','आठवां','नौवां','दसवां','ग्यारहवां','बारहवां']
hindiMonthPrefixDict = {i:j for (j,i) in enumerate(hindiMonthPrefix)}

truthMonths,truthDates,dates,months=[],[],[],[]
check,total=0,0


for sentence in date1:
#     sentence = "हमारे यहां बच्चा का उम्र 3 साल 2 महीना"
    flag=0
    for month in rawMonths:
        if month in sentence:
            truthMonths.append(1)
            months.append(month)
            flag=1
            break

    if(flag!=1):
        truthMonths.append(0)
        months.append('-1')

    #Now checking for months in hindi
    if flag==0:
        for month in hindiMonths:
            if month in sentence:
                truthMonths[-1]=1
                months[-1]=month #rawMonths[hindiMonthsDict[month]]
                flag=1
                break

    item=sentence.replace("-"," ").split()

#     # Near string matching for hindi months and english months
#     if flag==0:
#         for i in range(len(item)):
#             #Here monthVal can be two things only 1 or 0 as our function returns these things only.
#             monthRet,monthVal=compareStrings(item[i],rawMonths)

#             if monthVal==1:
#                 truthMonths[-1]=1
#                 months[-1]=monthRet
#                 flag=1
#                 break
#             else:
#                 hindiMonRet,hindiMonVal=compareStrings(item[i],hindiMonths)
#                 if hindiMonVal==1:
#                     truthMonths[-1]=1
#                     months[-1]=hindiMonRet
#                     flag=1
#                     break


    #Now for hindi prefix like pehla mahina, dusra mahine, teesra mahina and continued till 12th months

    if(len(item)>=2):
        for i in range(len(item)-1):
            if item[i] in hindiMonthPrefix and (item[i+1]=='महीना' or item[i+1] == "महिना"):
                if flag==0:
                    truthMonths[-1]=1
                    months[-1] = item[i] #rawMonths[hindiMonthPrefixDict[item[i]]]
                    flag=1
                    break

    total+=len(item)

    #For Months
    if(len(item)>=2):
        for i in range(len(item)-1):
                if item[i].isdigit() and item[i+1].isdigit() and len(item[i])!=4 and len(item[i+1])!=4:
                    if flag==0:
                        if (int(item[i+1])) <= 12:
                            truthMonths[-1]=1
                            months[-1] = item[i+1]  #rawMonths[int(item[i+1])-1]
                            flag=1
                            break
                elif item[i].isdigit() and item[i+1].isdigit() and len(item[i])!=4 and len(item[i+1])==4:
                    if flag==0:
                        if len(item[i])==1 and int(item[i])!=0:
                            truthMonths[-1]=1
                            months[-1] = item[i] #rawMonths[int(item[i])-1]
                            flag=1
                            break
                        elif len(item[i])==3:
                            if int(item[i][:2]) <= 31 and int(item[i][2]) != 0:
                                truthMonths[-1]=1
                                months[-1] = item[i][2]  #rawMonths[int(item[i][2])-1]
                                flag = 1
                                break
                            elif int(item[i][:2]) <= 31 and int(item[i][2]) == 0:
                                if int(item[i][1])==1:
                                    truthMonths[-1]=1
                                    months[-1] = item[i][1:] #rawMonths[int(item[i][1:])-1]
                                    flag = 1
                                    break
                        elif len(item[i])==2:
                            if int(item[i])<=12:
                                truthMonths[-1]=1
                                months[-1] = item[i] #rawMonths[int(item[i])-1]
                                flag=1
                                break
                            else:
                                truthMonths[-1]=1
                                months[-1] = item[i][1] #rawMonths[int(item[i][1])-1]
                                flag = 1
                                break
                        else:
                            z = 2 #dummy

                elif item[i].isdigit() and item[i+1].isdigit() and len(item[i])==4 and len(item[i+1])==4:
                    if flag==0:
                        if int(item[i+1]) <= 2100 and int(item[i+1]) >= 1900:
                            if int(item[i][2:]) <= 12:
                                truthMonths[-1]=1
                                months[-1] = item[i][2:] #rawMonths[int(item[i][2:])-1]
                                flag = 1
                                break
                else:
                    z=2 #Dummy

#     if truthMonths[-1]==1:
#         trainMonthOut.append(1)
#     else:
#         trainMonthOut.append(0)

    flagDate=0
    if len(item)>=2:
        for i in range(len(item)-1):
                if item[i].isdigit() and item[i+1].isdigit() and len(item[i])!=4 and len(item[i+1])!=4:
                    if flagDate==0:
                        truthDates.append(1)
                        dates.append(item[i])
                        flagDate=1
                        break
                elif item[i].isdigit() and len(item[i])!=4 and not item[i+1].isdigit() and int(item[i])<32:
                    if flagDate==0:
                        suppList = ["साल","महीना","महिना"]
                        if not(item[i+1] in suppList):
                            truthDates.append(1)
                            dates.append(item[i])
                            flagDate=1
                            break
                elif item[i].isdigit() and item[i+1].isdigit() and len(item[i])!=4 and len(item[i+1])==4:
                    if flagDate==0:
                        if len(item[i])==3:
                            if int(item[i][:2]) <= 31 and int(item[i][2]) != 0:
                                truthDates.append(1)
                                dates.append(item[i][:2])
                                flagDate = 1
                                break
                            elif int(item[i][:2]) <= 31 and int(item[i][2]) == 0:
                                if int(item[i][1])==1:
                                    truthDates.append(1)
                                    dates.append(item[i][0])
                                    flagDate = 1
                                    break
                        elif len(item[i])==2:
                            if int(item[i])<=12:
                                z = 2 #Do  nothing
                            else:
                                truthDates.append(1)
                                dates.append(item[i][0])
                                flagDate = 1
                                break
                        else:
                            z = 2 #dummy
                elif item[i].isdigit() and item[i+1].isdigit() and len(item[i])==4 and len(item[i+1])==4:
                    if flagDate==0:
                        if int(item[i+1]) <= 2100 and int(item[i+1]) >= 1900:
                            if int(item[i][2:]) <= 12:
                                truthDates.append(1)
                                dates.append(item[i][:2])
                                flagDate = 1
                                break
                else:
                    z=2

    if flagDate==0:
        truthDates.append(0)
        dates.append('-1')
        flagDate=1

#Now for year

truthYears,years=[],[]
for sentence in date1:
    flagYear = 0
    for items in sentence.replace("-"," ").split():
        try:
            if len(items) == 4 and int(items) > 1900 and int(items) < 2100:
                truthYears.append(1)
                years.append(items)
                flagYear=1
                break
        except:
            z=2 #Dummy z
    if flagYear!=1:
        words = sentence.replace("-"," ").split()
        for i in range(len(words)-2):
            try:
                if (type(int(words[i])) == int)  and (type(int(words[i+1]))==int) and (type(int(words[i+2]))==int):
                    if len(words[i+2])==2:
                        truthYears.append(1)
                        if int(words[i+2]) > 50:
                            years.append("19"+words[i+2])
                        else:
                            years.append("20"+words[i+2])
                        flagYear = 1
                        break
            except:
                z=2
    if flagYear!=1:
        words = sentence.replace("-"," ").split()
        for i in range(len(words)-1):
            if words[i] in rawMonths or words[i] in hindiMonths or words[i] in hindiMonthPrefix:
                if words[i+1].isdigit() and len(words[i+1])==2:
                    if int(words[i+1])>=50:
                        truthYears.append(1)
                        years.append("19"+str(words[i+1]))
                    else:
                        truthYears.append(1)
                        years.append("20"+str(words[i+1]))
                    flagYear =1
                    break


    if flagYear!=1:
        truthYears.append(0)
        years.append('-1')


#Now the training of models -> data, month and year

dataInputForm=[]
for sentence in date1:
    dataInputForm.append(np.array(sentence.split()))
# dateInputForm=np.asarray(dataInputForm)

from sklearn import svm
import nltk
nltk.download('punkt')
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
# x=date1.to_numpy()

words = []
for x in date1:
    w = nltk.word_tokenize(str(x))
    words.extend(w)

words = list(set(words))

vectorizer = CountVectorizer()
vectorizer.fit(words)
print("Encoder Done")

import pickle
pickle.dump(vectorizer,open('vectorizer','wb'))

inputX=date1.to_numpy()
print(inputX.shape)

sampleX_enc = np.array([vectorizer.transform(x).toarray().squeeze() for x in [inputX]])[0]

yDate=truthDates
yMonth=truthMonths
yYear=truthYears

# yDate = originalDate
# yMonth = originalMonth
# yYear = originalYear

dateModel=svm.SVC(C=1.0,gamma=0.05,kernel='rbf')
monthModel=svm.SVC(C=1.0,gamma=0.05,kernel='rbf')
yearModel=svm.SVC(C=1.0,gamma=0.05,kernel='rbf')

dateModel.fit(sampleX_enc,yDate)
monthModel.fit(sampleX_enc,yMonth)
yearModel.fit(sampleX_enc,yYear)

pickle.dump(dateModel,open('dateModel','wb'))
pickle.dump(monthModel,open('monthModel','wb'))
pickle.dump(yearModel,open('yearModel','wb'))
