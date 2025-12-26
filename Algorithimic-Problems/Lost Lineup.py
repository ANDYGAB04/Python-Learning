n = int(input())
numbers = input().split()
dicti = {-1: 1}
li = list(map(int, numbers))
for i in range(n - 1):
    dicti.update({li[i]: i + 2})

dicti = dict(sorted(dicti.items()))

for i in dicti.values():
    print(i, end=" ")
