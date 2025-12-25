number = int(input())
numbers = input().split()
li = list(numbers)
maxvalue = li[0]
minvalue = li[0]
amazingperformances = 0
for i in li[1:]:
    if int(maxvalue) < int(i):
        maxvalue = i
        amazingperformances += 1
    if int(minvalue) > int(i):
        minvalue = i
        amazingperformances += 1

print(amazingperformances)
