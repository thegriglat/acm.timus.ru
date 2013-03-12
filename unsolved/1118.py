#!/usr/bin/python
import math
def getTriv(N):
    ans = []
    for i in xrange(1,N // 2 + 1):
        if N % i == 0:
            ans.append(i)
    return sum(ans) / (0.0 + N)

def getDelit(N):
    ans = [1]
    M = N
    m = N // 2 + 1#int(math.sqrt(N)) + 1
    i = 2
    while 2 <= i <= m:
        while M % i == 0:
            ans.append(i)
            M = M / i
        i += 1
    ans = expand(ans,N)
    if M == 1:
        return ans
    elif M != N:
        return ans + [M]
    else:
        return ans
    
def expand(d,N):
    d = list(set(d))
    #print d
    l = len(d)
    a = d[:]
    for i in xrange(1,l):
        for j in xrange(i,l):
            if N % (d[i] * d[j]) == 0 and d[i] * d[j] < N:
                a.append(d[i] * d[j])
    return list(set(a))
        
(I, J) = raw_input().rstrip().split(" ")
I = int(I)
J = int(J)
minn = None
mint = 10000
i = J
step = -1
while I <= i <= J: 
    if I == 1:
        minn = 1
        break
    delit = getDelit(i)
    if len(delit) == 1:
        if (1 / (1.0 + i) <= mint):
            minn = i
            break
    triv = sum(delit) / (0.0 + i)
    #print i, delit,triv
    if triv <= mint:
        mint = triv
        minn = i
    if i % 2 != 0 and step != -2:
        step = -2
    i += step
print minn
