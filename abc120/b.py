# -*- coding: utf-8 -*-


from sys import stdin
import numpy as np

import time
fd = open('b.txt')
stdin = fd
start=time.time()

############################################

# read data for n sequences.
input2=(stdin.readline().split())
input3=[]
for a in input2:
    input3.append(int(a))
A=[]
B=[]
C=[]
K=input3[3]
input=stdin.readline().split()
for a in input:
    A.append(int(a))
input=stdin.readline().split()
for a in input:
    B.append(int(a))
input=stdin.readline().split()
for a in input:
    C.append(int(a))

aind=len(A)-1
bind=len(B)-1
cind=len(C)-1

ans=[]

def whichmin(a,min):
    for i,b in enumerate(a):
        if min == b:
            return(i)
            break
        
while(K>0):
    # max ans
    ans = A[aind] + B[bind] + C[cind]
    print(ans)
    
    # start loop
    inpt=[A[aind],B[bind],C[cind]]
    amin = np.max([A[aind],B[bind],C[cind]])
    amin = int(amin)
    i = whichmin(inpt,amin)
    if i == 0:
        keep = [A[aind],A[aind-1]]
        gen1 = [B,bind]
        gen2 = [C,cind]
    elif i == 1:
        keep = [B[bind],B[bind-1]]
        gen1 = [A,aind]
        gen2 = [C,cind]
    else:
        keep = [C[cind],C[cind-1]]
        gen1 = [A,aind]
        gen2 = [B,bind]

    # search
    while (gen1[0][gen1[1]]<keep[1] and gen2[0][gen2[1]]<keep[1]):
        if gen1[0][gen1[1]] < gen2[0][gen2[1]]:
            gen1[1] -= 1
        else:
            gen2[1] -= 1
        a = gen1[0][gen1[1]]
        b = gen2[0][gen2[1]]
        c = keep[0]
        print(a+b+c)    
        K -= 1
    if i==0:
        aind -= 1
    elif i==1:
        bind -= 1
    else:
        cind -= 1
    