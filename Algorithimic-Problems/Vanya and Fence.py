n, h = map(int, input().split())
vec = []
vec = input().split()
width = 0
for i in range(n):
    if int(vec[i]) > h:
        width += 2
    else:
        width += 1

print(width)
