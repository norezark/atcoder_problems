S = list(input())

s = 0
cl = 0
cc = S[0]
ccc = 0

def kaidan(k):
    return k * (k + 1) / 2

for i in range(len(S)):
    if S[i] == cc:
        ccc += 1
    else:
        if cc == '<':
            s += kaidan(ccc) + cl * ccc
            cl = ccc
        else:
            s += kaidan(ccc) - min(cl, ccc)
            cl = 0
        cc = S[i]
        ccc = 1

if cc == '<':
    s += kaidan(ccc) + cl * ccc
else:
    s += kaidan(ccc) - cl

print(int(s))
