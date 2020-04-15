# -*- coding: utf-8 -*-


from sys import stdin

import time
fd = open('c.txt')
stdin = fd
start=time.time()

############################################
#from sys import stdin
import numpy as np

# read data for n sequences.
input = stdin.readline().split()
m = int(input[0])
n = int(input[1])
#n = int(stdin.readline().split()[1])
data = np.zeros(n)
d = stdin.readline().split()
for i,x in enumerate(d):
    data[i] = int(x)
data = sorted(data)

dif = np.zeros(len(data)-1)
for x in range(0, len(data)-1):
    dif[x] = data[x+1]-data[x]

out = 0

# split in m data.
#print(data)
dif = np.zeros(len(data)-1)
for x in range(0, len(data)-1):
    dif[x] = data[x+1]-data[x]
out = sum(sorted(dif, reverse=True)[m-1:])

            

print(int(out))
            