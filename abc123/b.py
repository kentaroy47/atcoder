# -*- coding: utf-8 -*-


from sys import stdin

import time
fd = open('b.txt')
stdin = fd
start=time.time()

############################################

import numpy as np
# read data for n sequences.
n = stdin.readline().split()
a = int(n[0])
b = int(n[1])
c = int(n[2])

ans = []
for i in range(1, a+1):
    if a%i==0:
        ans.append(i)
ans=sorted(ans,reverse=True)
if a == 1:
    ans=[1]
count=0

for i in ans:
    if b%i==0:
        count+=1
    if count==c:
        break
print(i)