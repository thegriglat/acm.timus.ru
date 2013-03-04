#!/usr/bin/python
import sys

def getDistSimple(path,ppr,ppl):
    global x
    coord = 0
    i = 0
    if path == 1:
        pp = 1
    else:
        pp = -1
    while coord != x:
        if pp == 1:
            bord = ppr
        else:
            bord = ppl
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
ppr = 1000
ppl = -1000
for i in xrange(len(p)):
    if p[i] < ppr and p[i] > 0:
        ppr = p[i]
    if p[i] > ppl and p[i] < 0:
        ppl = p[i]
dist = 0
if x > ppr or x < ppl:
    print  "Impossible"
else:
    print getDistSimple(1,ppr,ppl), getDistSimple(-1,ppr,ppl)
