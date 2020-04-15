# -*- coding: utf-8 -*-

from sys import stdin

fd = open('b.txt')
stdin = fd

############################################

from sys import stdin

# read data for n sequences.
n = int(stdin.readline().rstrip())
data = [int(stdin.readline().rstrip()) for _ in range(n)]

data = sorted(data, reverse=True)
data[0] *= 0.5
data[0] = int(data[0])

print(sum(data))