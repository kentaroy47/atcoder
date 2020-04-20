# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 21:27:49 2020

@author: arute
"""


from sys import stdin

import time
import numpy as np
fd = open('c.txt')
stdin = fd
start=time.time()

############################################

# read data for n sequences.
temp = stdin.readline().split()
N = int(temp[0])

data = []
write = stdin.readline().split()
for i in range(N-1):
    data.append(int(write[i]))

data = np.asarray(data)

out = np.zeros(N)
for d in data:
    out[d-1] += 1

o = ""
for l in out:
    o+=str(int(l))+"\n"

print(o)