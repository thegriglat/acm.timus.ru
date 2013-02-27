#!/usr/bin/python

import math
N = input()
i = [0,0,0,0]
a = int(math.sqrt(N))
m = 5
for i[0] in xrange(a):
    for i[1] in xrange(a):
        for i[2] in xrange(a):
            for i[3] in xrange(a):
                if i[0]**2 + i[1]**2 + i[2]**2 + i[3]**2 == N:
                    if 4 - i.count(0) < m:
                        m = 4 - i.count(0)

print m