#!/usr/bin/python

import sys,math

def getL(n):
    if int(math.sqrt(N)) ** 2 == N:
        return 1
    i = 0
    while int(math.sqrt(N)) - i > 0:
        b = math.sqrt(N - int(math.sqrt(N)) ** 2)
        if int(b) == b:
            return 2
        i += 1
  
    stop = int(math.sqrt(n)) + 1
    m = 0
    i = [0] * 3
    for i[0] in xrange(stop):
        for i[1] in xrange(i[0],stop):
            for i[2] in xrange(i[1],stop):
                if sum([i[x] ** 2 for x in xrange(3)])  == n:
                    return 3
    return 4

N = input()
print getL(N)
