H, W = map(int, input().split(' '))
S = [list(input()) for _ in range(H)]

def p(i, j):
    if S[i][j] == '#':
        return 1
    return 0

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            continue
        
        cnt = 0
        if i != 0:
            if j != 0:
                cnt += p(i-1,j-1)
            cnt += p(i-1,j)
            if j != W-1:
                cnt += p(i-1,j+1)

        if j != 0:
            cnt += p(i,j-1)
        if j != W-1:
            cnt += p(i,j+1)
        
        if i != H-1:
            if j != 0:
                cnt += p(i+1,j-1)
            cnt += p(i+1,j)
            if j != W-1:
                cnt += p(i+1,j+1)
        
        S[i][j] = str(cnt)

print('\n'.join([''.join(S[i]) for i in range(H)]))