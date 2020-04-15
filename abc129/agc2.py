# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-


from sys import stdin
import itertools

import time
fd = open('agc.txt')
stdin = fd
start=time.time()

############################################

# read data for n sequences.
temp = stdin.readline().split()
data=[]
prev="A"
for i,letter in enumerate(temp[0]):
    if not i==len(temp[0])-1:
        next = temp[0][i+1]
    else:
        next="B"
    if letter=="A":
        if next=="B" or next=="A":
            data.append("A")
        prev = "A"
    elif letter=="B" and next=="C":
        data.append("T")
        prev="T"
    else:
        if not prev=="X" and not prev=="T":
            data.append("X")
        if prev=="T":
            prev="C"
        else:
            prev="X"

prev="A"

count=0
next=0
prev=[]
for i,d in enumerate(data):
#    print(d)
    if d=="A":
        next+=1
        prev.append("A")
    elif d=="T" and "A" in prev:
        next+=1
        prev.append("T")
    elif d=="X":
        if "A" in prev and "T" in prev:
            count+=next-1
        next=0
        prev=[]
print(count)