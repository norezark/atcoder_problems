N = int(input())
a = map(int, input().split())

def color(r):
    return min(r // 400, 8)

c = list(map(color, a))
cs = set(c)
cc = len(cs)
ac = c.count(8)
if ac == 0:
    print(cc, cc)
else:
    cc -= 1
    print(max(1,cc), cc+ac)