def dateExist(sentence):
    import pickle
    import numpy as np

    vectorizer = pickle.load(open('vectorizer','rb'))
    dateModel = pickle.load(open('dateModel','rb'))
    monthModel  = pickle.load(open('monthModel','rb'))
    yearModel = pickle.load(open('yearModel','rb'))

    inputX = np.array([sentence])
    x_Encoded = np.array([vectorizer.transform(inputX).toarray().squeeze()])

    dateP = dateModel.predict(x_Encoded)
    monthP = monthModel.predict(x_Encoded)
    yearP = yearModel.predict(x_Encoded)

    if(dateP!=0 or monthP!=0 or yearP!=0):
        return 1
    else:
        return 0
