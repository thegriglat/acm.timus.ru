#!/usr/bin/python
import sys

sys.stdin = open("1195.txt")

a = [[[]*3]*3]*3
t = sys.stdin.readlines()
print t
idx = -1
for i in t:
    idx += 1
    (a[idx][0],a[idx][1],a[idx][2] )= i.rstrip()

print a