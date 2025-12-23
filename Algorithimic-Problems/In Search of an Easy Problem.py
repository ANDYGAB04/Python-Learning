n = int(input())
integers = input()

vector = [int(num) for num in integers.split()]

if 1 in vector:
    print("HARD")
else:
    print("EASY")
