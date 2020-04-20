# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 21:27:49 2020

@author: arute
"""


from sys import stdin

import time
import numpy as np
import math

fd = open('d.txt')
stdin = fd
start=time.time()

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

############################################

# read data for n sequences.
temp = stdin.readline().split()
N = int(temp[0])
M = int(temp[1])

# すべての場合の数を計算。
probs = np.zeros(1).astype("int64")

for i,m in enumerate(range(M,N+2)):
    # 作れる最小は？
    if i == 0:
        small = np.sum(np.arange(m))
        #
        large = np.sum(np.arange(N+1-m,N+1))
    else:
        small = (small+m-1).astype("int64")
        large = (large + (N+1-m)).astype("int64")
    probs = probs + (large - small + 1)

print(int(probs%(1e9+7)))
