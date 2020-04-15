from sys import stdin
import numpy as np

import time
fd = open('d.txt')
stdin = fd
start=time.time()

############################################

# read data for n sequences.
temp = stdin.readline().split()
d = np.asarray(temp).astype(int)

c = 10
a = 11

if d <= 10:
    print(d)
else:
    while True:
        st = str(a)
        ok = 1
        for i,n in enumerate(st[1:]):
            if i == 0:
                dif = np.abs(int(n) - int(st[0]))
            else:
                dif = np.abs(int(n) - int(prev))
            if dif > 1:
                ok = 0
            prev = int(n)
        if ok == 1:
            c += 1
        if c == d:
            print(a)
            break     
        a += 1
        
            