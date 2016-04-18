#!/bin/python3

import sys

from itertools import groupby

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
arr.sort()
cnt_arr = [len(list(g)) for k, g in groupby(arr)]
for i in cnt_arr:
    print(n)
    n -= i
