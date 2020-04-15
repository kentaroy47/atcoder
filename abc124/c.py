# -*- coding: utf-8 -*-

from sys import stdin

fd = open('c.txt')
stdin = fd

############################################

#from sys import stdin
import numpy as np

# read data for n sequences.
data = stdin.readline().split()
data2 = str(data)[1:-1][1:-1]

# 0101...
count1=0
count2=0
data = data[1:-1]

for i,a in enumerate(data2[1:-1]):
    a = int(a)
    if i %2 == 0:
        if a == 1:
            count1+=1
        else:
            count2+=1
    else:
        if a == 0:
            count1+=1
        else:
            count2+=1
    
if count1<count2:
    count=count1
else:
    count=count2
print(count)
#count2=0
# 1010..