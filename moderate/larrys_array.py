t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                cnt += 1
    if cnt%2:
        print('NO')
    else:
        print('YES')
