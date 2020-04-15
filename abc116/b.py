# -*- coding: utf-8 -*-


from sys import stdin

import time
fd = open('b.txt')
stdin = fd
start=time.time()

############################################

import numpy as np
# read data for n sequences.
n = stdin.readline().split()
a = int(n[0])

out = np.zeros(1000000)
out[0] = int(a)

for i,x in enumerate(out[:-1]):
    # do func.
    if a%2 == 0:
        a/=2
    else:
        a=a*3+1
    # check if m exists   
    if a in out:
        answer = i+2
        break
    out[i+1]=int(a)
    
print(int(answer))

end = time.time()
print(end-start)