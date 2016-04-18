#!/bin/python3
# check if class cancelled due to too many people arriving late
import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    cnt = sum(1 for s in a if s <=0 )
    print('YES' if cnt < k else 'NO')
