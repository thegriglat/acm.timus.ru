#!/usr/bin/python
from sys import stdin
N = int(stdin.readline().rstrip())
a = [int(x) for x in stdin.readline().rstrip().split(" ")]
mini = 1e10
for i in xrange(len(a)):
    s = sum(abs(a[x] - i - 1) for x in xrange(len(a)))
    if s < mini:
        idx = i + 1
        mini = s
print idx
