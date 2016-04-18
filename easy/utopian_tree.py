#!/bin/python3
# double height during spring, grow by one during summer
import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if n % 2 == 0:
        k = 2**(n//2+1)-1
    else:
        k = 2**(n//2+1+1)-1-1
    print(k)
