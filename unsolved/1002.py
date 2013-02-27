#!/usr/bin/python

import sys,math,itertools,re
sys.stdin = open("1002.txt","r")
def getstdin(Type="str"):
    line = sys.stdin.readline().rstrip()
    if Type == "str":
        return line
    elif Type == "int":
        return int(line)
    elif Type == "float":
        return float(line)
    elif Type == "long":
        return long(line)

def getwords(n):
    global tel
    itn = iter(n)
    tell = []
    words = []
    for c in itn:
        tell.append(tel[int(c)])
    telcomb = itertools.product(*tell)
    for i in telcomb:
        s = ""
        for c in i:
            s += c
        words.append(s)
    return words

def getdata():
    n = getstdin("str")
    if n == "-1":sys.exit(0)
    words = getwords(n)
    dictN = getstdin("int")
    dct = []
    for i in xrange(dictN):
        dct.append(getstdin("str"))
    return (words,dct)

def splitword(word,dct):
    w = word
    tempd = dct
    s = "("
    for i in dct:
        s += i + "|"
    s = s[:-1]
    s += ")?"
    res = []
    s = s * len(dct)
    for d in dct:
        dct = tempd
        for w1 in w:
            if d not in w1: del dct[dct.index(d)]
        for i in re.findall(s,w1):
            result = []
            for j in i:
                if j != "": result.append(j)
            res.append(  str(result)[1:-1].replace(",","").replace("'",""))
    while "" in res: res.remove("")
    res = list(set(res))
    mini = 1000
    minit = ""
    for i in res:
        if len(i.split()) <= mini:
            mini = len(i.split())
            minit = i
    return minit

def resultword(words,dct):
    resultword = []
    for w in words:
        temp = w
        for d in dct:
            temp = temp.replace(d,"")
        if len(temp) == 0:
            resultword.append(w)
    return resultword

tel = [("o","q","z"),
    ("i","j"),
    ("a","b","c"),
    ("d","e","f"),
    ("g","h"),
    ("k","l"),
    ("m","n"),
    ("p","r","s"),
    ("t","u","v"),
    ("w","x","y")]

while True:
    (words,dct) = getdata()
    rword = resultword(words,dct)
    del words
    if len(rword) == 0:
        print "No solution."
    else:
        print splitword(rword,dct)

