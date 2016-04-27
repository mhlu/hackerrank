#!/bin/python3

import sys
import math


s = input().strip()
s = ''.join(s.split())
l = len(s)
r = math.floor(math.sqrt(l))
c = math.ceil(math.sqrt(l))
if not (r*c>=l):
    r+=1
    
for j in range(c):
    for i in range(r):
        if i*c+j < l:
            print(s[i*c+j], end='')
    print(' ', end='')
