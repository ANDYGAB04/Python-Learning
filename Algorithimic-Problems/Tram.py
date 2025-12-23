n = int(input())

maxcapacity = 0
capacity = 0
for i in range(n):
    a, b = map(str, input().split())
    a = int(a)
    b = int(b)
    capacity -= a
    capacity += b
    maxcapacity = max(capacity, maxcapacity)

print(maxcapacity)
