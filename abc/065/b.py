N = int(input())
a = [int(input()) for _ in range(N)]
now = 1
cnt = 0
while now != 2 and cnt <= N:
    now = a[now-1]
    cnt += 1
if cnt > N:
    print(-1)
else:
    print(cnt)