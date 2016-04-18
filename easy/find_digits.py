#!/bin/python3
# find number of n that divides n
import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    digits = list(map(int, str(n)))
    c = 0
    for d in digits:
        if d == 0:
            continue
        if n%d == 0:
            c+=1
    print(c)
