S = list(input())

cnt = 0
t = 0
for i in range(len(S)):
    if S[i] == 'W':
        cnt += t
    else:
        t += 1

print(cnt)
