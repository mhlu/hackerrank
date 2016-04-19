t = int(input().strip())
for test in range(t):
    s = set([0])
    n = int(input().strip())
    a = int(input().strip())
    b = int(input().strip())
    for i in range(n-1):
        newS = set()
        for e in s:
            newS.add(e+a)
            newS.add(e+b)
        s = newS
    for j in sorted(s):
        print(j, end=' ')
    print()
