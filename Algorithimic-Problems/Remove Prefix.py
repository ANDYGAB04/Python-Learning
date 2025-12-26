t = int(input())
out_lines = []

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    seen = set()
    i = n - 1
    while i >= 0 and arr[i] not in seen:
        seen.add(arr[i])
        i -= 1

    out_lines.append(str(i + 1))

print("\n".join(out_lines))
