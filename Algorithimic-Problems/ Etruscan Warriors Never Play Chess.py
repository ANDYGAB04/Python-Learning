import math

t = int(input())
for _ in range(t):
    n = int(input())
    s = math.isqrt(1 + 8 * n)
    k = (s - 1) // 2
    print(k)
