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


r = np.sum(np.asarray([d for d in data])=="R")
g = np.sum(np.asarray([d for d in data])=="G")
b = np.sum(np.asarray([d for d in data])=="B")
out = r*g*b

if N > 2:
    for ii, i in enumerate(data[:-2]):
        for jj,j in enumerate(data[ii+1:-1]):
            jj = jj+ii+1
            if i!=j:
                sum1 = 0                    
                for d in np.asarray([d for d in "RGB"]):
                    if i!=d and j!=d:
                        let = d
                if jj+jj-ii<N:
                    if data[jj+jj-ii]==let:                    
                        out-=1
print(out)

