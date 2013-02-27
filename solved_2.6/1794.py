#!/usr/bin/python
from sys import stdin
dict

N = int(stdin.readline().rstrip())
a = [int(x) for x in stdin.readline().rstrip().split(" ")]
mini = 1e10
b = [0 for i in xrange(len(a))]
for i in xrange(len(a)):
    j = i - a[i]  + 1
    if j < 0:
        j += len(a)
    b[j] += 1
print b.index(max(b)) + 1

