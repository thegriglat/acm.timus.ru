#!/usr/bin/python

import sys,math

def getL(n):
    """
    Decomposition of n by Lagrange theorem.
    n = a**2 + b**2 + c**2 + d**2
    """
    if int(math.sqrt(n)) ** 2 == N:
        return 1
    i = 0
    a = 5
    while a > 0:
        a = int(math.sqrt(n)) - i
        b = math.sqrt(n - a ** 2)
        if a < b: break     #Optimize 2x
        #print a, b
        if int(b) == b:
            return 2
        i += 1
    stop = int(math.sqrt(n)) + 1
    m = 0
    i = [0] * 3
    speed = 3
    if N < 81:
        speed = 1
    for i[0] in xrange(1,stop // speed):
        for i[1] in xrange(i[0],stop // speed):
            for i[2] in xrange(i[1],stop):
                #print i
                if sum([i[x] ** 2 for x in xrange(3)])  == n:
                    return 3
    return 4

N = input()
print getL(N)

