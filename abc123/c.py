# -*- coding: utf-8 -*-

from sys import stdin

fd = open('c.txt')
stdin = fd

############################################

#from sys import stdin
import numpy as np

# read data for n sequences.
data = stdin.readline().split()
data=str(data)
data2=[]
for a in data[2:-2]:
    data2.append(int(a))
data=data2

start = data[0]
count=0
for i, c in enumerate(data):
    # end
    if i == len(data)-1:
        break
    # startと3こ続いた
    if c==start and data[i+1]==start:
        count+=2
        
    # 同じのが三個続いた
    if i!=0:
        if c==data[i-1]==data[i+1]:
            count+=2
            start=c

count0=0
for i, c in enumerate(data):
    if c==0:
        count0+=1
count1=len(data)-count0

if count1>count0:
    print(len(data)-(count1-count0))
else:
    print(len(data)-(count0-count1))

