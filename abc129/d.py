# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-


from sys import stdin
import itertools

import time
fd = open('d.txt')
stdin = fd
start=time.time()

############################################

# read data for n sequences.
temp = stdin.readline().split()
N = int(temp[0])
M = int(temp[1])

A = stdin.readline().split()
card = []
for i in A:
    card.append(int(i))
card=sorted(card)
#print(card)

data = []
for i in range(M):
    write = stdin.readline().split()
    data.append(write)

for sousa in data:
    # sort card every time
    card=sorted(card)
    for i in range(int(sousa[0])):
        if card[i] < int(sousa[1]):
            card[i] = int(sousa[1])
        else:
            break

print(sum(card))

print(time.time()-start)