A, B, C = map(int, input().split())

from fractions import gcd
print('YES' if C % gcd(A, B) == 0 else 'NO')