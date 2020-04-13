S = input()

l = len(S)
for i in range(l-2,0,-2):
    # print(S[i//2:i], S[0:i//2])
    if S[i//2:i] == S[0:i//2]:
        print(i)
        break