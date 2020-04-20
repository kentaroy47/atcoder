# -*- coding: utf-8 -*-

############################################

# read data for n sequences.
N = int(input())
data = input()

out = 0
r=0;g=0;b=0;
for d in data:
    if d =="R":
        r+=1
    elif d=="B":
        b+=1
    else:
        g+=1
out = r*g*b

if N > 2:
    for ii, i in enumerate(data[:-2]):
        for jj,j in enumerate(data[ii+1:-1]):
            jj = jj+ii+1
            if i!=j:
                sum1 = 0                    
                for d in [d for d in "RGB"]:
                    if i!=d and j!=d:
                        let = d

                if jj+jj-ii<N:
                    if data[jj+jj-ii]==let:                    
                        out-=1
print(out)

