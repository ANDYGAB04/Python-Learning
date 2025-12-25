number = int(input())
numbers = input().split()
li = list(numbers)
li = list(map(int, li))
maxlength = 1
nr = 1
for i in range(len(li) - 1):
    if li[i] >= li[i + 1]:
        nr = 1
    elif li[i] < li[i + 1]:
        nr += 1
    maxlength = max(maxlength, nr)

print(maxlength)
