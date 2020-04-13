N = int(input())
a = list(map(int, input().split()))

r = [0] * (10**5+2)
for i in range(N):
    r[a[i]] += 1
    r[a[i]+1] += 1
    r[a[i]+2] += 1

print(max(r))