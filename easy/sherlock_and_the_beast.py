#!/bin/python3
# find the largest number with n digits made of 5 and 3 where
# number of 5 is divisible by 3 and number of 3 is divisible by 5
import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    if n % 3 == 0:
        print('5'*n)
        continue
    
    i = n//3
    k = 0
    while i >= 0:
        if (n - i*3) % 5 == 0:
            break
        i-=1
    else:
        print('-1')
        continue
        
    print(('5'*(i*3))+('3'*(n-(i*3))))
