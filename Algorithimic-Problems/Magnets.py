number = int(input())
groups = 1
first = str(input())
for i in range(number - 1):
    string = str(input())
    if string != first:
        groups += 1
    first = string

print(groups)
