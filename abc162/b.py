# -*- coding: utf-8 -*-

from sys import stdin

import time
import numpy as np
import math

fd = open('b.txt')
stdin = fd
start=time.time()

############################################

# read data for n sequences.
temp = stdin.readline().split()
N = int(temp[0])+1

out = 0
for i in range(1,N):
    for j in range(1,N):
        part = np.gcd(j,i)
        #for k in range(1,N):       
        out += np.sum(np.gcd(part,np.arange(1,N)))
print(out)