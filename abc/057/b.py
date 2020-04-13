N, M = map(int, input().split())
sp = [list(map(int, input().split())) for i in range(N)]
cp = [list(map(int, input().split())) for i in range(M)]

def mah(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

sci = []

for i in range(N):
    mindis = 0
    minind = 0
    for j in range(M):
        m = mah(sp[i], cp[j])
        if j == 0 or mindis > m:
            mindis = m
            minind = j
    sci.append(minind+1)

print('\n'.join(map(str, sci)))