# given n chapters, max k problems per page, a page can't have
# more than one chapter's problems, ti problems per chapter,
# a special problem is a problem who's number in the chapter is same
# as the page that holds it, how much such problems are there?
n, k = list(map(int, input().strip().split()))
t = list(map(int, input().strip().split()))

cnt = 0
p = 1
for c in range(n):
    q = 1
    while q <= t[c]:
        if q <= p < min(q+k, t[c]+1):
            cnt += 1
        q += k
        p += 1
print(cnt)
