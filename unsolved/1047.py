#!/usr/bin/python

import sys

def MatToTriang():
    global A
    global B
    for i in xrange(len(A) - 2,-1,-1):
        k = A[i][i + 1] / (A[i + 1][i+1] + 0.0)
        #B[i][0] -= k * B[i+1][0]
        B[i] -= k * B[i+1]
        for j in xrange(i - 1, i+2): 
            A[i][j] -= k * A[i+1][j] 
    #return A
    
sys.stdin = open("1047.txt", "r")
N = int(sys.stdin.readline().rstrip())
a0 = float(sys.stdin.readline().rstrip())
an1 = float(sys.stdin.readline().rstrip())
#a = [a0] + [0]*N + [an1]
#B initialize
B = [float(sys.stdin.readline().rstrip()) * (-2)   for x in xrange(0,N)]
#B stop
#c = [float(sys.stdin.readline().rstrip()) * (-2)   for x in xrange(0,N)]
A = [[ 0 for j in xrange(N)] for i in xrange(N)]
B[0] += a0
B[N-1] += an1
#c[0] += a0
#c[N - 1] += an1
#B = [[c[i]] for i in xrange(len(c))]
#del c
for i in xrange(0,N):
    try:
        A[i][i - 1] = -1 ##-0.5
    except:
        pass
    A[i][i] =  2 ##1.0
    try:
        A[i][i + 1] =  -1 ##-0.5
    except:
        pass
MatToTriang()
print "%.2f" % (B[0] / (0.0 + A[0][0]))