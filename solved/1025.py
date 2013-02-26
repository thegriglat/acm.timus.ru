#!/usr/bin/python
import sys
sys.stdin = open("1025.txt","r")
N = input()
p = [int(x) for x in raw_input().rstrip().split(" ")]

p.sort()
ans = 0
sp = sum(p)
lp = len(p)
t = 0
while t < 0.5 * lp:
    j = p.pop(0)
    ans += j // 2 + 1
    t += 1

print ans
