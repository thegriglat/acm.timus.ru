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
        #print a ** 2, b**2
        if int(b) == b:
            return 2
        i += 1
    stop = int(math.sqrt(n)) + 1
    m = 0
    i = [0] * 3
    for i[0] in xrange(stop,0,-1):
        for i[1] in xrange(1,i[0]):
            for i[2] in xrange(stop):
                if sum([i[x] ** 2 for x in xrange(3)])  == n:
                    return 3
    return 4

N = input()
print getL(N)
