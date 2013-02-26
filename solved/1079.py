#!/usr/bin/python
import sys
def addai(key,value):
    global ai
    if key in ai.keys():
        return None
    else:
        ai[key] = value

def getai(n):
    global ai
    if n in ai.keys():
        return ai[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n % 2 == 0:
        i = int(n / 2)
        temp = getai(i)
        addai(n,temp)
        return temp
    else:
        i = n // 2 
        temp = getai(i) +getai(i+1)
        addai(n,temp)
        return temp

line = int(sys.stdin.readline().rstrip())
a = []
a.append(line)
while (line != 0):
     line = int(sys.stdin.readline().rstrip())
     a.append(line)
ai = {0:0,1:1}
a.pop(len(a) - 1)
for i in xrange(2,max(a) + 1):
    if i % 2 == 0:
        ai[i] = ai[int(i//2)]
    else:
        ai[i] = ai[int(i//2)] + ai[int(i//2)+1]

for test in a:
    maxi = 0
    for i in xrange(0,test + 1):
        t = ai[i]
        if t > maxi:
            maxi = t
    print maxi
