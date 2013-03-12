#!/usr/bin/python
import math

def layer(n):
    if int(math.sqrt(n)) ** 2 == n:
        return int(math.sqrt(n))
    else:
        return int(math.sqrt(n)) + 1

def gethorlayer(n):
    return (layer(n) ** 2 - n) // 2 + 1

def moveLeft(i):
    if i != (layer(i) - 1) ** 2 + 1:
        return i - 1
    else:
        return None
def moveRight(i):
    if i != layer(i) ** 2:
        return i + 1
    else:
        return None
def moveUp(i):
    return (layer(i) - 2) ** 2 + i - (layer(i) - 1) ** 2  - 1
def moveDLeft(i):
    if (i - (layer(i) - 1) ** 2) % 2 == 0:
        return moveUp(i)
    else:
        return moveUp(moveLeft(i))
def moveDRight(i):
    if (i - (layer(i) - 1) ** 2) % 2 == 0:
        return moveUp(i)
    else:
        return moveUp(moveRight(i))



a = raw_input().rstrip().split(" ")
for i in xrange(len(a)):
    a[i] = int(a[i])
n = max(a)
m = min(a)
del a
lm = layer(m)
ln = layer(n)
i = n
step = 0


# GET split level of n
##d = []
##for L in xrange(1,ln + 1):
##    l = gethorlayer(n)
##    if l <= L: 
##        d.append(L**2 - 2*(l - 1))
##        if l != L:
##            d.append(L**2 - 2*(l - 1) - 1)
##del d[d.index(n)]
##d.sort()
###print d
##a = [abs(x - m) for x in d]
##step = len(a[a.index(min(a)):]) + min(a)
###print min(a), a[a.index(min(a))]

# ERRO