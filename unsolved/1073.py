#!/usr/bin/python

import sys,math
N = input()
i = [0,0,0,0]
a = (math.sqrt(N) // 1 + 1)
m = 6
s = [0, 1, 2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
 59, 61, 67 , 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131,137,
 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
 227, 229, 233, 239, 241, 251]

for i[0] in s:
    if i[0] > a:break
    for i[1] in s:
        if i[1] > a:break
        for i[2] in s:
            if i[2] > a:break
            for i[3] in s:
                if i[3] > a:break
                if i[0]**2 + i[1]**2 + i[2]**2 + i[3]**2 == N:
                    if 4 - i.count(0) < m:
                        m = 4 - i.count(0)
print m