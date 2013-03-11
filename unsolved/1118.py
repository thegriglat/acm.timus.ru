#!/usr/bin/python

def getDel(N):
    ans = []
    for i in xrange(1,N // 2 + 1):
        if N % i == 0:
            ans.append(i)
    return ans
    
def getTriv(N):
    ans = getDel(N)
    return sum(ans) / (0.0 + N)

(I, J) = raw_input().rstrip().split(" ")
I = int(I)
J = int(J)
minn = None
mint = getTriv(I)
for i in xrange(I,J + 1):
    temp = getTriv(i)
    if temp < mint:
        mint = temp
        minn = i
print minn