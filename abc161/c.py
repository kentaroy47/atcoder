from sys import stdin
import numpy as np

import time
fd = open('b.txt')
stdin = fd
start=time.time()

############################################

# read data for n sequences.
temp = stdin.readline().split()
N, K = np.asarray(temp).astype(int)

