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
                sum1 = 0                    
                for d in np.asarray([d for d in "RGB"]):
                    if i!=d and j!=d:
                        #sum1 = np.sum(np.asarray([d for d in data[jj+1:]])==d)
                        sum1 = 0
                        for l in data[jj+1:]:
                            if d == l:
                                sum1 +=1
                        let = d
                out+=sum1
                if jj+jj-ii<N:
                    if data[jj+jj-ii]==let:                    
                        out-=1
print(out)

