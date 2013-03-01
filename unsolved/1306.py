#!/usr/bin/python

import sys

def getMediana(A,sorted=False):
    if not sorted:
        A.sort()
    if len(A) % 2 != 0:
        return A[len(A) // 2]
    else:
        return 0.5 * (A[len(A)//2 - 1] + A[len(A) // 2])

sys.stdin = open("1306.txt")

N = input()
n = []
for i in xrange(N):
    temp = input()
    n.append(temp)

print getMediana(n) if N < 100 else print 0