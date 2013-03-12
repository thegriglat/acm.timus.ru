#!/usr/bin/python

import sys,math

def getL(n):
    stop = int(math.sqrt(n)) + 1
    m = []
    i = [0] * 4
    for i[0] in xrange(stop):
        if i[0] ** 2 == N:
            m.append(1)
        for i[1] in xrange(i[0],stop):
            if sum([i[x] ** 2 for x in xrange(2)]) == N:
                m.append(2)
            for i[2] in xrange(i[1],stop):
                if sum([i[x] ** 2 for x in xrange(3)])  == N:
                    m.append(3)
                for i[3] in xrange(i[2],stop):
                    if sum([i[x] ** 2 for x in xrange(4)])  == N:
                        m.append(4)
                    #print i, sum([i[x] ** 2 for x in xrange(4)])
    return min(m)




N = input()
print getL(N)
