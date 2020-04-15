from sys import stdin
import numpy as np

import time
fd = open('b.txt')
stdin = fd
start=time.time()

############################################

# read data for n sequences.
temp = stdin.readline().split()
N, M = np.asarray(temp).astype(int)
temp = stdin.readline().split()
a = np.asarray(temp).astype(int)

sumvotes = np.sum(a)

c = 0; OUT = False
for data in a:
    if data >= sumvotes/(4*M):
        c += 1
    if c >= M:
        OUT = True
        #break

if OUT:
    print("Yes")
else:
    print("No")