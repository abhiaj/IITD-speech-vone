def find_between(df, col, v1, v2):
    vals = df[col].values
    mx1, mx2 = (vals == v1).argmax(), (vals == v2).argmax()
    idx = df.index.values
    i1, i2 = idx.searchsorted([mx1, mx2])
    if(v2==36):
        return df.iloc[i1:]
    else:
        return df.iloc[i1:i2]

def SortTuples(tup):
    n = len(tup) 
    for i in range(n): 
        for j in range(n-i-1): 
            if tup[j][0] > tup[j + 1][0]: 
                tup[j], tup[j + 1] = tup[j + 1], tup[j]              
    return tup 

def removeDuplicates(tup):
    tup = [(alpha, set(st), set(dst), set(subdst), val) for (alpha, st, dst, subdst, val) in tup]
    res = []
    eq_idxs = set()
    for i in range(len(tup)):
        isSubset = False
        isEq = False
        for j in range(len(tup)):
            if i != j:
                if tup[i][1] == tup[j][1] and tup[i][2] == tup[j][2] and tup[i][3] == tup[j][3]:
                    isEq = True
                    eq_idxs.add(j)
                    continue
                if tup[i][1].issubset(tup[j][1]) and tup[i][2].issubset(tup[j][2]) and tup[i][3].issubset(tup[j][3]):
                    isSubset = True
                    break
        if not isSubset:
            if isEq:
                if i not in eq_idxs:
                    eq_idxs.add(i)
                    res.append(tup[i])
            else:
                res.append(tup[i])
    tup = [(alpha, list(st), list(dst), list(subdst), val) for (alpha, st, dst, subdst, val) in res]
    return tup