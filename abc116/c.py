# -*- coding: utf-8 -*-

from sys import stdin

fd = open('c.txt')
stdin = fd

############################################

#from sys import stdin
import numpy as np

# read data for n sequences.
n = int(stdin.readline())
data = np.zeros(n)
d = stdin.readline().split()
for i,x in enumerate(d):
    data[i] = int(x)

out = 0

for i,x in enumerate(data):
    
    # pick smallest data not zero.
    for offset in range(0, len(data)-i):
        if data[i+offset] < 1:
            break
        if offset == len(data)-i-1:
            offset += 1
    if not data[i]==0:
        if len(data[i:i+offset])>1:
            minnum = np.min(data[i:i+offset])
        else:
            minnum = 0
        for x in range(offset):
            data[i+x] -= minnum
        
        out += minnum
        out += data[i]
#    print(data)
#    print(offset)

   
    
           
print(int(out))