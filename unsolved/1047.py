#!/usr/bin/python

import sys

def MatToTriang(G,changeB=True):
    A = list(G)
    global B
    for i in xrange(len(A) - 2,-1,-1):
        k = A[i][i + 1] / (A[i + 1][i+1] + 0.0)
        if changeB:B[i][0] -= k * B[i+1][0]
        for j in xrange(len(A)):
            A[i][j] -= k * A[i+1][j]    
    return A
##    for i in xrange(1,len(G)):
##        k = A[i][i - 1] / (A[i - 1][i - 1] + 0.0)
##        #modify B too
##        if changeB: B[i][0] -= k * B[i-1][0]
##        for j in xrange(i - 1,len(A)):
##            A[i][j] -= k * A[i - 1][j]
##    return A

##def Minor(A,i,j):
##    B = []
##    for z in A[0:i] + A[i+1:]:
##        B.append(z[0:j] + z[j + 1:])
##    return B
##
##def MatDet(A,triangle=False):
##    if len(A) == 1:
##        return A[0][0]
##    if len(A) == 2:
##        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
##    if triangle:
##        t = 1
##        for i in xrange(len(A)):
##            t *= A[i][i]
##        return t
##    D = 0
##    for i in xrange(len(A)):
##        D += A[0][i] * MatDet(Minor(A,0,i)) * (-1) ** i
##    return D
##
##def MatMul(A,B):
##    return [[sum([A[i][n]*B[n][j] for n in xrange(len(A[0]))]) for j in xrange(len(B[0]))] for i in xrange(len(A))]
##
##def Transpose(A):
##    return map(list,zip(*A))
##
##def MatInv(A,triangle=False):
##    D = MatDet(A,triangle)
##    if D == 0:
##        return None
##    M = [[((-1)**(i + j)) * MatDet(Minor(A,i,j))/(0.0 + D) for j in xrange(len(A))] for i in xrange(len(A))]
##    return Transpose(M)
    
sys.stdin = open("1047.txt", "r")
N = int(sys.stdin.readline().rstrip())
a0 = float(sys.stdin.readline().rstrip())
an1 = float(sys.stdin.readline().rstrip())
a = [a0] + [0]*N + [an1]
c = [float(sys.stdin.readline().rstrip()) * (-2)   for x in xrange(0,N)]
A = [[ 0 for j in xrange(N)] for i in xrange(N)]
c[0] += a0
c[N - 1] += an1
B = [[c[i]] for i in xrange(len(c))]
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
A = MatToTriang(A,True)
##print 2, numpy.matrix(A)
##print 3, numpy.matrix(B)
##X = MatMul(MatInv(A,True) , B)
##print 4, numpy.matrix(X)
##print  "%.2f" % X[0][0]
print "%.2f" % (B[0][0] / (0.0 + A[0][0]))
###a1 + an = -(2*sc - a0 - an1)
##a1 = - 0.5*(2*sum(c) - a0 - an1)
##print "%.2f" % a1
