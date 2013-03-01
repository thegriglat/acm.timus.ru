#!/usr/bin/python

import sys

def MatToTriang():
    global A
    global B
    for i in xrange(len(A) - 2,-1,-1):
        k = A[i][i + 1] / (A[i + 1][i+1] + 0.0)
        B[i][0] -= k * B[i+1][0]
        for j in xrange(i - 1, i+2):    ##len(A)):
            A[i][j] -= k * A[i+1][j] 
    #return A
    
sys.stdin = open("1047.txt", "r")
N = int(sys.stdin.readline().rstrip())
a0 = float(sys.stdin.readline().rstrip())
an1 = float(sys.stdin.readline().rstrip())
#a = [a0] + [0]*N + [an1]
c = [float(sys.stdin.readline().rstrip()) * (-2)   for x in xrange(0,N)]
A = [[ 0 for j in xrange(N)] for i in xrange(N)]
c[0] += a0
c[N - 1] += an1
B = [[c[i]] for i in xrange(len(c))]
del c
##print numpy.matrix(B)
##
##B.insert(0,[a0])
##B.append([an1])
##
##A[0][0] = 1
##A[N + 1][N + 1] = 1
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
##print 1, numpy.matrix(A)
MatToTriang()
##print 2, numpy.matrix(A)
##print 3, numpy.matrix(B)
##X = MatMul(MatInv(A,True) , B)
##print 4, numpy.matrix(X)
##print  "%.2f" % X[0][0]

print "%.2f" % (B[0][0] / (0.0 + A[0][0]))
##print "%.2f" % (c[0] / (0.0 + A[0][0]))
###a1 + an = -(2*sc - a0 - an1)
##a1 = - 0.5*(2*sum(c) - a0 - an1)
##print "%.2f" % a1
