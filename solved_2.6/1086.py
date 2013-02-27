#!/usr/bin/python
import sys
import math
def issimple(i):
    for j in xrange(2,math.trunc(math.sqrt(i)) + 1):
        if i % j == 0:
            return False
    return True

countN = int(sys.stdin.readline().rstrip())
N = []
for i in xrange(countN):
    N.append(int(sys.stdin.readline().rstrip()))

simple = [1,2,3]
i = 5
while len(simple) <= 15000:
    if issimple(i):
        simple.append(i)
    i += 2  
for i in N:
    print simple[i]
