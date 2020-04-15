# -*- coding: utf-8 -*-

from sys import stdin

fd = open('d.txt')
stdin = fd

############################################

#from sys import stdin
import numpy as np

# read data for n sequences.
n = stdin.readline().split()
N = int(n[0])
K = int(n[1])

data = stdin.readline().split()
data = str(data)[1:-1][1:-1]

# 1の数の要素にエンコード
# [1の数,次の1までの0の数]

list2=[]
if N == 1:
    print(N)
else:
    data2 = []
    count1=0
    count0=0
    for a in data:
        a = int(a)
        if count0 == 0:
            if a == 1:
                count1+=1
            else:
                count0+=1
        else:
            if a == 0:
                count0+=1
            else:
                data2.append([count1, count0])
                count1=1
                count0=0
    data2.append([count1, count0])
    
    if len(data2)==1:
        print(np.sum(data2))
    else: 
        for i,d in enumerate(data2[:-(K)]):
            sum2=0
            point=i
            for k in range(K+1):
                if k==K:
                    sum2+=(data2[point+k][0])
                else:
                    sum2+=(data2[point+k][0]+data2[point+k][1])
            list2.append(sum2)
        print(max(list2))

# 隣あうK+1コの要素で最大の部分を選ぶ。
# 分割しているときに計算もすればTLEを防げそう.
        