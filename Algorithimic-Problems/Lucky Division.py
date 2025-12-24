n = int(input().strip())
ok = False
for i in range(1, n + 1):
    s = str(i)
    if all(ch in "47" for ch in s):
        if n % i == 0:
            ok = True
            break

print("YES" if ok else "NO")
