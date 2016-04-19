#!/bin/python3

import sys


n = int(input().strip())
s = input().strip()
k = int(input().strip())

for c in s:
    if c.isalpha():
        start = 'A' if c.isupper() else 'a'
        c = chr(  (ord(c)-ord(start)+k)%26 + ord(start)  )
    print(c, end='')

