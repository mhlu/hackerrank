#!/bin/python3

import sys


# expect x >= y
def calc(b,w,x,y,z):
    x2 = min(x, y+z)
    return b*x2+w*y

t = int(input().strip())
for a0 in range(t):
    b,w = input().strip().split(' ')
    b,w = [int(b),int(w)]
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    if x >= y:
        print(calc(b,w,x,y,z))
    else:
        print(calc(w,b,y,x,z))
