# -*- coding: utf-8 -*-


from sys import stdin

import time
fd = open('a.txt')
stdin = fd
start=time.time()

############################################


# read data for n sequences.
input=[]
for _ in range(6):
    input.append(int(stdin.readline().split()[0]))
k=input[5]

ant = input[0:5]

x=0
for a in ant[:4]:
    for b in ant[1:]:
        if b-a <= k:
            continue
        else:
            x=1
            break

if x==0:
    print("Yay!")
else:
    print(":(")
#data = [int(stdin.readline().rstrip()) for _ in range(n)]
