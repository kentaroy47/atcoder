# -*- coding: utf-8 -*-


from sys import stdin

import time
fd = open('b.txt')
stdin = fd
start=time.time()

############################################
#from sys import stdin
import numpy as np

# read data for n sequences.
n = int(stdin.readline())
data = np.zeros(n)
d = stdin.readline().split()
for i,x in enumerate(d):
    data[i] = int(x)

max = np.max(data)
if max >= (np.sum(data)-max):
    print("No")
else:
    print("Yes")