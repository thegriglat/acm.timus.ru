#!/usr/bin/python

import sys,numpy
sys.stdin = open("1047.txt", "r")
N = int(sys.stdin.readline().rstrip())
a0 = float(sys.stdin.readline().rstrip())
an1 = float(sys.stdin.readline().rstrip())
c = [float(sys.stdin.readline().rstrip()) * (-1)  for x in xrange(0,N)]
c = [a0] + c + [an1]
a = [0 for x in xrange(N+2)]
a[N + 1] = an1
a[0] = a0
A = numpy.matrix([[ 0 for j in xrange(N + 2)] for i in xrange(N + 2)])
B = (numpy.matrix(c)).transpose()
ma = A.tolist()
ma[0][0] = 1
ma[N + 1][N + 1] = 1
for i in xrange(1,N + 1):
    ma[i][i - 1] = -0.5
    ma[i][i] = 1
    ma[i][i + 1] = -0.5 
A = numpy.matrix(ma)
X = A.getI() * B
print  "%.2f" % X.tolist()[1][0]

