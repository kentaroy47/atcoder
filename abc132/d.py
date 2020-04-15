# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-


from sys import stdin

import time
fd = open('d.txt')
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

data = sorted(data)

print(data[int(N/2)] - data[int(N/2)-1])