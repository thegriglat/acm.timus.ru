#!/ust/bin/python
import sys
sqr2 = 0.70710678118654757
def Goxy(num):
    global x, y,sqr2
    if num == 8:
        y += 1
    elif num == 2:
        y -= 1
    elif num == 6:
        x += 1
    elif num == 4:
        x -= 1
    elif num == 9:
        x += sqr2
        y += sqr2
    elif num == 7:
        x -= sqr2
        y += sqr2
    elif num == 3:
        x += sqr2
        y -= sqr2
    elif num == 1:
        x -= sqr2
        y -= sqr2

def Go(num,mode=None):
    global sqr2
    x = 0
    y = 0
    if num == 8:
        y += 1
    elif num == 2:
        y -= 1
    elif num == 6:
        x += 1
    elif num == 4:
        x -= 1
    elif num == 9:
        x += sqr2
        y += sqr2
    elif num == 7:
        x -= sqr2
        y += sqr2
    elif num == 3:
        x += sqr2
        y -= sqr2
    elif num == 1:
        x -= sqr2
        y -= sqr2
    elif num == 0:
        pass
    if mode == "x":
        return x
    elif mode == "y":
        return y

Mx = [[ Go(i,"x") + Go(j,"x") for j in xrange(0,10)] for i in xrange(0,10)]
My = [[ Go(i,"y") + Go(j,"y") for j in xrange(0,10)] for i in xrange(0,10)]

#sys.stdin = open("1413.txt")
s = raw_input().rstrip()
x = 0
y = 0
i = 0
while i < len(s):
    num = int(s[i:i+2])
    print num
    if len(str(num)) == 1:
        Goxy(num)
        break
    istep,jstep = str(num)
    istep = int(istep)
    jstep = int(jstep)
    x += Mx[istep][jstep]
    y += My[istep][jstep]
    i += 2
    if str(num).count("0") != 0:
        break
##    if num == 8:
##        y += 1
##    elif num == 2:
##        y -= 1
##    elif num == 6:
##        x += 1
##    elif num == 4:
##        x -= 1
##    elif num == 9:
##        x += sqr2
##        y += sqr2
##    elif num == 7:
##        x -= sqr2
##        y += sqr2
##    elif num == 3:
##        x += sqr2
##        y -= sqr2
##    elif num == 1:
##        x -= sqr2
##        y -= sqr2
print "%.10f %.10f" % (x,y)