#!/bin/python3
# search a subgrid inside a grid
import sys

def equal(a, ai, aj, b):

    for i in range(len(b)):
        for j in range(len(b[0])):
            if a[ai+i][aj+j] != b[i][j]:
                return False
    return True

t = int(input().strip())
for a0 in range(t):
    R,C = input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in range(R):
       G_t = str(input().strip())
       G.append(G_t)
    r,c = input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in range(r):
       P_t = str(input().strip())
       P.append(P_t)
        
    for i in range(len(G)-len(P)+1):
        for j in range(len(G[0])-len(P[0])+1):
            if equal(G,i,j,P):
                print('YES')
                break
        else:
            continue
        break
    else:
        print('NO')
