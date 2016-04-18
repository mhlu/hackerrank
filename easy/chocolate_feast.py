#!/bin/python3
# how many chocolate can you eat if you have n dollars
# each chocolate cost c dollars or m chocolate wrappers
import sys


t = int(input().strip())
for a0 in range(t):
    n,c,m = input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]

    cnt = n//c
    wrapper = cnt
    while wrapper >= m:
        cnt += wrapper//m
        wrapper = wrapper//m + wrapper%m
    print(cnt)
