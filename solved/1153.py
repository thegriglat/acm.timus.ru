#!/usr/bin/python

def isSimple(N):
    for i in xrange(2,N//2):
        if N % i == 0:
            return False
    return True

N = int(raw_input().rstrip())
d = {}
print isSimple(N)
