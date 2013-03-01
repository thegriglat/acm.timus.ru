#!/usr/bin/python

import sys
##TODO rewrite to A is tuple
##def MatToTriang():
##    global A
##    global B
##    testk = 1
##    for i in xrange(len(A) - 2,-1,-1):
##        k = A[i][i + 1] / (A[i + 1][i+1] + 0.0)
##        testk *= k
##        B[i] -= k * B[i+1]
##        print "i = %d\tk = %f\tt = %f" % (i,k,testk)
##        for j in xrange(i - 1, i+2): 
##            A[i][j] -= k * A[i+1][j] 
            
def M2T():
#    global A
    global B
    global N
##    a = 2
##    f = -1 / (0.0 + a)
##    for i in xrange(N-2,-1,-1):
##        a = 2 + f
##        f = -1 / (a + 0.0)
##        B[i] -= f * B[i+1]
##        print "f=%f,a=%f,i=%d" % (f,a,i)
    k = 0
    a = 2
    for i in xrange(N - 2,-1,-1):
        print i
        a = 2 + k
        k = -1 / (a + 0.0)
        #k = A[i][i + 1] / (A[i + 1][i+1] + 0.0)
        B[i] -= k * B[i+1]
#       A[i][i] -= k * A[i + 1][i]
#        print "i = %d\tk = %f\t" % (i,k)
    k = -1 / (0.0 + a)
    if N != 1: a = 2 + k
    return  B[0] / (0.0 + a )
    
sys.stdin = open("1047.txt", "r")
N = int(sys.stdin.readline().rstrip())
a0 = float(sys.stdin.readline().rstrip())
an1 = float(sys.stdin.readline().rstrip())
B = [float(sys.stdin.readline().rstrip()) * (-2)   for x in xrange(0,N)]
A = [[ 0 for j in xrange(N)] for i in xrange(N)]
B[0] += a0
B[N-1] += an1
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
        
ans = M2T()
##MatToTriang()
#print "%.2f" % (ans)
print "%.2f" % (ans)