testcases = int(input())
while testcases > 0:
    number = int(input())
    numbers = input().split()
    li1 = list(map(int, numbers))
    numbers = input().split()
    li2 = list(map(int, numbers))

    changes = 0
    for i in range(number):
        if li1[i] > li2[i]:
            changes += 1
            li1.insert(i, li2[i])
            li1.pop()

    print(changes)
    testcases -= 1
