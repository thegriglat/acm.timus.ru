#!/usr/bin/python

import sys
            
def M2T():
    global B
    global N
    k = 0
    a = 2
    for i in xrange(N - 2,-1,-1):
        a = 2 + k
        k = -1 / (a + 0.0)
        B[i] -= k * B[i+1]
    k = -1 / (0.0 + a)
    if N != 1: a = 2 + k
    return  B[0] / (0.0 + a )
    
sys.stdin = open("1047.txt", "r")
N = int(sys.stdin.readline())
a0 = float(sys.stdin.readline())
an1 = float(sys.stdin.readline())
B = [float(sys.stdin.readline()) * (-2)   for x in xrange(0,N)]
B[0] += a0
B[N-1] += an1
print "%.2f" % (M2T())