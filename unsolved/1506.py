#!/usr/bin/python

import sys
#sys.stdin = open("1506.txt")

def tospace(s):
    return " " * (4 - len(s)) + s

(N,K) = sys.stdin.readline().rstrip().split(" ")
N = int(N)
K = int(K)
arr = sys.stdin.readline().rstrip().split(" ")
for i in xrange(len(arr)):
    arr[i] = tospace(arr[i])
#print arr
i = 0
stolb = 1
for i in xrange(1,N):
    if i * K >= N:
        stolb = i
        break
#print stolb
i = 0
if K == 1:
    stolb = N
while i < stolb:
#for i in  xrange(K):
    s = ""
    j = 0
    while i + j * stolb < N:
        # join all arr[i + K * j]
        try:
            s = s + arr[i + j * stolb]
        except:
            pass
        #print i + (N//K) * j, arr[i +  (N // K) * j]
        j += 1   
    print s
    i += 1
    
