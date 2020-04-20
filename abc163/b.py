# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-


from sys import stdin

import time
import numpy as np
fd = open('b.txt')
stdin = fd
start=time.time()

############################################

# read data for n sequences.
temp = stdin.readline().split()
N = int(temp[0])
M = int(temp[1])

data = []
write = stdin.readline().split()
for i in range(M):
    data.append(int(write[i]))

data = np.asarray(data)
data = np.sum(data)

if data > N:
    print(-1)
else:
    print(N-data)