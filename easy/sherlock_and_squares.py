# find number of squares between a and b
import math
t = int(input().strip())
for i in range(t):
    A, B = tuple(map(int, input().strip().split()))
    a = math.ceil(math.sqrt(A))
    b = math.floor(math.sqrt(B))
    if b >= a:
        print(b-a+1)
    else:
        print(0)
