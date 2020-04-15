# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-


from sys import stdin
import itertools

import time
fd = open('b.txt')
stdin = fd
start=time.time()

############################################

# read data for n sequences.
temp = stdin.readline().split()
N = int(temp[0])

data = []
write = stdin.readline().split()
for i in range(N):
    data.append(int(write[i]))

total = sum(data)

best = 1e6
buf = 0
for i in range(N):
    buf += data[i]
    score = abs(buf - (total-buf)) 
    if score < best:
        best = score

print(best)