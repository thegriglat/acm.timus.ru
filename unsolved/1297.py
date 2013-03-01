#!/usr/bin/python
import sys

#a = sys.stdin.readline().rstrip()
a = "ThesampletextthatcouldbereadedthesameinbothordersArozaupalanalapuazorA"
a = " " + a + " "
d = []
for i in xrange(len(a)):
    for j in xrange(len(a)):
        if a[i:j] == a[j-1:i-1:-1] and a[i:j] != "":
            d.append(a[i:j])
maxl = max(len(s) for s in d)
q = []
for i in d:
    if len(i) == maxl:
        q.append(i)
del d
idx = []
for i in q:
    idx.append(a.index(i))
print q[idx.index(min(idx))]