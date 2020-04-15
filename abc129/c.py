# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-


from sys import stdin
import itertools

import time
fd = open('c.txt')
stdin = fd
start=time.time()

############################################

# read data for n sequences.
temp = stdin.readline().split()
N = int(temp[0])
M = int(temp[1])

data = []
for i in range(M):
    write = stdin.readline().split()
    data.append(write)

mina = 0
maxa = 10e7
for num in data:
    if int(num[0]) > mina:
        mina = int(num[0])
    if int(num[1]) < maxa:
        maxa = int(num[1]) 

count = maxa-mina+1

if count < 0:
    print(0)
else:
    print(count)
