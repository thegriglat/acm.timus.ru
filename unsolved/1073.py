#!/usr/bin/python

import math
N = input()
i = 0
while N > 0:
    N -= (math.sqrt(N) // 1) ** 2
    i += 1
print i