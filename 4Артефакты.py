from collections import defaultdict
n, m = map(int, input().split())
a, c, d, l, tres, res = [], defaultdict(int), 0, 0, (10**18, -1, -1), {}

for i in range(n):
    for x in map(int, input().split()): a.append((x, i))
a = sorted(a)


for r in range(len(a)):
    v, e = a[r]
    c[e] += 1
    if c[e] == 1: d += 1

    while d == n:
        if a[r][0] - a[l][0] < tres[0]: tres = (a[r][0] - a[l][0], l, r)
        v2, e2 = a[l]
        c[e2] -= 1
        if c[e2] == 0: d -= 1
        l += 1

t, l, r = tres
for i in range(l, r + 1):
    v, e = a[i]
    if e not in res: res[e] = v

print(*sorted(res.values()))