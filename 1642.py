#!/usr/bin/python
import sys

def getDist(path,pr,pl):
    global x
    coord = 0
    i = 0
    if path == 1:
        pp = 1
    else:
        pp = -1
    while coord != x:
        if pp == 1:
#            try:
                bord = pr.pop(0)
#            except:
#                bord = None
        else:
#            try:
                bord = pl.pop(0)
#            except:
#                bord = None
        while coord != bord :
            coord +=  pp
            i += 1
            if coord == x:
                break
        pp *= -1
    return i

#sys.stdin = open("1642.txt","r")
(n,x) = (int(x) for x in sys.stdin.readline().rstrip().split(" "))
p = [int(j) for j in sys.stdin.readline().split()]
p.sort()
pr = []
pl = []
for i in xrange(len(p)):
    if p[i] >= 0:
        pr.append(p[i])
    else:
        pl.append(p[i])
pl.reverse()
dist = 0
if pr == []:
    pr = [1000]
if pl == []:
    pl = [-1000]
if x > max(pr) or x < min(pl):
    print  "Impossible"
else:
    print getDist(1,pr,pl), getDist(-1,pr,pl)
