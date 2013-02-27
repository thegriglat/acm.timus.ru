#!/usr/bin/python
import sys
import math
def getLine(p1,p2):
    (x1,y1) = p1
    (x2,y2) = p2
    if x2 - x1 != 0:
        k = (y2 - y1) / float(x2 - x1)
    else :
        k = 0
    b = y1 - k * x1
    return (k,b)

def getAddB(k, R):
    phi = math.atan(k)
    return R * math.cos(phi)
def getConnect(p1,R1,p2):
    (x,y) = p1
    addb = getAddB(getLine(p1,p2)[0],R1)
    xc = math.sqrt(R1**2 - addb ** 2) + x
    yc = addb + y
    return (xc,yc)

def getDist(p1,p2):
    (x1,y1) = p1
    (x2,y2) = p2
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)
def getLineSector(Opoint,p1,p2,R):
    k1 = getLine(Opoint,p1)[0]
    k2 = getLine(Opoint,p2)[0]
    k = abs(k2 - k1)
    if k == 0 and getLine(p1,p2)[0] == 0:
        return math.pi * R
    elif k == 0:
        return math.pi * R * 0.5
    return R * math.atan(k)

sys.stdin = open("1020.txt","r")
(N,R) = sys.stdin.readline().rstrip().split()
N = int(N)
R = float(R)
coord = []    
for i in xrange(N):
     x,y = sys.stdin.readline().rstrip().split()
     x = float(x)
     y = float(y)
     coord.append((x,y))
sumline = 0
for i in xrange(N):
    j = i + 1
    n = i - 1
    if i + 1 >= N: j = 0
    if i - 1 < 0: n = N - 1
    sumline += getDist(
            getConnect(
                coord[i],
                R,
                coord[j]),
            getConnect(
                coord[j],
                R,
                coord[i]))
#    sumline += 0.5 * getLineSector(
#            coord[i],
#            getConnect(
#                coord[i],
#                R,
#                coord[j]
#                ),
#            getConnect(
#                coord[i],
#                R,
#                coord[n]
#                ),R)
sumline += 2 * math.pi * R
print("%.2f" % sumline)
