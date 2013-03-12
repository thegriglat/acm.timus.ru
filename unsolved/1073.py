#!/usr/bin/python

import sys,math

def getL(n):
    if int(math.sqrt(N)) ** 2 == N:
        return 1
    stop = int(math.sqrt(n)) + 1
    m = 0
    i = [0] * 3
    for i[0] in xrange(stop):
##        if i[0] ** 2 == n:
##            m.append(1)
        for i[1] in xrange(i[0],stop):
            if sum([i[x] ** 2 for x in xrange(2)]) == n:
                return 2
##                m.append(2)
            for i[2] in xrange(i[1],stop):
                if sum([i[x] ** 2 for x in xrange(3)])  == n:
                    ##m.append(3)
                    m = 1
    if m == 1:
        return 3
    else:
        return 4

N = input()
d = []

print getL(N)
