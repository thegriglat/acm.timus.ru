#!/usr/bin/python
import sys

l1 = sys.stdin.readline()
del l1
line = sys.stdin.readline().rstrip()
a = line.split()
b = []
for i in a:
    b.append(int(i))

del a
b.sort()
sl = []
m1,m2 = 0,0
c = []
c += b 
m1 = b.pop(len(b) - 1)
while len(b) != 0:
    if m1 >= m2:
        m2 += b.pop(len(b) - 1)
    else:
        m1 += b.pop(len(b) - 1)

for i in xrange(len(c)):
    sl.append(abs(sum(c[i:]) - sum(c[:i])))

if abs(m2-m1) < min(sl):
    print abs(m2-m1)
else:
    print min(sl)
