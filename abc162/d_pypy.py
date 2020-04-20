# -*- coding: utf-8 -*-

############################################

# read data for n sequences.
N = int(input())
data = input()

out = 0

if N > 2:
    for ii, i in enumerate(data[:-2]):
        for jj,j in enumerate(data[ii+1:-1]):
            jj = jj+ii+1
            if i!=j:
                for kk, k in enumerate(data[jj+1:]):
                    kk = kk+jj + 1
                    if i!=k and j!=k:
                        if (jj-ii) != (kk-jj):
                            out+=1
print(out)

