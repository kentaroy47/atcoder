# -*- coding: utf-8 -*-

from sys import stdin

import time
import numpy as np
import math

fd = open('d.txt')
stdin = fd

############################################

# read data for n sequences.
temp = stdin.readline().split()
N = int(temp[0])
temp = stdin.readline().split()
data = temp[0]


out = 0

if N > 2:
    for ii, i in enumerate(data[:-2]):
        for jj,j in enumerate(data[ii+1:-1]):
            jj = jj+ii+1
            if i!=j:
                for kk, k in enumerate(data[jj+1:]):
                    kk = kk+jj + 1
                    if i!=k and j!=k:
                        if (jj-ii) != (kk-jj):
                            out+=1
print(out)

