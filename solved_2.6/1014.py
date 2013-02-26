#!/usr/bin/python
def deliteli(N):
    d = {}
    for i in xrange(10):
        d[i] = 0
    if N == 0:
        return ([],True)
    for i in xrange(2, 10,1):
        while N % i == 0:
            d[i] += 1
            N = N / i
    if N == 1:
        return (d,True)
    else:
        return (d,False)
            
def getN(d):
    s = ""
    for i in d.iterkeys():
        for j in xrange(d[i]):
            s += str(i)
    if s != "":
        return s
    else:
        return 1

def SafePlus(key,value):
    global d
    if d.get(key) != None:
        d[key] += value
    else:
        d[key] = value
def RemZero():
    global d
    for i in xrange(10):
        if i in d.keys() and d[i] <= 0:
            del d[i]

def RemDupl():
    global d
    if d.get(2) >= 3:
        SafePlus(8,1)
        d[2] -= 3
    if d.get(3) >= 2:
        SafePlus(9,1)
        d[3] -= 2
    if d.get(4) >= 1 and d.get(2) >= 1:
        SafePlus(8,1)
        d[4] -= 1
        d[2] -= 1
    if d.get(2) >= 1 and d.get(3) >= 1:
        SafePlus(6,1)
        d[3] -= 1
        d[2] -= 1
    if d.get(2) >= 2:
        SafePlus(4,1)
        d[2] -= 2

N = int(raw_input().rstrip())
(d,stat) = deliteli(N)
ans = 10
if d != [] and stat == True : 
    oldd = None
    while oldd != d:
       oldd = d.copy()
       RemDupl()
    RemZero()
    ans = getN(d)
if N == 0:
    ans = 10 
if 1 <= N <= 9:
    ans = N
if stat == False:
    ans = -1
if ans == 0:
    ans = -1
print ans
