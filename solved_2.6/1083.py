#!/usr/bin/python

import sys,math

line = sys.stdin.readline().rstrip()
(n,kf) = line.split()
k = len(kf)
n = int(n)
del kf
N = 1
i = 0
for i in xrange(n // k):
    N *= (n - i * k)
if n % k != 0:
    N *= n % k

print N
