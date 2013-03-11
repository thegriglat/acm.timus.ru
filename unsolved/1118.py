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
if I % 2 == 0 and J - I >= 2:
    step = 2
    start = I + 1
elif I % 2 != 0 and J - I >=2:
    start = I
    step = 2
else:
    step = 1
    start = I
    
for i in xrange(start,J + 1,step):
    temp = getTriv(i)
    #print i, temp
    if temp <= mint:
        mint = temp
        minn = i
print minn