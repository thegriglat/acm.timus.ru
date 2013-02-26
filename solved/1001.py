#!/usr/bin/python
import sys,math,re
sys.stdin = open("1001.txt","r")
a = re.sub("\s+"," ",sys.stdin.read().replace("\n"," ")).split(" ")
while "" in a:
    del a[a.index("")]
for i in xrange(len(a) - 1,-1,-1):
    print "%.4f" % math.sqrt(float(a[i]))
