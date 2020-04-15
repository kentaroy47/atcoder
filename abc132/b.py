# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-


from sys import stdin

#import time
#fd = open('b.txt')
#stdin = fd
#start=time.time()

############################################

# read data for n sequences.
temp = stdin.readline().split()
N = int(temp[0])

data = []
write = stdin.readline().split()
for i in range(N):
    data.append(int(write[i]))

count = 0
for i in range(N-2):
    array = sorted(data[i:i+3])
    if data[i+1]==array[1]:
        count += 1
        
print(count)