import math
from itertools import dropwhile
cnt = 0
p = int(input().strip())
q = int(input().strip())

for i in range(p, q+1):
    arr = list(str(i**2))
    split = len(str(i))
    a = arr[:-split]
    b = list(dropwhile(lambda x: x=='0', arr[-split:]))
    if b == []:
        b = 0
    else:
        b = int(''.join(b))
        
    if a == []:
        a = 0
    else:
        a = int(''.join(a))
    if a + b == i:
        print(i, end=' ')
        cnt += 1
        
if cnt == 0:
    print('INVALID RANGE', end='')
print()
