import math
import copy
def convert(v, m, n):
    v = v%(2*n+2*m-4)
    p = v//(n+m-2)
    v = v%(n+m-2)
    if p == 0:
        if v < n:
            j = v
            i = 0
        else:
            j = n-1
            i = v-(n-1)
    elif p == 1:
        if v < n:
            j = (n-1)-v
            i = m-1
        else:
            j = 0
            i = (m-1)-(v-(n-1))
    return i, j

def rotate(arr, m, n, r):
    narr = copy.deepcopy(arr)
    for s in range(math.ceil(min(n,m)/2)):
        n1 = n-2*s
        m1 = m-2*s
        for j in range(n1*2+m1*2-4):
            v = (j-r)%(n1*2+m1*2-4)
            o_i, o_j = convert(j, m1, n1)
            n_i, n_j = convert(v, m1, n1)
            narr[s+n_i][s+n_j] = arr[s+o_i][s+o_j]
    return narr

m, n, r = tuple(map(int, input().strip().split()))
arr = []
for i in range(m):
    arr.append(list(map(int, input().strip().split())))
    
narr = rotate(arr, m, n, r)
for row in narr:
    for cell in row:
        print(cell, end=' ')
    print()
