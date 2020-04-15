from sys import stdin
import numpy as np

import time
fd = open('c.txt')
stdin = fd
start=time.time()

############################################

# read data for n sequences.
temp = stdin.readline().split()
N, K = np.asarray(temp).astype(int)

# K==1の場合
if K == 1:
    print(0)
    
elif N <= K:
    a = np.abs(N-K)
    if a < N:
        print(a)
    else:
        print(N)
else:
    rem = N%K
    print(np.abs(rem - K))
