# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-


from sys import stdin
import itertools

import time
fd = open('agc.txt')
stdin = fd
start=time.time()

############################################

# read data for n sequences.
temp = stdin.readline().split()
N = int(temp[0])
A = int(temp[1])
B = int(temp[2])
C = int(temp[3])
D = int(temp[4])

a = stdin.readline().split()
rock = []
for i in a[0]:
    rock.append(i)
    
# which one is further?
ok = 0
if D>C:
    if D-1 == len(rock):
        rock2 = rock[C-2:D-1]
    else:
        rock2 = rock[C-2:D]
else:
    if C-1 == len(rock):
        rock2 = rock[D-2:C-1]
    else:
        rock2 = rock[D-2:C]
if D > C:
    # place sunuke
    rock2 = rock
    rock2[A-1] = "#"
    # AがBより先にいる場合、避難場所があるか探索。
    
    
    
    for i,elem in enumerate(rock2[B-1:D-1]):
        # check if two rocks exist
        if elem=="#" and rock2[i+1]=="#":
            # rock2から3個以上開いてる場所はある？
            # Dは含まない。
            
            ok = 1    
            break
        # place sunuke
        rock[D-1] = "#"
    for i,elem in enumerate(rock[A-1:C-1]):
        if elem=="#" and rock[i+1]=="#":
            ok = 1    
            break
else:
    # place sunuke
    rock2 = rock
    # 
#    rock2[B-1] = "#" 
    for i,elem in enumerate(rock2[A-1:C-1]):
        # check if two rocks exist
        if elem=="#" and rock2[i+1]=="#":
            ok = 1    
            break
        rock[C-1] = "#"
    for i,elem in enumerate(rock[B-1:D-1]):
        if elem=="#" and rock[i+1]=="#":
            ok = 1    
            break
if ok == 0:
    print("Yes")
else:
    print("No")